import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for, session
from ..ext.sql_app import GetSql
from ..ext.forms import LoginForm
from werkzeug.security import check_password_hash


@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            if not request.get_json():
                return jsonify({"code": 409, "msg": "请填写参数"})
            data = request.get_json()
            if type(data) == str:
                data = json.loads(data)
        else:
            if not request.form.to_dict():
                return jsonify({"code": 409, "msg": "请填写参数"})
            data = request.form.to_dict()  # 获取请求的信息数据
        try:
            us_info = GetSql().query_sql(data['username'])  # 从数据库查询此username的信息

            for i, key in data.items():  # 遍历字典的key不能为空
                if key == '':
                    return jsonify({"code": 404, "msg": i + "不能为空"})
            if not data['username'] or not data['password']:
                return jsonify({"code": 405, "msg": "缺少必填参数"})
            if not us_info:
                return jsonify({"code": 406, "msg": "账号不存在"})
            print(check_password_hash(us_info.password, data['password']))
            if us_info and check_password_hash(us_info.password, data['password']):
                # 保存session信息
                session['user_id'] = us_info.username
                data = {
                    "code": 200,
                    "info": {
                        "id": us_info.id,
                        "name": us_info.username,
                        "age": us_info.age,
                        "nickname": us_info.nickname
                    },
                    "msg": "success"
                }
                #  return jsonify(data)
                return redirect(url_for("api.community"))
            else:
                return jsonify({"code": 404, "msg": "用户名或密码错误"})
        except KeyError as e:
            print(e)
            return jsonify({"code": 444, "msg": "缺少必填的参数"})
