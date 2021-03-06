import wtforms
from wtforms.validators import length, email
from ..models import EmailCaptchaModel


class RegisterForm(wtforms.Form):
    """
    校验登录的用户名是长度是否符合要求
    """
    username = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=8, max=20)])
    email = wtforms.StringField(validators=[email()])

    def validate_captcha(self, field):
        """校验验证码是否正确"""
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.capycha.lower() != captcha.lower():
            raise wtforms.ValidationError("邮箱验证码错误")

    def validate_email(self, field):
        email = field.data
        user_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError("邮箱已存在")


class LoginForm(wtforms.Form):
    """
    校验登录的用户名是长度是否符合要求
    """
    username = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=8, max=20)])


class QuestionFrom(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=20)])
    content = wtforms.StringField(validators=[length(min=5)])


class AnswerForm(wtforms.Form):
    """
    校验回复的内容
    """
    content = wtforms.StringField(validators=[length(min=1)])
