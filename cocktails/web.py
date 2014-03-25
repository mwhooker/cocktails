from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template
from werkzeug.routing import Map, Rule, RuleTemplate
db = SQLAlchemy(app)

@app.route("/bootstrap")
def bootstrapf():
    import bootstrap
    bootstrap.bstrap()
    return "done"

@app.route("/")
def hello():
    from database import Book
    return str(Book.query.all())
    
@app.route("/books")
def books():
    from database import Book
    allbooks = Book.query.all()
    return render_template('books.html', books=allbooks)
    
@app.route("/book/<bookid>")
def book(bookid):
    from database import Book
    from database import Recipe

    mybook = Book.query.filter_by(id=bookid).first()
    recipelist = Recipe.query.filter_by(book_id=bookid).all()
    
    return render_template('book.html', book=mybook, recipies=recipelist)

if __name__ == "__main__":
    app.run()
