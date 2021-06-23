add documentation for following commands
1. `pip3 install virtualenv`
2. `virtualenv venv`
3.  1. if win10: `.\venv\Scripts\activate` (might need to `Set-ExecutionPolicy RemoteSigned` to run and `Set-ExecutionPolicy Restricted` after running for protection reason)
    2.    if linux/macos: `source venv/bin/activate`
4. `pip3 install -r requirements.txt`
5. `python main.py`
6. `deactivate` to exit venv