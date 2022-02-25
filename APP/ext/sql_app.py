from APP.models import UserInfo
from APP import db


class GetSql:
    """"数据库的操作"""

    # 删
    # 改
    # 查
    def query_sql(self, u):
        user = UserInfo.query.filter(UserInfo.username == u).first()
        return user

    # 增
    def add_sql(self, u, pwd, nickname, age=19,
                avatar_url='http://r7nj4y6e5.bkt.clouddn.com/src%3Dhttp___zhaopin-rd5-pub.oss-cn-beijing.aliyuncs.com_imgs_staff_b2a446ab1ad5d1fe7f9fe11f82a3538b.jpg_x-oss-process%3Dimage_crop%2Cx_0%2Cy_0%2Cw_959%2Ch_959%26refer%3Dhttp___zhaopin-rd5-pub.oss-cn-beijing.aliyuncs.jpg'):
        u = UserInfo(username=u, password=pwd, age=age, nickname=nickname, avatar_url=avatar_url)
        db.session.add(u)
        db.session.commit()
        db.session.close()

    # 查询邮箱
    def query_email(self, username):
        user = UserInfo.query.filter_by(username == username).first()
        return user
