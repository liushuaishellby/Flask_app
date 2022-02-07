from datetime import datetime

from APP import db


# 创建用户信息表
class UserInfo(db.Model):
    __tablename__ = "user_info"
    # 创建列 id 为主键
    id = db.Column(db.Integer, primary_key=True)
    # 账号为字符串，不能为空
    username = db.Column(db.String(16), nullable=False)
    # 账号为字符串，不能为空
    password = db.Column(db.String(16), nullable=False)
    # email = ""
    age = db.Column(db.String(16), nullable=False)
    # 性别只能使用男/女
    sex = db.Column(db.Enum("男", "女"), nullable=False)
    token = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(16))


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
