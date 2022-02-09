from flask import render_template

from APP.api import api
from APP.decorators import login_required
from APP.models import QuestionModel


@api.route('/', methods=['POST', 'GET'])
@login_required
def index():
    print(123)
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    username = questions[0].author.username
    print(username)
    return render_template('index.html', questions=questions)
