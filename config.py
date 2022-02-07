"""配置信息"""


class ConfigClass(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "adsjkh*sjg**9"
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@124.222.112.42:3306/user"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = "465"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = "3521346025@qq.com"
    MAIL_PASSWORD = "nnsttfljpqzmchcg"
    MAIL_DEFAULT_SENDER = "3521346025@qq.com"
