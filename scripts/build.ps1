# Windows build script for Coding Trainer (the Makefile's counterpart). Run: build <target>
# build.cmd starts this script without changing PowerShell's execution policy.
# Never touches your own files: work\ (your solutions) and progress.json.
param([string]$Target = "help")
$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot
Set-Location $Root

# Python launchers from the python.org installer; override with $env:PYTHON / $env:GUI_PYTHON.
$Python = if ($env:PYTHON) { $env:PYTHON } else { "py" }
$GuiPython = if ($env:GUI_PYTHON) { $env:GUI_PYTHON } else { "pyw" }
$Version = (Get-Content VERSION).Trim()
$Dist = Join-Path build "coding-trainer-$Version.zip"

function Get-Shortcut { Join-Path ([Environment]::GetFolderPath("Programs")) "Coding Trainer.lnk" }

function Invoke-Native($Exe, [string[]]$Arguments) {
    & $Exe @Arguments
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

switch ($Target) {
    "help" {
        "build run        start the desktop app"
        "build web        start the web app on http://localhost:8000"
        "build install    add Coding Trainer to the Start menu"
        "build uninstall  remove it from the Start menu"
        "build test       check generators, all 84 reference solutions and the capsule in 4 languages (in a temp copy)"
        "build dist       package the committed app (no docs/) as $Dist"
        "build clean      remove build\, src\__pycache__\ and the test cache"
    }
    "run" { Invoke-Native $GuiPython @("src\gui_tk.py") }
    "web" { Invoke-Native $Python @("src\app.py") }
    "install" {
        $shortcut = Get-Shortcut
        $link = (New-Object -ComObject WScript.Shell).CreateShortcut($shortcut)
        $link.TargetPath = (Get-Command $GuiPython).Source
        $link.Arguments = "`"$Root\src\gui_tk.py`""
        $link.WorkingDirectory = $Root
        $link.IconLocation = "$Root\assets\coding-trainer.ico"
        $link.Description = "Daily coding problems in C, C++, Python and Rust"
        $link.Save()
        "Installed $shortcut"
    }
    "uninstall" { Remove-Item (Get-Shortcut) -Force -ErrorAction Ignore }
    "test" { Invoke-Native $Python @("scripts\selftest.py") }
    "dist" {
        Invoke-Native $Python @("scripts\selftest.py")
        New-Item -ItemType Directory -Force build | Out-Null
        Invoke-Native git @("archive", "--format=zip", "--prefix=coding-trainer-$Version/", "-o", $Dist, "HEAD", "README.md", "VERSION", "Makefile", "build.cmd", "src", "problems", "assets", "scripts")
        "Built $Dist ($([math]::Round((Get-Item $Dist).Length / 1KB)) KB)"
    }
    "clean" { Remove-Item build, src\__pycache__, "$env:APPDATA\coding-trainer\cache" -Recurse -Force -ErrorAction Ignore }
    default {
        "Unknown target '$Target'. Run: build help"
        exit 1
    }
}
