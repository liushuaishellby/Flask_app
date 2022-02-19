import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for, session

from ..ext.Token import create_token
from ..ext.sql_app import GetSql
from ..ext.forms import LoginForm
from werkzeug.security import check_password_hash
from ..ext.make_res import make_res


@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        if request.headers.get('Content-Type') == 'application/json':
            if not request.get_json():
                res = make_res(4000)
                return res
            data = request.get_json()
            if type(data) == str:
                data = json.loads(data)
        else:
            if not request.form.to_dict():
                res = make_res(4003)
                return res
            data = request.form.to_dict()  # 获取请求的信息数据
        print(data)
        try:
            if not data['username'] or not data['password']:
                res = make_res(4003)
                return res
            us_info = GetSql().query_sql(data['username'])  # 从数据库查询此username的信息

            for i, key in data.items():
                # 遍历字典的key不能为空
                if key == '':
                    res = make_res(4000)
                    return res
            if not us_info:
                res = make_res(4004)
                return res
            if us_info and check_password_hash(us_info.password, data['password']):
                # 设置token信息
                token = create_token(us_info.id)

                data = {
                    "info": {
                        "id": us_info.id,
                        "username": us_info.username,
                        "age": us_info.age,
                        "nickname": us_info.nickname
                    },
                    "XT-token": token
                }
                res = make_res(200, data)
                return res
            else:
                res = make_res(4104)
                return res
        except KeyError as e:
            res = make_res(5000)
            return res
    else:
        res = make_res(5005)
        return res
