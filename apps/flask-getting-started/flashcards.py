from datetime import datetime
from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("Welcome.html", message1="This is a greeting")


@app.route('/date')
def date():
    return "This page was served at - " + str(datetime.now())


counter = 0


@app.route('/count')
def count():
    global counter
    counter += 1
    return "Counter - " + str(counter)


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index = len(db) -1)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run()