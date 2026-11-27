"""Start either packaged JLPT application from its local data directory."""

import argparse
from importlib import import_module
import os
from pathlib import Path
import socket
from threading import Event, Thread
import webbrowser

import uvicorn


SYSTEM_DIR = Path(__file__).resolve().parent.parent
LOCAL_ADDRESS = "127.0.0.1"


def open_when_started(server, url, finished):
    while not server.started:
        if finished.wait(0.1):
            return
    try:
        opened = webbrowser.open(url, new=2)
    except (OSError, webbrowser.Error):
        opened = False
    if not opened:
        print(f"Mở địa chỉ này trong trình duyệt: {url}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("app", choices=("mastery", "sprint"))
    parser.add_argument("--no-browser", action="store_true", help="Keep the browser closed")
    args = parser.parse_args()

    if args.app == "mastery":
        name, project, package, db_name, port = (
            "N3 Mastery 10/10", "n3_ten_point_mastery", "n3_mastery", "n3_mastery.db", 8010
        )
        path_vars = {
            "N3_MASTERY_DB_PATH": SYSTEM_DIR / project / "data" / db_name,
            "N3_MASTERY_EXCEL_DIR": SYSTEM_DIR / "exam_downloads",
        }
    else:
        name, project, package, db_name, port = (
            "JLPT N3 Sprint 7 ngày", "jlpt_study_system", "jlpt_study_system", "jlpt_study.db", 8000
        )
        path_vars = {
            "JLPT_DB_PATH": SYSTEM_DIR / project / "data" / db_name,
            "JLPT_SPRINT_DIR": SYSTEM_DIR / "jlpt_n3_sprint",
        }

    database = SYSTEM_DIR / project / "data" / db_name
    if not database.is_file():
        parser.exit(1, f"Thiếu cơ sở dữ liệu {db_name}. Hãy giải nén toàn bộ gói ZIP.\n")
    os.environ.update({key: str(path) for key, path in path_vars.items()})
    app = import_module(f"{package}.api").app

    with socket.socket() as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        try:
            listener.bind((LOCAL_ADDRESS, port))
        except OSError as error:
            if error.winerror not in (10013, 10048):
                raise
            listener.bind((LOCAL_ADDRESS, 0))
        address, actual_port = listener.getsockname()
        url = f"http://{address}:{actual_port}/"
        server = uvicorn.Server(uvicorn.Config(app, host=address, port=actual_port))
        finished = Event()
        print(f"{name} — {url}", flush=True)
        print("Giữ cửa sổ này mở khi học. Nhấn Ctrl+C để tắt.", flush=True)
        if not args.no_browser:
            Thread(target=open_when_started, args=(server, url, finished), daemon=True).start()
        try:
            server.run(sockets=[listener])
        finally:
            finished.set()
    return 0 if server.started else 1


if __name__ == "__main__":
    raise SystemExit(main())
