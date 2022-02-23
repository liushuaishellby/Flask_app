import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for, session

from ..ext.Token import create_token
from ..ext.get_qiniu_token import get_qiniu_token
from ..ext.sql_app import GetSql
from ..ext.forms import LoginForm
from werkzeug.security import check_password_hash
from ..ext.Token import login_required
from ..ext.make_res import make_res


@api.route('/avatar/get_token', methods=['POST'])
@login_required
def get_avatar_token():
    try:
        if request.method == 'POST':
            if not request.get_json():
                res = make_res(4000)
                return res
            # 调用token函数
            key = request.get_json()['key']
            print(key)
            token = get_qiniu_token(file_key=key)
            data = {
                "token": token
            }
            res = make_res(200, data)
            return res
        else:
            # 不合法的请求
            res = make_res(5005)
            return res

    except Exception:
        # 返回请求异常
        res = make_res(5000)
        return res
