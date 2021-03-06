from app import db
# continue verifying the schema
# http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html#many-to-many
# TODO sqlite doesnt support decimals. Use a string?

# address the many to many with a bridge table
camera_categories = db.Table('camera_categories', db.Model.metadata,
    db.Column('camera_id', db.Integer, db.ForeignKey('camera.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), index=True)

    def __repr__(self):
        return '<Category %r>' % (self.category_name)


class CameraType(db.Model):
    __tablename__ = 'camera_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32), index=True)

    def __repr__(self):
        return '<Type %r>' % (self.type)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Camera(db.Model):
    __tablename__ = 'camera'
    id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(255), index=True)
    url = db.Column(db.String(255))
    type_id = db.Column(db.Integer, db.ForeignKey('camera_type.id'))
    type = db.relationship('CameraType', backref='camera_type')
    categories = db.relationship('Category', secondary=camera_categories, backref='camera_categories', lazy='dynamic')
    city = db.Column(db.String(64), index=True)
    country = db.Column(db.String(64), index=True)
    latitude_n = db.Column(db.Numeric(precision=10, scale=8))
    latitude_e = db.Column(db.Numeric(precision=10, scale=8))
    coords_verified = db.Column(db.Integer)
    comment = db.Column(db.String(255))

    def __repr__(self):
        return '<CameraName %r>' % (self.camera_name)

