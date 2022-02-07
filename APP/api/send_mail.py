import string
import random
from datetime import datetime

from . import api
from flask_mail import Message
from flask import request
from ..models import EmailCaptchaModel

from .. import db
from ..ext.send_mail import mail
from ..ext.sql_app import GetSql


@api.route('/mail')
def my_mail():
    email = request.args.get('email')
    # 生成验证码
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    if email:
        message = Message(
            subject="测试课堂注册",
            recipients=['3521346025@qq.com'],
            body=f"【测试小课堂】您的验证码是：{captcha}。请不要告诉任何人哦"
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        # 判断是否有captcha
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()

        else:
            """向数据库添加验证码"""
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
            print("captcha", captcha)
        return "success"
    else:
        return "无效邮箱"
