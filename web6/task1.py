from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизации Марса"


@app.route('/index')
def index():
    return "И на марсе будут яблоки цвести"

@app.route('/promotion')
def promotion():
    return '''<p>Человечество вырастает из детства.</p>
              <p>Человечеству мала одна планета.</p>
            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p>И начнем с Марса!</p>
            <p>Присоединяйся!</p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
