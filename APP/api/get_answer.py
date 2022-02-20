"""回复页面请求和存储"""
import json

from flask import render_template, request, g, redirect, url_for, jsonify
from APP.api import api
from .. import db
from ..ext.Token import login_required, verify_token
from ..ext.make_res import make_res
from ..models import AnswerModel, UserInfo, QuestionModel
from ..ext.forms import AnswerForm


@api.route('/get_answer', methods=['POST', 'GET'])
# @login_required
def get_answer():
    try:
        if request.method == 'POST':
            if request.headers.get('Content-Type') == 'application/json':
                if not request.get_json():
                    res = make_res(4000)
                    return res
                data = request.get_json()
                print(data)
                if type(data) == str:
                    data = json.loads(data)
                question_id = data['question_id']
            else:
                if not request.form.to_dict():
                    res = make_res(4003)
                    return res
                question_id = request.form.get('question_id')
        else:
            question_id = request.args.get('question_id')
        question = QuestionModel.query.get(question_id)
        answer_list = []
        if not question.answers:
            res = make_res(5003)
            return res
        for answer in question.answers:
            answer_info = {
                "answer_id": answer.id,
                "answer_username": answer.author.username,
                "answer_content": answer.content,
                "answer_create_time": str(answer.create_time),
                "answer_nickname": answer.author.nickname}
            answer_list.append(answer_info)
        # data中保存了所有回复信息以及回复总数
        data = {"answer_total": len(question.answers), "answer_info": answer_list}
        res = make_res(200, data)
        return res
    except Exception:
        res = make_res(5003)
        return res
