
from . import api
from flask import request

from .. import db
from ..ext.Token import  verify_token
from ..ext.Token import login_required
from ..ext.make_res import make_res
from ..models import UserInfo


@api.route('/avatar/update', methods=['POST'])
@login_required
def update_avatar():
    try:
        if request.method == 'POST':
            if not request.get_json():
                res = make_res(4000)
                return res
            avatar_url = request.get_json()['avatar_url']
            # 通过token获取id
            token = request.headers['XT-token']
            id = verify_token(token)
            user = UserInfo.query.get(id)
            # 通过id去修改avatar_url字段
            user.avatar_url = avatar_url
            db.session.commit()
            db.session.close()
            res = make_res(200)
            return res
        else:
            # 不合法的请求
            res = make_res(5005)
            return res

    except Exception:
        # 返回请求异常
        res = make_res(5000)
        return res

    # 最后返回一个200状态码
