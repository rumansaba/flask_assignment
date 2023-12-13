from flask import Flask, render_template

app = Flask(__name__)

# Route for handling 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Route for handling 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Sample route for testing
@app.route('/')
def index():
    # Uncomment the line below to simulate a 500 internal server error
    # 1 / 0
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
