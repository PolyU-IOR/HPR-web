@echo off
setlocal

REM === Resolve paths relative to this script ===
set "ROOT=%~dp0"
set "SITE=%ROOT%site"
set "DOCS=%ROOT%docs"
set "LANDING=%ROOT%landing"
set "ASSETS=%ROOT%assets"

REM === Clean site ===
if exist "%SITE%" rmdir /s /q "%SITE%"
mkdir "%SITE%"

REM === Build Sphinx projects ===
sphinx-build -b html "%DOCS%\hprlp" "%SITE%\hprlp"
sphinx-build -b html "%DOCS%\hprqp" "%SITE%\hprqp"

REM === Copy landing files to site root (index.html, CSS, JS, images, etc.) ===
REM robocopy is reliable and included in Windows
robocopy "%LANDING%" "%SITE%" *.* /E /NFL /NDL /NJH /NJS /NP >nul

REM === Mirror assets (avatars, images, css/js if any) to site/assets ===
robocopy "%ASSETS%" "%SITE%\assets" /MIR /NFL /NDL /NJH /NJS /NP >nul

REM === Ensure .nojekyll so _static/_sources are served on GitHub Pages ===
type nul > "%SITE%\.nojekyll"

echo Done. Open "%SITE%\index.html"

