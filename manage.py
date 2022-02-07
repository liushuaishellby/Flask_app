from flask import render_template

from APP import create_app

app = create_app()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
