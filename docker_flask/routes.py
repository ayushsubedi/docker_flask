
from flask import render_template
from docker_flask import application
from docker_flask import basic_auth
from docker_flask.helper import tweet_text
from docker_flask.models import TwitterClient


@application.route('/')
def index():
    return 'docker_flask'


@application.route('/basicauth')
@basic_auth.required
def basicauthtest():
    return 'it works'


@application.route('/apitest')
def apitest():
    return tweet_text()

