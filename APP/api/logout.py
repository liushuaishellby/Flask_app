import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for, session
from ..ext.sql_app import GetSql
from ..ext.forms import LoginForm
from werkzeug.security import check_password_hash


@api.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('api.login'))
