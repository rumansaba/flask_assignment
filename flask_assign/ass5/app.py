from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key for your application

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username} <br><a href="/logout">Logout</a>'
    return 'You are not logged in <br><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
