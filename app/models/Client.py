from app import db

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client = db.Column(db.String(50))
    ci = db.Column(db.String(50))
    telephone = db.Column(db.String(50))
    email = db.Column(db.String(50))

    #relacion uno a muchos con contract
    contract = db.relationship("Contract", back_populates="clients")