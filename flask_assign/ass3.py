from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the dynamic content app!"
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! This is your personalized greeting."

if __name__ == '__main__':
    app.run(host='0.0.0.0')