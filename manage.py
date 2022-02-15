from APP import create_app
from APP.models import QuestionModel, UserInfo

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
