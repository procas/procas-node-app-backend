from flask import Flask, request, jsonify

import repository
from Security import authentication
from Services import videoHelper
from Services import noteHelper
from Models.User import *
from Models.register_response import *
from Models.login_response import *
from Models.video_response import *
from Models.note_response import *
from repository import *
import ssl

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def reg():
    context = ssl.create_default_context()
    email = request.args.get('email')
    pwd = request.args.get('pass')
    if authentication.valid(User(email, pwd), context):
        r = RegisterResponse('200', 'Success')
    else:
        r = RegisterResponse('500', 'Error')
    return jsonify(r.__dict__)

@app.route('/validate', methods=['GET'])
def validate():
    token = request.args.get('tkn')
    if authentication.isTokenValid(token):
        r = RegisterResponse('200', 'Success')
    else:
        r = RegisterResponse('500', 'Error')
    return jsonify(r.__dict__)

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    pwd = request.args.get('password')
    # check if password matched and email is validated
    if authentication.validLogin(User(email, pwd)):
        r = LoginResponse('200', 'Logged in', authentication.jwtEncode(email))
    else:
        r = LoginResponse('500', 'Error', '')
    return jsonify(r.__dict__)

@app.route('/upload', methods=['GET'])
def upload():
    token = request.form.get('token')
    file = request.files['file']
    title = request.args.get('title')
    if authentication.isValidJWT(token)[0]:
        r = videoHelper.upload_video(file, title, authentication.isValidJWT(token)[1])
    else:
        r = VideoResponse('401', 'Unauthorized', '')
    return jsonify(r.__dict__)

@app.route('/uploadnote', methods=['POST'])
def upload_note():
    data = request.get_json()
    title = data['title']
    detail = data['detail']
    token = data['token']
    if authentication.isValidJWT(token)[0]:
        email = authentication.isValidJWT(token)[1]
        r = noteHelper.save_note(email, title, detail)
    else:
        r = VideoResponse('401', 'Unauthorized', '')
    return jsonify(r.__dict__)


@app.route('/getnotes', methods=['GET'])
def getnotes():
    token = request.args.get('token')
    if authentication.isValidJWT(token)[0]:
        email = authentication.isValidJWT(token)[1]
        try:
            return jsonify(noteHelper.get_notes(email))
        except:
            n = NoteResponse('500', 'Internal Server Error')
    else:
        n = NoteResponse('401', 'Unauthorized')
    return jsonify(n.__dict__)


@app.route('/deletenote', methods=['GET'])
def deletenote():
    id = request.args.get('id')
    token = request.args.get('token')
    if authentication.isValidJWT(token)[0]:
        n = noteHelper.delete_note(id)
    else:
        n = NoteResponse('401', 'Unauthorized')
    return jsonify(n.__dict__)


@app.route('/modifynote', methods=['POST'])
def modifynote():
    data = request.get_json()
    id = data['id']
    title = data['title']
    detail = data['detail']
    token = data['token']
    if authentication.isValidJWT(token)[0]:
        n = noteHelper.modify_note(id, title, detail)
    else:
        n = NoteResponse('401', 'Unauthorized')
    return jsonify(n.__dict__)


if __name__ == "__main__":
    # app.run(host="localhost", port=8080)
     app.run(host="localhost", port=8080)
