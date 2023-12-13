from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('notifications.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('notification', {'message': 'Connected to the server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def notify_users():
    while True:
        time.sleep(5)
        socketio.emit('notification', {'message': 'New update! Check it out.'})

if __name__ == '__main__':
    socketio.start_background_task(notify_users)
    socketio.run(app, host='0.0.0.0')
