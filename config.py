"""配置信息"""


class ConfigClass(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "adsjkh*sjg**9"
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/my_databases"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
