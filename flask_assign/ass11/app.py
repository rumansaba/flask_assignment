from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('chat_app_full.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@socketio.on('message')
def handle_message(data):
    emit('message', {'username': session['username'], 'message': data['message']}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    if 'username' not in session:
        return False

    emit('message', {'username': 'System', 'message': f'{session["username"]} has joined.'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    if 'username' in session:
        emit('message', {'username': 'System', 'message': f'{session["username"]} has left.'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
