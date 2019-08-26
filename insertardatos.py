from main import app, db, User, Post, Tag, migrate

def insertar(numero):
    print("va a isertar el dato")
    user4 = User(username='fake_name'+str(numero))
    db.session.add(user4)

    try:

        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()  # optional, depends on use case

