from flask import Flask, jsonify, g

import models

DEBUG = True
PORT = 8001

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)


@app.before_request
def before_request():
    "Connect to the database before each request."
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    'Close the database connection after each request.'
    g.db.close()
    return response

# The default URL ends in / ("my-website.com/").


@app.route('/')
def index():
    return 'hi'


# @app.route('/sayhi/<username>')  # When someone goes here...
# def hello(username):  # Do this.
#     return "Hello {}".format(username)


# @app.route('/json')
# def song():
#     return jsonify(title="Frankie", artist="Lionel")


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
