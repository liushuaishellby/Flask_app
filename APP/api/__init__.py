from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api", __name__)

from . import community, question_detail, answer, send_mail, login, logout, publish, \
    community, register, search,get_answer
