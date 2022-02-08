from flask import Flask
from config import ConfigClass
from flask_sqlalchemy import SQLAlchemy

# 先实例化db
db = SQLAlchemy()


# 工厂模式
def create_app():
    app = Flask(__name__)
    # app配置config信息
    app.config.from_object(ConfigClass)
    # 使用app初始化db
    db.init_app(app)
    from .ext.send_mail import mail
    mail.init_app(app)
    from APP import api
    # 注册蓝图
    app.register_blueprint(api.api, url_prefix="/api")
    return app
