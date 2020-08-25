from flask import Flask, render_template, sessions, request
import requests
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = "dangvansam"
socketio = SocketIO(app)
count = 0

@app.route('/')
def index():
    #print(requests.sid)
    return render_template("client.html")

@socketio.on('connect')
def connect():
    global count
    count += 1
    emit('count_client', {'count': count}, broadcast=True)

@socketio.on('disconnect')
def disconnect():
    global count
    count -= 1
    emit('count_client', {'count': count}, broadcast=True)

@socketio.on('client_to_server')
def handle_client_request(data):
    #print(requests.sid)
    socketio.emit('server_to_client', {'username':data['username'], 'text': data['text']}, broadcast=True)

socketio.run(app, debug=True)