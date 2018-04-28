import getpass
from . import media,core
logmode=False
def password(prompt='Please Enter Password: '):
    global logmode
    if logmode:
        print("Password")
    return getpass.getpass(prompt)
