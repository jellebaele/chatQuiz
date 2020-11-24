import os

from flask import Flask, render_template, url_for, request, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room

from form_fields import LoginForm
from models import *

app = Flask(__name__)
app.secret_key = 'CHANGE LATER'

# Config database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://exvngnyhhlrrpl:454d5ec7c5e1bee24801a9ab4c54c3ee0545a3b0b18bb6efd7b3f4237ac' \
                                 'd325b@ec2-52-5-176-53.compute-1.amazonaws.com:5432/d5kjmua3rlrpq3'
db = SQLAlchemy(app)

socketio = SocketIO(app)
ROOMS = ["home"]


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == 'POST' and login_form.validate_on_submit():
        user = User(username=login_form.username.data, avatar=login_form.avatar.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    imgs = os.listdir("static/images")
    for i in range(len(imgs)):
        imgs[i] = url_for('static', filename='images/' + imgs[i])

    return render_template('login.html', form=login_form, images=imgs)


@app.route('/home')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)
