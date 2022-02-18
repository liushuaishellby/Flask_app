from flask import render_template, jsonify

from APP.api import api
from APP.ext.make_res import make_res
from APP.models import QuestionModel, UserInfo


@api.route('/community', methods=['POST', 'GET'])
def community():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    data = []
    for question in questions:
        info = {
            "title": question.title, "content": question.content,
            "username": UserInfo.query.get(question.id).username,
            "create_time": str(question.create_time),
            "question_id": question.id,
            "answer_total": len(question.answers)}
        data.append(info)
    res = make_res(200, data)
    return res
