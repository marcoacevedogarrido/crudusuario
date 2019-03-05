from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    apellido = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.nombre)
