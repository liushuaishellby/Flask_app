import json

from . import api
from flask import request, jsonify

from ..ext.make_res import make_res
from ..ext.sql_app import GetSql
from ..ext.check import CheckInfo
from werkzeug.security import generate_password_hash


@api.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # 判断是否为空请求
            if request.headers.get('Content-Type') == 'application/json':
                if not request.get_json():
                    res = make_res(4000)
                    return res
                data = request.get_json()
                if type(data) == str:
                    data = json.loads(data)
                if not data['username'] or not data['password'] or not data['nickname'] or not data['email'] or not \
                data['captcha']:
                    res = make_res(4003)
                    return res
            else:
                if not request.form.to_dict():
                    res = make_res(4003)
                    return res
                data = request.form.to_dict()  # 获取请求的信息数据
            # 获取请求的参数
            # 校验表单提交的数据
            resp = CheckInfo().check_user_info(**data)
            if 'code' in resp:
                return jsonify(resp)
            else:
                data = resp
            # 从数据库查询此是否已有username的信息
            us_info = GetSql().query_sql(data['username'])
            if not us_info:  # 如果us_info为空 那么就可以继续注册
                # 将数据添加到数据库
                GetSql().add_sql(u=data['username'], pwd=generate_password_hash(data['password'])
                                 , nickname=data['nickname'])
                res = make_res(200)
                return res
            else:
                res = make_res(4104)
                return res

        except KeyError as e:
            res = make_res(4003)
            return res
    else:
        res = make_res(5005)
        return res
