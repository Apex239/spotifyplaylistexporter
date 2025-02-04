@echo off
REM Create virtual environment if it doesn't exist
if not exist venv (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Start the Flask app in a new window
start "" python app.py

REM Wait a few seconds to allow the server to start
timeout /t 2 /nobreak >nul

REM Open the default web browser to the app URL
start http://localhost:5000/

REM Print a message in the terminal
echo Server started. Go to http://localhost:5000/ in your browser.
pause
