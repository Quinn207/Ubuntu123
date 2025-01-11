from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' % name

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()