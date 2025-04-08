@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo Running tests...
pytest tests\
if %ERRORLEVEL% EQU 0 (
    echo ✅ All tests passed!
    exit /b 0
) else (
    echo ❌ Some tests failed.
    exit /b 1
)
