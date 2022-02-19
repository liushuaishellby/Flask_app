"""回复页面请求和存储"""
import json

from flask import render_template, request, g, redirect, url_for, jsonify
from APP.api import api
from .. import db
from ..ext.Token import login_required, verify_token
from ..ext.make_res import make_res
from ..models import AnswerModel, UserInfo, QuestionModel
from ..ext.forms import AnswerForm


@api.route('/push_answer', methods=['POST', 'GET'])
@login_required
def push_answer():
    try:
        if request.method == 'POST':
            if request.headers.get('Content-Type') == 'application/json':
                if not request.get_json():
                    res = make_res(4000)
                    return res
                answer_data = request.get_json()
                if type(answer_data) == str:
                    data = json.loads(answer_data)

                question_id = answer_data['question_id']
                content = answer_data['content']
            else:
                form = AnswerForm(request.form)
                if form.validate():
                    content = form.content.data
                    question_id = form.question_id.data
                else:
                    res = make_res(5006)
                    return res
                    # 储存回复
            token = request.headers['XT-token']
            id = verify_token(token)
            user = UserInfo.query.get(id)
            answer_model = AnswerModel(content=content, author=user, question_id=question_id)
            db.session.add(answer_model)
            db.session.commit()
            db.session.close()
            question = QuestionModel.query.get(question_id)

            answer_list = []
            for answer in question.answers:
                if not answer:
                    res = make_res(5003)
                    return res
                answer_info = {
                    "answer_user": answer.author.username,
                    "answer_content": answer.content,
                    "answer_create_time": str(answer.create_time)}
                answer_list.append(answer_info)
                # data中保存了所有回复信息以及回复总数
            data = {"answer_total": len(question.answers), "answer_info": answer_list}
            res = make_res(200, data)
            return res
        else:
            res = make_res(5005)
            return res
    except Exception as e:
        raise e
