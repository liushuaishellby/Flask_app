"""问答详情页面"""

from flask import render_template, request

from APP.api import api
from APP.ext.Token import login_required
from APP.ext.make_res import make_res
from APP.models import QuestionModel, AnswerModel


@api.route('/question_detail', methods=['POST'])
@login_required
def question_detail():
    try:
        if request.method == 'POST':
            r_data = request.get_json()
            question_id = r_data['question_id']
            question = QuestionModel.query.get(question_id)
            data = {
                "username": question.author.username,
                "create_title": question.title,
                "time": question.create_time,
                "content": question.content,
            }
            res = make_res(200, data)
            return res
        else:
            res = make_res(5005)
            return res
    except Exception:
        res = make_res(5006)
        return res
