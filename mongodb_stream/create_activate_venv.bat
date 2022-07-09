@echo off
:: virtualenv venv
:: source venv/bin/activate
:: pip3 install -r requirements.txt

call %~dp0venv\Scripts\activate.bat
call %~dp0venv\Scripts\pip3 install -r requirements.txt
pause
