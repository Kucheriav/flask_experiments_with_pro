from flask import Flask, render_template
import sqlite3

def get_db_connection(filename):
    curr = sqlite3.connect(filename)
    curr.row_factory = sqlite3.Row
    return curr


app = Flask(__name__)
# было
# @app.route('/')
# def index_v5():
#     return render_template('index_for_v5.html', title='Main')

#
# @app.route('/')
# def index_v6():
#     return render_template('index_for_v6.html', title='Main')


# самостоятельно создать ссылку с главной на новую страницу с краткой информацией об авторах
# и создать обработчик маршрута
@app.route('/creators')
def do_it_yourself():
    return render_template('creators.html', title='Creators')

@app.route('/')
def index_v7():
    cursor = get_db_connection('db/info.db')
    users = cursor.execute('SELECT * FROM Users').fetchall()
    cursor.close()
    return render_template('index_for_v7.html', title='Main', users=users)

@app.route('/user/<i>')
def user(i):
    cursor = get_db_connection('db/info.db')
    user = cursor.execute(f'SELECT * FROM Users WHERE id == {i}').fetchone()
    cursor.close()
    return render_template('user.html', title='Userpage', user=user)

if __name__ == '__main__':
    app.run()