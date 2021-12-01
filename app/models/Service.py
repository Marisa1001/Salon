from app import db

class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.String(50))

    #relacion foreign
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'))
    contract = db.relationship("Contract", back_populates="services")
    

