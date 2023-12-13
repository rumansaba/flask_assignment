from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('result.html', user_input=user_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
