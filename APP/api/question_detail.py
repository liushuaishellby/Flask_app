"""问答详情页面"""

from flask import render_template, request

from APP.api import api
from APP.ext.make_res import make_res
from APP.models import QuestionModel, AnswerModel


@api.route('/question_detail', methods=['POST', 'GET'])
def question_detail():
    question_id = request.args.get('question_id')
    question = QuestionModel.query.get(question_id)
    data = {
        "username": question.author.username,
        "create_title": question.title,
        "time": question.create_time,
        "content": question.content,
    }
    res = make_res(200, data)
    return res
