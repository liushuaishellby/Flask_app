from flask import render_template, session, g
from APP.ext.sql_app import GetSql
from APP import create_app
from APP.models import QuesitonModel

app = create_app()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            # 查询数据可user_id信息
            user = GetSql().query_sql(user_id)
            g.user = user
        except:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}

    else:
        return {}


@app.route('/index', methods=['POST', 'GET'])
def index111():
    print(123)
    questions = QuesitonModel.query.all()
    return render_template('index.html', questions=questions)


if __name__ == '__main__':
    app.run()
