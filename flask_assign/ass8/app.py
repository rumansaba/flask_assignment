from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Mock User class for demonstration purposes
class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

# Replace this with your actual user loading mechanism
@login_manager.user_loader
def load_user(user_id):
    # Replace with your user retrieval logic (e.g., querying a database)
    users = {
        '1': User('1', 'user1', 'password1'),
        '2': User('2', 'user2', 'password2')
    }
    return users.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Replace with your actual authentication logic
        user = next((u for u in load_users().values() if u.username == username and u.password == password), None)

        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Replace with your actual registration logic
        # For simplicity, this example uses a mock user with a hardcoded ID
        user_id = str(len(load_users()) + 1)
        user = User(user_id, username, password)
        users = load_users()
        users[user_id] = user

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def load_users():
    # Replace with your user retrieval logic (e.g., querying a database)
    return {
        '1': User('1', 'user1', 'password1'),
        '2': User('2', 'user2', 'password2')
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0')
