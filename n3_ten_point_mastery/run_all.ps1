param(
    [string]$Action = "menu",
    [int]$Port = 8000,
    [switch]$NoBrowser
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$script:LastActionExitCode = 0

try {
    [Console]::InputEncoding = [System.Text.Encoding]::UTF8
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
} catch {
}
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

function Resolve-N3Python {
    $candidates = @()
    $venvPy = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
    if (Test-Path $venvPy) {
        $candidates += ,@($venvPy, @())
    }
    $candidates += ,@("py", @("-3.11"))
    $candidates += ,@("py", @("-3"))
    $candidates += ,@("python", @())

    foreach ($cand in $candidates) {
        $exe = $cand[0]
        $prefix = $cand[1]
        if (-not (Test-Path $exe) -and -not (Get-Command $exe -ErrorAction SilentlyContinue)) {
            continue
        }
        try {
            & $exe @prefix -c "import fastapi, uvicorn, openpyxl, rich" *> $null
            if ($LASTEXITCODE -eq 0) {
                return @{ Exe = $exe; Prefix = $prefix }
            }
        } catch {
            continue
        }
    }
    return $null
}

$pyInfo = Resolve-N3Python
if ($null -eq $pyInfo) {
    Write-Host "[FAIL] Không tìm thấy Python 3.11+ có đủ thư viện (fastapi, uvicorn, openpyxl, rich)." -ForegroundColor Red
    Write-Host "Hãy cài đặt hoặc kiểm tra lệnh: py -3.11 -m pip install fastapi uvicorn openpyxl rich"
    exit 1
}

function Invoke-N3Cli {
    param([string[]]$CliArgs)
    Push-Location $ProjectRoot
    try {
        $argsList = @()
        if ($pyInfo.Prefix) { $argsList += $pyInfo.Prefix }
        $argsList += (Join-Path $ProjectRoot "n3_cli.py")
        $argsList += $CliArgs
        & $pyInfo.Exe @argsList
        $script:LastActionExitCode = [int]$LASTEXITCODE
    } finally {
        Pop-Location
    }
}

function Invoke-FullVerification {
    Push-Location $ProjectRoot
    try {
        $astScript = "D:\Working-kit\scripts\verify_ast.py"
        if (Test-Path $astScript) {
            Write-Host "[INFO] 1/3 Kiểm tra cú pháp Python & JSON..."
            $astArgs = @()
            if ($pyInfo.Prefix) { $astArgs += $pyInfo.Prefix }
            $astArgs += $astScript
            $astArgs += $ProjectRoot
            & $pyInfo.Exe @astArgs
            $script:LastActionExitCode = [int]$LASTEXITCODE
            if ($script:LastActionExitCode -ne 0) { return }
        }

        if (Get-Command "node" -ErrorAction SilentlyContinue) {
            Write-Host "[INFO] 2/3 Kiểm tra cú pháp JavaScript (app.js)..."
            & node --check (Join-Path $ProjectRoot "n3_mastery\static\app.js")
            $script:LastActionExitCode = [int]$LASTEXITCODE
            if ($script:LastActionExitCode -ne 0) { return }
        }

        Write-Host "[INFO] 3/3 Chạy toàn bộ bộ kiểm thử tự động (pytest)..."
        $ptArgs = @()
        if ($pyInfo.Prefix) { $ptArgs += $pyInfo.Prefix }
        $ptArgs += @("-m", "pytest", (Join-Path $ProjectRoot "tests"), "-v")
        & $pyInfo.Exe @ptArgs
        $script:LastActionExitCode = [int]$LASTEXITCODE
    } finally {
        Pop-Location
    }
}

function Run-SingleAction {
    param([string]$ActName)
    $script:LastActionExitCode = 0
    $norm = ($ActName | ForEach-Object { $_.Trim().ToLowerInvariant() })
    switch ($norm) {
        "web" {
            $cliArgs = @("quickstart", "--port", "$Port")
            if ($NoBrowser) { $cliArgs += "--no-browser" }
            Invoke-N3Cli -CliArgs $cliArgs
        }
        "doctor" {
            Invoke-N3Cli -CliArgs @("doctor")
        }
        "status" {
            Invoke-N3Cli -CliArgs @("status")
        }
        "import" {
            Invoke-N3Cli -CliArgs @("import")
        }
        "backup" {
            Invoke-N3Cli -CliArgs @("backup")
        }
        "grammar" {
            Invoke-N3Cli -CliArgs @("grammar", "--exam-only")
        }
        "study" {
            Invoke-N3Cli -CliArgs @("study", "--limit", "5")
        }
        "test" {
            Invoke-FullVerification
        }
        default {
            Write-Host "[FAIL] Tác vụ không hợp lệ: '$ActName'. Hỗ trợ: menu, web, doctor, status, import, backup, grammar, study, test." -ForegroundColor Red
            $script:LastActionExitCode = 1
        }
    }
}

if ($Action.Trim().ToLowerInvariant() -ne "menu") {
    Run-SingleAction -ActName $Action
    exit $script:LastActionExitCode
}

while ($true) {
    Write-Host ""
    Write-Host "================================================================"
    Write-Host "  CHƯƠNG TRÌNH ÔN THI TIẾNG NHẬT CUỐI KÌ & JLPT N3 (10/10)"
    Write-Host "================================================================"
    Write-Host "  [1] Mở giao diện Web học tập (Khuyên dùng - tự mở trình duyệt)"
    Write-Host "  [2] Kiểm tra sức khỏe dữ liệu & hệ thống (doctor)"
    Write-Host "  [3] Xem điểm hiện tại & tiến độ 12 chủ đề (status)"
    Write-Host "  [4] Nạp lại toàn bộ file đề Excel (.xlsx) (import)"
    Write-Host "  [5] Sao lưu an toàn tiến độ học tập (.db) (backup)"
    Write-Host "  [6] Tra cứu nhanh ngữ pháp có trong đề thi (grammar)"
    Write-Host "  [7] Làm nhanh 5 câu hỏi trên cửa sổ dòng lệnh (study)"
    Write-Host "  [8] Chạy kiểm định kỹ thuật toàn bộ (AST + JS + Pytest)"
    Write-Host "  [0] Thoát"
    Write-Host "----------------------------------------------------------------"
    $choice = (Read-Host "Nhập số (0-8) rồi nhấn Enter").Trim()
    switch ($choice) {
        "1" { Run-SingleAction -ActName "web" }
        "2" { Run-SingleAction -ActName "doctor"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "3" { Run-SingleAction -ActName "status"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "4" { Run-SingleAction -ActName "import"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "5" { Run-SingleAction -ActName "backup"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "6" { Run-SingleAction -ActName "grammar"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "7" { Run-SingleAction -ActName "study"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "8" { Run-SingleAction -ActName "test"; [void](Read-Host "Nhấn Enter để quay lại menu...") }
        "0" { exit 0 }
        default { Write-Host "[WARN] Vui lòng nhập một số từ 0 đến 8." -ForegroundColor Yellow }
    }
}
