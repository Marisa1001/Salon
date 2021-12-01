from app import db

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.String(50))
    

    #relacion uno a muchos con contract
    contract = db.relationship("Contract", back_populates="events")