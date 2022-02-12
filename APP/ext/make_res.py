from flask import make_response


def make_res(s_code, data=None):
    from APP.base.status_code import res_status
    res = res_status(s_code, data)
    resp = make_response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



