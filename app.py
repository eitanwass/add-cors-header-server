from flask import Flask

app = Flask(__name__)


@app.route('/stats/')
def access_amount():
    return '0'


if __name__ == '__main__':
    app.run()
