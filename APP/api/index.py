from flask import Blueprint, render_template

# 创建蓝图对象
index = Blueprint("/", __name__)


@index.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
