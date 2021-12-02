from app import db


class Contract(db.Model):
    __tablename__ = "contracts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client = db.Column(db.String(50))
    tipe = db.Column(db.String(50))
    date = db.Column(db.Date)
    color = db.Column(db.String(50))
    total = db.Column(db.Integer)


    #relacion foreign con usuarios
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #user = db.relationship("User", back_populates="contracts")

