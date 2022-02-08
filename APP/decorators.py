from flask import g, redirect, url_for
from functools import wraps


def login_required(func):
    """限制用户必须登录才可以访问"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('api.login'))

    return wrapper
