from app import db
from app.models.Service import Service

class Contract(db.Model):
    __tablename__ = "contracts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    total = db.Column(db.String(50))

    #relacion uno a muchos con services
    service = db.relationship("Sevice", back_populates="contracts")

    #relacion foreign con eventos
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship("Event", back_populates="contracts")

    #relacion foreign con clientes
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship("Client", back_populates="contracts")

    #relacion foreign con usuarios
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="contracts")

