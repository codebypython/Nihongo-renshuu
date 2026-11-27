"""Build the Windows x64 ZIP from committed source and fresh study databases."""

import argparse
import hashlib
from io import BytesIO
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[2]
WINDOWS_FILES = "packaging/windows"
PACKAGE_NAME = "Language Lab - JLPT N3"
ZIP_NAME = "Language-Lab-JLPT-N3-Windows-x64.zip"
PYTHON_VERSION = "3.14.10"
PYTHON_SHA256 = "90905e64a840557d8c1bc4f5b74db3d7ee85e3ffb217611cac1c7813acea4159"
SOURCE_PATHS = ("exam_downloads", "jlpt_n3_sprint", "jlpt_study_system", "n3_ten_point_mastery")
LAUNCHERS = ("Mo N3 Mastery.cmd", "Mo JLPT Sprint 7 ngay.cmd", "DOC TRUOC.txt")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def unpack_source(system):
    source = git("archive", "--format=zip", "HEAD", "--", *SOURCE_PATHS)
    with ZipFile(BytesIO(source)) as archive:
        database_suffixes = {".db", ".sqlite", ".sqlite3"}
        if any(Path(member).suffix in database_suffixes for member in archive.namelist()):
            raise ValueError("Tạo bản phát hành từ mã nguồn và học liệu dự án.")
        archive.extractall(system)


def install_runtime(staging, runtime):
    download = staging / "python-embed.zip"
    url = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-embed-amd64.zip"
    with urlopen(url, timeout=45) as response, download.open("wb") as output:
        shutil.copyfileobj(response, output)
    with download.open("rb") as contents:
        checksum = hashlib.file_digest(contents, "sha256").hexdigest()
    if checksum != PYTHON_SHA256:
        raise ValueError("Mã SHA-256 của Python đóng gói không khớp.")
    with ZipFile(download) as archive:
        archive.extractall(runtime)

    path_file = runtime / "python314._pth"
    path_file.write_text(
        "python314.zip\n.\npackages\n../n3_ten_point_mastery\n../jlpt_study_system\n",
        encoding="ascii",
    )
    requirements = staging / "requirements.txt"
    requirements.write_bytes(git("show", "HEAD:requirements.txt"))
    constraints = staging / "runtime-constraints.txt"
    constraints.write_bytes(git("show", f"HEAD:{WINDOWS_FILES}/runtime-constraints.txt"))
    packages = runtime / "packages"
    subprocess.run(
        [
            sys.executable, "-m", "pip", "--isolated", "install", "--disable-pip-version-check",
            "--ignore-installed", "--only-binary=:all:", "--no-compile", "--platform", "win_amd64",
            "--python-version", PYTHON_VERSION, "--implementation", "cp", "--target", str(packages),
            "-r", str(requirements), "-c", str(constraints),
        ],
        check=True,
    )
    # Generated console entry points contain paths to the build machine.
    bin_dir = packages / "bin"
    if bin_dir.is_dir():
        for entry in bin_dir.iterdir():
            entry.unlink()
        bin_dir.rmdir()
    (runtime / "launch.py").write_bytes(git("show", f"HEAD:{WINDOWS_FILES}/launch.py"))


def seed(system):
    launcher = str(system / "runtime" / "python.exe")
    settings = {
        "JLPT_DB_PATH": system / "jlpt_study_system/data/jlpt_study.db",
        "JLPT_SPRINT_DIR": system / "jlpt_n3_sprint",
        "N3_MASTERY_DB_PATH": system / "n3_ten_point_mastery/data/n3_mastery.db",
        "N3_MASTERY_EXCEL_DIR": system / "exam_downloads",
    }
    environment = dict(os.environ, **{key: str(value) for key, value in settings.items()})
    for script, command in (
        ("jlpt_study_system/jlpt_cli.py", "init"),
        ("n3_ten_point_mastery/n3_cli.py", "import"),
    ):
        subprocess.run(
            [launcher, "-B", "-X", "utf8", str(system / script), command],
            env=environment, check=True,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / ZIP_NAME)
    args = parser.parse_args()
    if sys.platform != "win32":
        parser.error("Chạy công cụ đóng gói trên Windows 64-bit.")
    output = args.output.resolve()
    if output.exists():
        parser.error(f"Tệp đích đã tồn tại: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix="jlpt-build-", dir=output.parent) as temp:
        staging = Path(temp)
        package = staging / PACKAGE_NAME
        system = package / "he-thong"
        runtime = system / "runtime"
        unpack_source(system)
        install_runtime(staging, runtime)
        for name in LAUNCHERS:
            content = git("show", f"HEAD:{WINDOWS_FILES}/{name}")
            if name.endswith(".cmd"):
                content = content.replace(b"\n", b"\r\n")
            (package / name).write_bytes(content)
        seed(system)

        candidate = staging / ZIP_NAME
        with ZipFile(candidate, "w", compression=ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(staging).as_posix())
        with ZipFile(candidate) as archive:
            invalid = archive.testzip()
            if invalid:
                raise ValueError(f"Tệp ZIP không hợp lệ: {invalid}")
        candidate.rename(output)
    print(output)


if __name__ == "__main__":
    main()
