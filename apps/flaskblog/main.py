from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Prasad Honrao',
        'title': 'First post',
        'content': 'This is the first post',
        'date_posted': '12-NOV-2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second post',
        'content': 'This is the second post',
        'date_posted': '12-NOV-2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
