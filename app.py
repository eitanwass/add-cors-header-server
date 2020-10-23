from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/')
def test_cors():
    res = requests.get('https://apibay.org/q.php?q=test')
    return res.content


@app.route('/<path:addr>')
def create_request(addr):

    res = requests.get(request.full_path[1:])

    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.data = res.content

    return response


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run()
