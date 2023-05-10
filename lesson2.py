from flask import Flask, render_template

app = Flask(__name__)
# было
# @app.route('/')
# def index_v5():
#     return render_template('index_for_v5.html', title='Main')

#
@app.route('/')
def index_v6():
    return render_template('index_for_v6.html', title='Main')

# def do_it_yourself():
#     return render_template('index_for_v6.html', title='Main')



if __name__ == '__main__':
    app.run()