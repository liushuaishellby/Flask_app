from . import api
from flask import request, render_template, g, redirect, url_for

from .. import db
from ..models import  QuestionModel
from ..decorators import login_required
from ..ext.forms import QuestionFrom


@api.route('/publish', methods=['GET', 'POST'])
@login_required
def publish():
    if request.method == 'GET':
        return render_template('publish.html')
    else:
        form = QuestionFrom(request.form)
        # 校验发布的文案字数是否符合要求
        if form.validate():
            title = form.title.data
            content = form.content.data
            # 将数据添加至数据库
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            # 给他一个提示
            return redirect(url_for('api/publish'))
