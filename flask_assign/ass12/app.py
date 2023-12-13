from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('realtime_data.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('notification', {'message': 'Connected to the server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def update_data():
    count = 0
    while True:
        time.sleep(2)
        count += 1
        socketio.emit('update_data', {'count': count})

if __name__ == '__main__':
    socketio.start_background_task(update_data)
    socketio.run(app, host='0.0.0.0')
