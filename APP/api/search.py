from . import api
from flask import request, jsonify, make_response, render_template

from .. import db
from sqlalchemy import or_

from ..ext.make_res import make_res
from ..models import QuestionModel


@api.route("/search", methods=["GET"])
# @login_requird
def search():
    if request.method == 'GET':
        q = request.args.get('q')
        # 知道符合条件的帖子
        questions = QuestionModel.query.filter(
            or_(QuestionModel.title.contains(q), (QuestionModel.content.contains(q)))).order_by(
            db.text('-create_time'))
        data = []
        for question in questions:
            info = {
                "title": question.title, "content": question.content,
                "username": question.author.username,
                "create_time": str(question.create_time),
                "question_id": question.id}
            data.append(info)
        res = make_res(200, data)
        return res
    else:
        res = make_res(5005)
        return res
