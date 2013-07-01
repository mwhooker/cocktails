from cocktails.web import db
from sqlalchemy.schema import UniqueConstraint


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1023), unique=True)
    introduction = db.Column(db.String(4095), unique=True)
    dedication = db.Column(db.String(4095), unique=True)


class Recipe(db.Model):
    __table_args__ = (
        UniqueConstraint('name', 'book_id'),
    )
    id = db.Column(db.Integer, primary_key=True)
    serving_size = db.Column(db.Integer, default=1)
    name = db.Column(db.String(1023))
    notes = db.Column(db.String(4095))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book',
        backref=db.backref('recipes', lazy='dynamic'))


class Portion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.Float(asdecimal=True))
    unit_type = db.Column(db.Enum('grams', 'dashes', 'parts',
                        name='employee_types'))

    stet_unit = db.Column(db.String(255))

    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    ingredient = db.relationship('Ingredient')

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Recipe',
        backref=db.backref('ingredients', lazy='dynamic'))


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

