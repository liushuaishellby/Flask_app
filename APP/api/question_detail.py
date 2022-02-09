"""问答详情页面"""

from flask import render_template

from APP.api import api
from APP.decorators import login_required
from APP.models import QuestionModel, AnswerModel


@api.route('/question_detail/<int:question_id>', methods=['POST', 'GET'])
@login_required
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)
    return render_template('question_detail.html', question=question)
