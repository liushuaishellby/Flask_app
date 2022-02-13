"""回复页面请求和存储"""

from flask import render_template, request, g, redirect, url_for, jsonify
from APP.api import api
from .. import db
from ..ext.Token import login_required, verify_token
from ..ext.make_res import make_res
from ..models import AnswerModel, UserInfo, QuestionModel
from ..ext.forms import AnswerForm


@api.route('/answer', methods=['POST', 'GET'])
@login_required
def answer():
    try:
        question_id = request.form.get('question_id')
        question = QuestionModel.query.get(question_id)
        answer_list = []
        for answer in question.answers:
            answer_info = {
                "answer_user": answer.author.username,
                "answer_content": answer.content,
                "answer_create_time": str(answer.create_time)}
            answer_list.append(answer_info)
        # data中保存了所有回复信息以及回复总数
        data = {"answer_total": len(question.answers), "answer_info": answer_list}
        if request.method == 'POST':
            form = AnswerForm(request.form)
            token = request.headers['XT-token']
            id = verify_token(token)
            user = UserInfo.query.get(id)
            if form.validate():
                content = form.content.data
                # 储存回复
                answer_model = AnswerModel(content=content, author=user, question_id=question_id)
                db.session.add(answer_model)
                db.session.commit()
                res = make_res(200,data)
                return res
        else:
            res = make_res(5005,data)
            return res
    except Exception:
        res = make_res(5006)
        return res
