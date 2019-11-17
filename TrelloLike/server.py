from flask import Flask, render_template, request
from models.models import PostIt
from models.database import db_session
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    all_post_it = PostIt.query.all()
    return render_template('index.html', postits=all_post_it)

@app.route('/add', methods=['post'])
def add():
    title = request.form['title']
    content = PostIt(title, datetime.now())
    print(f'{title}のPOSTを確認')
    db_session.add(content)
    db_session.commit()
    return index()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)