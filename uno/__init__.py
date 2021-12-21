from flask import (
    Flask, render_template, request, redirect, url_for
)

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        # number = request.form['number']
        mode = request.form['mode']
        swap = 'swap' in request.form
        force = 'force' in request.form
        print("=======================================+++++++++++++========================")
        # print(number)
        print(mode)
        print(swap)
        print(force)
        print("=======================================+++++++++++++========================")
        return redirect(url_for("game", mode=mode))
    return render_template("index.html")

@app.route('/<mode>', methods=('GET', 'POST'))
def game(mode=None):
    if request.method == 'POST':
        if request.form['button'] == 'Next':
            next()
        elif request.form['button'] == 'End Helper':
            end()
        # button = request.form['name']
        # if button == "next":
        #     print('POST for next')
        #     pass
        # elif button == "end":
        #     print('POST for end')
        #     pass
        # return "hello world"
    return render_template('game.html', mode=mode)

def next():
    print('Next')

def end():
    print('End helper')

# @app.route('/game')


# import os

# from flask import Flask

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'uno.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app