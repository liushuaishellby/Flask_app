import time

from . import api
from flask import request, render_template, jsonify, redirect, url_for
from ..ext.sql_app import GetSql
from ..ext.check import CheckInfo
from ..models import EmailCaptchaModel
from werkzeug.security import generate_password_hash


@api.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        try:
            # 判断是否为空请求
            if not request.form.to_dict():
                return jsonify({"code": 404, "msg": "请填写参数"})
            # 获取请求的参数
            data = request.form.to_dict()
            print(data)
            # 校验表单提交的数据
            resp = CheckInfo().check_user_info(**data)
            if 'code' in resp:
                return jsonify(resp)
            else:
                data = resp
            # 从数据库查询此是否已有username的信息
            us_info = GetSql().query_sql(data['username'])
            if not us_info:  # 如果us_info为空 那么就可以继续注册
                # 将参数插入数据库
                d = {
                    "code": 200,
                    "info": data,
                    "msg": "success",
                    "token": data['username'] + str(time.time())
                }
                # 将数据添加到数据库
                GetSql().add_sql(u=data['username'], pwd=generate_password_hash(data['password']), token=d['token'],
                                 sex="女", nickname=data['nickname'])
                return redirect(url_for("api.login"), code=200)
            else:
                return jsonify({"code": "400", "msg": "用户名已存在"})

        except KeyError as e:
            print(e)
            return (f"未填写{e}参数")
