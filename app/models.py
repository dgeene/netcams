from app import db
# this schema needs to be verified
# are bridge tables being created?
# http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html#many-to-many
#

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), index=True)

    def __repr__(self):
        return '<Category %r>' % (self.category_name)

class CameraType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32), index=True)

    def __repr__(self):
        return '<Type %r>' % (self.type)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Cameras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(255), index=True)
    url = db.Column(db.String(255))
    type = db.relationship('CameraType', backref='camera_type', lazy='dynamic')
    categories = db.relationship('Category', backref='camera_categories', lazy='dynamic')
    city = db.Column(db.String(64), index=True)
    country = db.Column(db.String(64), index=True)
    latitude_n = db.Column(db.Numeric(precision=10, scale=8))
    latitude_e = db.Column(db.Numeric(precision=10, scale=8))
    coords_verified = db.Column(db.Integer)
    comment = db.Column(db.String(255))

    def __repr__(self):
        return '<CameraName %r>' % (self.camera_name)

