from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import ConfigClass
from ..base.status_code import  res_status
from functools import wraps



def create_token(api_user):
    """
    生成token
    :param api_user: 用户id
    :return: token
    """

    # 第一步设置参数内部的私钥，这里这里写在共用的配置信息，如果是测试可以写死
    # 第二部 参数是有效期（秒）

    s = Serializer(secret_key=ConfigClass.SECRET_KEY, expires_in=3600)

    # 接受用户的id转换与编码
    token = s.dumps({"id": api_user}).decode('ascii')
    return token


def verify_token(token):
    """
    校验token
    :param token:
    :return: 用户信息 or None
    """

    # 参数为私钥，跟create_token的私钥保持一致
    s = Serializer(secret_key=[ConfigClass.SECRET_KEY])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转后的数据，根据模型类去数据库查询用户的信息
    # user = UserInfo.query.get(data['id'])
    return data['id']


def login_required(func):
    """
    装饰器 验证请求是必须带有token 判断用户是否登陆
    :param func:
    :return: func
    """

    @wraps(func)
    def verification_token(*args, **kwargs):
        try:
            print('进来')
            # 在请求头拿到token
            token = request.headers['XT-token']
        except Exception:
            # 没有接收到token，给前端一个错误
            # 这里的code写一个文件统一管理。后期再来做
            return jsonify({"code": 4000, "msg": '缺少参数token '})
        s = Serializer(secret_key=ConfigClass.SECRET_KEY)
        try:
            s.loads(token)
        except Exception:
            resp = res_status(4101)
            return resp

        return func(*args, **kwargs)

    return verification_token
