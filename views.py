# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello world..!!"
#
from datetime import datetime
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    date = datetime.now().strftime('%Y-%m-%d')
    user = {'nickname':'Sourabh'}
    post = [
        {
            'author':{'nickname':'John'},
            'body':'beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Joe'},
            'body':'You need to watch Avenger Movie!'
        }
    ]
    return render_template('index.html',user=user,post=post,date=date)

if __name__ == "__main__":
    app.run()
