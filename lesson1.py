# работаем с базовой маршрутизацией, рендером, шаблонами, настраиваем нав-панель
# файлы base/index_for_v4/5 styles.css

from flask import Flask

app = Flask(__name__)

# выводим текст
# @app.route('/')
# def index_v1():
#     return 'Моя первая соцсеть'

# выводим html-текст
# @app.route('/')
# def index_v2():
#     return '''<html>
#                 <head>
#                     <title>Social Network</title>
#                 </head>
#                 <body>
#                     <h1>Main page</h1>
#                 </body>
#             </html>'''

# рендерим html-файл
# from flask import render_template
# @app.route('/')
# def index_v3():
#     return render_template('index_for_v3.html')

# рендерим html-файл с наследованием из base (копипаста нав-панели)
# from flask import render_template
# @app.route('/')
# def index_v4():
#     return render_template('index_for_v4.html', title='Main')

# рендерим html-файл с наследованием из base (отредаченная нав-панель: в тегах
# ссылки поменяны классы на кнопочные (обязательно покурить доки кнопок)
# выкинуто лишнее непонятное)
from flask import render_template
@app.route('/')
def index_v5():
    return render_template('index_for_v5.html', title='Main')

if __name__ == '__main__':
    app.run()