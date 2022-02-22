from . import api
from flask import request

from ..ext.Token import verify_token, login_required
from ..ext.make_res import make_res
from ..models import UserInfo


@api.route('/get_userinfo', methods=['POST'])
@login_required
def get_userinfo():
    try:
        token = request.headers['XT-token']
        user_id = verify_token(token)
        user = UserInfo.query.get(user_id)
        data = {
                   "id": user.id,
                   "username": user.username,
                   "age": user.age,
                   "nickname": user.nickname,
                   "avatar_url": user.avatar_url
               },

        res = make_res(200, data)
        return res
    except Exception:
        res = make_res(5005)
        return res
