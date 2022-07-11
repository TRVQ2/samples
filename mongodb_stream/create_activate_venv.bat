@echo on
call python -m venv venv
call venv\Scripts\activate
call venv\Scripts\pip3 install -r requirements.txt
pause
