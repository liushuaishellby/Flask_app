import json
from . import api
from flask import request, render_template, jsonify, redirect, url_for

from ..decorators import login_required
from ..ext.sql_app import GetSql
from ..ext.forms import LoginForm
from werkzeug.security import check_password_hash


@api.route('/community', methods=['GET', 'POST'])
@login_required
def community():
    return render_template('community.html')
