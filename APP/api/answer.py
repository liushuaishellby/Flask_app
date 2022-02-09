"""回复页面请求和存储"""

from flask import render_template, request, g, redirect, url_for, jsonify
from APP.api import api
from .. import db
from ..decorators import login_required
from ..models import AnswerModel
from ..ext.forms import AnswerForm


@api.route('/answer/<int:question_id>', methods=['POST'])
@login_required
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        # 储存回复
        answer_model = AnswerModel(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for("api.question_detail", question_id=question_id))
    else:
        return redirect(url_for("api.question_detail", question_id=question_id))
