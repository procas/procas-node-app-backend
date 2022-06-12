import re
import hashlib
from Security.config import *

def valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def createHash(user_entered_password):
    db_password = user_entered_password + salt
    h = hashlib.md5(db_password.encode())
    return h.hexdigest()