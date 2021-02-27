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


@app.route('/image_mars')
def image_mars():
    return '''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="static/image/Mars.png" alt="Картинка Марса">
    <figcaption>Вот она какая, красная планета.</figcaption>
</body>
</html>'''


@app.route('/promotion_image')
def promotion_img():
    return '''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/style.css">
    <style>
        h1 {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="static/image/Mars.png" alt="Картинка Марса">
    <p class="alert-secondary">Человечество вырастает из детства.</p>
    <p class="alert-success">Человечеству мала одна планета.</p>
    <p class="alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="alert-warning">И начнем с Марса!</p>
    <p class="alert-danger">Присоединяйся!</p>
</body>
</html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    distance = 'error'
    resources = 'error'
    if planet_name == 'Венера' or planet_name == 'Марс':
        distance = 'Эта планета близка к земле'
        resources = 'На этой планете много ресурсов'
    elif planet_name == 'Юпитер' or planet_name == 'Меркурий':
        distance = 'Эта планета находится на среднем расстоянии от земли'
        resources = 'На этой планете мало ресурсов'
    elif planet_name == 'Сатурн' or planet_name == 'Уран' or planet_name == 'Нептун':
        distance = 'Эта планета далеко к земле'
        resources = 'На этой планете среднее количество ресурсов'
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
</head>
<body>
    <h1>Мое предложение: {planet_name}</h1>
    <p>{distance}</p>
    <p class="alert-success">{resources}</p>
    <p class="alert-secondary">На этой планете отсутствуют вода и атмосфера</p>
    <p class="alert-warning">На ней небольшое магнитное поле;</p>
    <p class="alert-danger">Наконец, она просто красива!</p>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
