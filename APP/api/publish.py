import json

from . import api
from flask import request
from .. import db
from ..ext.Token import login_required, verify_token
from ..ext.make_res import make_res
from ..ext.sql_app import GetSql
from ..models import QuestionModel, UserInfo
from ..ext.forms import QuestionFrom

"""
发布问答接口
"""


@api.route('/publish', methods=['GET', 'POST'])
@login_required
def publish():
    """
    需要参数：title、content
    """
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            if not request.get_json():
                res = make_res(4000)
                return res
            data = request.get_json()
            if type(data) == str:
                data = json.loads(data)
            print(data)
            title = data['title']
            content = data['content']
        else:
            form = QuestionFrom(request.form)
            # 校验发布的文案字数是否符合要求
            if form.validate():
                title = form.title.data
                content = form.content.data
            else:
                res = make_res(5006)
                return res
        # 解密token 或者名户名
        token = request.headers['XT-token']
        id = verify_token(token)

        user = UserInfo.query.get(id)
        print(user)
        print(user.username)
        # 将数据添加至数据库
        question = QuestionModel(title=title, content=content, author=user)
        db.session.add(question)
        db.session.commit()
        res = make_res(200)
        return res
    else:
        res = make_res(5000)
        return res
