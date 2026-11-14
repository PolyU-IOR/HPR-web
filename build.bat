@echo off
setlocal
set "HPR_PYTHON=python"
if exist "%~dp0.venv\Scripts\python.exe" set "HPR_PYTHON=%~dp0.venv\Scripts\python.exe"
"%HPR_PYTHON%" "%~dp0tools\build_site.py" %*
exit /b %errorlevel%
