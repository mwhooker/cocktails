from cocktails.app import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)

class Portion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.Integer)
    unit_type = db.Column(db.Enum('grams', 'dashes', 'parts',
                        name='employee_types'))

    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    ingredient = db.relationship('Ingredient')

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Book',
        backref=db.backref('ingredients', lazy='dynamic'))


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serving_size = db.Column(db.Integer)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book',
        backref=db.backref('recipes', lazy='dynamic'))
