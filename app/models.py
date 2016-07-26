from app import db

class Cameras(db.Model):
    pass

class Category(db.Model):
    pass

class CameraType(db.Model):
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

