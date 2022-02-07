import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for
from ..ext.sql_app import GetSql


@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        try:
            if not request.get_json():
                return jsonify({"code": 409, "msg": "请填写参数"})
            form = LoginForm(request.form)
            print(form.validate())
            if form.validate():
                return jsonify({"code": 404, "msg": "账号长度超过限制"})
            data = request.get_json()  # 获取请求的信息数据\
            if type(data) == str:
                data = json.loads(data)
            us_info = GetSql().query_sql(data['username'])  # 从数据库查询此username的信息

            for i, key in data.items():  # 遍历字典的key不能为空
                if key == '':
                    return jsonify({"code": 404, "msg": i + "不能为空"})
            if not data['username'] or not data['password']:
                return jsonify({"code": 405, "msg": "缺少必填参数"})
            print(us_info)
            if not us_info:
                return jsonify({"code": 406, "msg": "账号不存在"})
            if data['username'] == us_info[1] and data['password'] == us_info[2]:

                data = {
                    "code": 200,
                    "info": {
                        "id": us_info[0],
                        "name": us_info[1],
                        "age": us_info[3],
                        "nickname": us_info[4]
                    },
                    "msg": "success"
                }
                return jsonify(data)
                # return redirect(url_for('/index'))
            else:
                return jsonify({"code": 404, "msg": "用户名或密码错误"})
        except KeyError as e:
            print(e)
            return jsonify({"code": 444, "msg": "缺少必填的参数"})
