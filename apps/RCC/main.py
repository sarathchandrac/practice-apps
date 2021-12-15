from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/one')
def one():
    numbers = ['one', 'two', 'three']
    return render_template('testone.html', name="sarath", numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)