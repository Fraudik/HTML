from flask import Flask, render_template
from data import db_session
from data.jobs import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


@app.route("/")
def index():
    session = db_session.create_session()
    news = session.query(Job)
    return render_template("index.html", news=news)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

