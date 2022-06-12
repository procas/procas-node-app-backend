import datetime

from flask import jsonify
from sqlalchemy import create_engine
from Security.validateCreds import *
from sqlalchemy.sql import text
from Models.Note import *

cnx = create_engine('mysql+pymysql://'+db_name+':'+db_password+'@'+db_host+'/'+db_name+'')
conn = cnx.connect()


def checkIfEmailExists(email):
    query = 'CALL GetUsersByEmail(\'{email}\')'.format(email=email)
    try:
        cursor = cnx.execute(query)
        rows = cursor.fetchall()
    except:
        return "Unable to fetch by email"
    return len(rows) > 0


def checkIfPasswordMatchesAndIsValid(email, pwd):
    query = 'CALL GetUsersByEmail(\'{email}\')'.format(email=email)
    try:
        cursor = cnx.execute(query)
        row = cursor.fetchone()
        password = row["pass"]
        isValid = row["is_valid"]
        return password == createHash(pwd) and isValid == True
    except:
        return False

# print(checkIfPasswordMatchesAndIsValid('mailtoproma@gmail.com', '12356'))

def saveUser(user):
    query = 'CALL AddUser(\'{email}\', \'{pwd}\')'.format(email=user.email, pwd=createHash(user.password))
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False

def saveNote(email, title, detail):
    query = 'CALL SaveNote(\'{email}\', \'{title}\', \'{detail}\', \'{created_date}\')'.format(email=email, title=title, detail=detail, created_date=datetime.datetime.now())
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False

def getNotes(email):
    query = 'CALL GetNotes(\'{email}\')'.format(email=email)
    lis = []
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        rows = cursor.fetchall()
        for r in rows:
            note = {'id': r['id'], 'title': r['title'], 'detail': r['detail'], 'date': r['created_date']}
            lis.append(note)
       # print(lis)
        return lis
    except:
        return []


def deleteNote(id):
    query = 'CALL DeleteNote(\'{id}\')'.format(id=id)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False

def modifyNote(id, title, detail):
    query = 'CALL ModifyNote(\'{id}\', \'{title}\', \'{detail}\')'.format(id=id, title=title, detail=detail)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False

def saveToken(email, token):
    query = 'CALL SaveToken(\'{email}\',\'{token}\')'.format(email=email, token=token)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False


def checkIfTokenExists(token):
    query = 'CALL GetToken(\'{token}\')'.format(token=token)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        rows = cursor.fetchall()
        return len(rows) > 0
    except:
        return False

# video_name, extension, title, url, user_id
def saveVideo(vidname, ext, url, title, email):
    query = 'CALL SaveVideoDetails(\'{vidname}\', \'{ext}\', \'{title}\', \'{url}\', \'{email}\')'.format(vidname=vidname, ext=ext, url=url, title=title, email=email)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False


def validateToken(token):
    query = 'CALL ValidateToken(\'{token}\')'.format(token=token)
    try:
        cursor = cnx.execute(text(query).execution_options(autocommit=True))
        return True
    except:
        return False