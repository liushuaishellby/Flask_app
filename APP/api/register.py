import time

from . import api
from flask import request, render_template, jsonify

from ..ext.sql_app import GetSql


@api.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        try:
            if not request.get_json():
                return jsonify({"code": "444", "msg": "请填写参数"})
            data = request.get_json()  # 获取请求的参数
            if not data['username'] or not data['password'] or not data['nickname'] or not data['age']:
                return jsonify({"code": "404", "msg": "缺少必填参数"})
            for i, key in data.items():  # 遍历字典的key不能为空
                if key == '':
                    return jsonify({"msg": i + "不能为空"})
            us_info = GetSql().query_sql(data['username'])  # 从数据库查询此是否已有username的信息

            if not us_info:  # 如果us_info为空 那么就可以继续注册
                # 将参数插入数据库
                d = {
                    "code": "200",
                    "info": data,
                    "msg": "success",
                    "token": data['username'] + str(time.time())
                }
                # 将数据添加到数据库
                GetSql().add_sql(u=data['username'], pwd=data['password'], token=d['token'],
                                 sex="女", nickname=data['nickname'], age=data['age'])
                return jsonify(d)
            else:
                return jsonify({"code": "400", "msg": "用户名已存在"})

        except KeyError as e:
            print(e)
            return jsonify({"code": "444", "msg": "缺少必填参数{}".format(e)})
