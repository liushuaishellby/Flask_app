from enum import Enum

from flask import jsonify
from manage import app

app.app_context().push()


class StatusCodeEnum(Enum):
    """状态码枚举"""

    OK = (200, '成功')
    ERROR = (-1, '错误')
    SERVER_ERR = (500, '服务器异常')
    Bad_Request = (4000, '请填写正确的参数')
    TOKEN_LACK = (4000, '缺少参数token')
    TOKEN_ERROR = (4101, '登陆已过期')
    IMAGE_CODE_ERR = (4001, '验证码错误')
    THROTTLING_ERR = (4002, '访问过于频繁')
    NECESSARY_PARAM_ERR = (4003, '缺少必传参数')
    USER_ERR = (4004, '用户名错误')
    PWD_ERR = (4005, '密码错误')
    CPWD_ERR = (4006, '密码不一致')
    USER_OR_PWD_ERROR = (4104, '用户名或密码错误')
    MOBILE_ERR = (4007, '手机号错误')
    SMS_CODE_ERR = (4008, '短信验证码有误')
    SESSION_ERR = (4010, '用户未登录')

    DB_ERR = (5000, '数据错误')
    EMAIL_ERR = (5001, '邮箱错误')
    TEL_ERR = (5002, '固定电话错误')
    NODATA_ERR = (5003, '无数据')
    NEW_PWD_ERR = (5004, '新密码错误')
    OPENID_ERR = (5005, '请求不合法')
    PARAM_ERR = (5006, '参数错误')
    STOCK_ERR = (5007, '库存不足')
    USER_IS = (4104, '用户名已存在')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def errmsg(self):
        """获取状态码信息"""
        return self.value[1]


def res_status(s_code, data=None):
    """
    封装返回的数据及状态码
    :param s_code:
    :param data:
    :return: 数据及状态码
    """
    for i in StatusCodeEnum:
        if s_code in i.value:
            code = i.value[0]
            msg = i.value[1]
            if data:
                d = {"code": code, "msg": msg}
                d['data'] = data
            else:
                d = {"code": code, "msg": msg}
            return jsonify(d)
    return '没有此状态码'
