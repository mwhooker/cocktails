from database import db

def bstrap():
    db.create_all()
    from database import Book
    from database import Recipe
    book = Book()
    book.name = 'Allie\'s Amazin Cocktials'
    book.introduction = "Voluptate organic viral, thundercats twee mixtape tote bag selfies ethical art party church-key asymmetrical pork belly single-origin coffee irure. Ethnic ugh +1 synth, blog elit Portland single-origin coffee Etsy art party you probably haven't heard of them excepteur deep v aesthetic. Sustainable fashion axe ea shoreditch nulla sartorial. Gentrify DIY tofu Marfa. Kogi selfies thundercats messenger bag, Etsy hashtag enim disrupt occaecat. Aliquip Odd Future Cosby sweater before they sold out. Labore ad aliquip sustainable Portland laboris"
    book.dedication = 'matt'
    db.session.add(book)
    book2 = Book()
    book2.name = 'Sloth\'s drink list'
    book2.introduction = 'blah balh blah, this doesn\'t need to be unique?'
    book2.dedication = 'tree\'s everywhere'
    db.session.add(book2)
    db.session.commit()
    
    recipe = Recipe()
    recipe.name = "Jack Rose"
    recipe.notes = "tastes better shaken"
    recipe.book = book
    recipe.book_id = book.id
    db.session.add(recipe)
    recipe2 = Recipe()
    recipe2.name = "Sazerac"
    recipe2.notes = "extra bitters ftw"
    recipe2.book = book
    recipe2.book_id = book.id
    db.session.add(recipe2)
    recipe3 = Recipe()
    recipe3.name = "Tree Tea"
    recipe3.notes = "great for rainy days"
    recipe3.book = book2
    recipe3.book_id = book2.id
    db.session.add(recipe3)
    db.session.commit()


if __name__ == '__main__':
    bstrap()
