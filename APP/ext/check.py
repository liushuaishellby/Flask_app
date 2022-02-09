import re
from flask import jsonify

from APP.models import EmailCaptchaModel


def split_s(**data):
    new_data = {}
    for d in data:
        if d == 'email':
            new_data[d] = data[d]
        if d == "nickname" or d == "username":
            continue
        new_data[d] = "".join(data[d].split())
    new_data["nickname"] = data["nickname"]
    new_data["username"] = data["username"]
    return new_data


class CheckInfo(object):
    def check_username(self, username):
        # 字母开头，允许6-12字节，允许字母数字下划线
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{6,15}$'
        result = re.search(pattern, username)
        return result

    def check_email(self, email):
        pattern_email = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
        result = re.search(pattern_email, email)
        return result

    def check_pwd(self, pwd):
        # 必须包含大小写字母和数字的组合，可以使用特殊字符，长度在8-16之间
        pattern_pwd = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$'
        result = re.search(pattern_pwd, pwd)
        return result

    def check_nickname(self, nickname):
        pattern_nickname = r'[a-z0-9[^a-za-z0-9_\n\t]]*'
        result = re.search(pattern_nickname, nickname)
        return result

    def check_user_info(self, **data):
        data = split_s(**data)
        username = self.check_username(data['username'])
        pwd = self.check_pwd(data['password'])
        nickname = self.check_nickname(data['nickname'])
        if not username:
            return ({"code": "404", "msg": "username格式错误"})
        if not pwd:
            return ({"code": "404", "msg": "password格式错误", "pwd": (data['password'])})
        if not nickname:
            return ({"code": "404", "msg": "nickname格式错误"})
        # 校验验证码是否正确
        email = data['email']
        user_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if data['captcha'] != user_model.captcha:
            return ({"code": "404", "msg": "验证码不正确"})

        return data

    # data = {"username": "hahahah", "password": "sd11111vssdsV", "email": "23234@   23qwe.commmmm", "nickname": "m哈哈哈"}
# s = CheckInfo().check_user_info(**data)
# print(s)
# u = CheckInfo().check_username('ha    h    ahah')
# print(u)
# nickname = '哈哈前哈'
# usr = check_nickname(nickname)
# if not usr:
#     print("格式不正确")
# else:
#     print(usr)
#     print("success")
