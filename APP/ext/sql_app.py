from APP.models import UserInfo
from APP import db


class GetSql:
    """"数据库的操作"""

    # 删
    # 改
    # 查
    def query_sql(self, u):
        user = UserInfo.query.filter(UserInfo.username == u)
        for i in user:
            return [i.id, i.username, i.password, i.age, i.nickname]

    # 增
    def add_sql(self, u, pwd, sex, token, nickname, age=None):
        u = UserInfo(username=u, password=pwd, age=age, sex=sex, token=token, nickname=nickname)
        db.session.add(u)
        db.session.commit()
        db.session.close()
