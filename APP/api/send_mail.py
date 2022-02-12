import string
import random
from datetime import datetime

from . import api
from flask_mail import Message
from flask import request, jsonify
from ..models import EmailCaptchaModel

from .. import db
from ..ext.send_mail import mail
from ..ext.check import CheckInfo


@api.route('/email', methods=['POST'])
def my_mail():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        email = data['email']
    else:
        email = request.form.get('email')
    # 生成验证码
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    # 验证邮箱格式
    check_email = CheckInfo().check_email(email)
    if not check_email:
        return jsonify({"code": 404, "msg": "邮箱格式错误"})
    captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
    if not captcha_model:
        message = Message(
            subject="测试课堂注册",
            recipients=['3521346025@qq.com'],
            body=f"【测试小课堂】您的验证码是：{captcha}。请不要告诉任何人哦"
        )
        mail.send(message)
        # 判断是否有captcha
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
            print(captcha)

        else:
            """向数据库添加验证码"""
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
            print("captcha", captcha)
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 404, "msg": "邮箱已存在"})
