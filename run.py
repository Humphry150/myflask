# coding:utf-8


from flask import Flask
from config import settings
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':

    app.run(host=settings.host, port=settings.port, debug=settings.debug)
