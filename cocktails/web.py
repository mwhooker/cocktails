from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
from flask.ext.sqlalchemy import SQLAlchemy
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

if __name__ == "__main__":
    app.run()
