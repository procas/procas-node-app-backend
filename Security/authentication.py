import repository
from Services import sendEmail, generateToken
from Security import validateCreds
from repository import *
import jwt
import datetime
from Security.config import *


def valid(user, context):
    if repository.checkIfEmailExists(user.email):
        return False
    if not validateCreds.valid_email(user.email):
        return False
    else:
        try:
            # save
            user_res = saveUser(user)
            token = generateToken.get_uuid()
            token_res = saveToken(user.email, token)
            # send email
            try:
                sendEmail.send(user, token, context)
            except:
                return False
            return True
        except:
            return False


def isTokenValid(token):
    if repository.checkIfTokenExists(token):
        if repository.validateToken(token):
            return True
        else:
            return False
    else:
        return False


def jwtEncode(email):
    token = jwt.encode({
        'public_id': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, secret_key)
    return token

# returns the email id from token
def jwtDecode(token):
    return jwt.decode(token, secret_key, algorithms="HS256")['public_id']

def isValidJWT(token):
    try:
        mail_id = jwtDecode(token)
        if checkIfEmailExists(mail_id):
            return True, mail_id
        else:
            return False, None
    except:
        return False, None

def validLogin(user):
    if checkIfEmailExists(user.email) and checkIfPasswordMatchesAndIsValid(user.email, user.password):
        return True
    else:
        return False