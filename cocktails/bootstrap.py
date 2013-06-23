from database import db

def bstrap():
    db.create_all()


if __name__ == '__main__':
    bstrap()
