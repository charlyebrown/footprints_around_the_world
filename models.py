from app import db
from sqlalchemy.dialects.postgresql import JSON


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    email = db.Column(db.String())
    company_type = db.Column(db.String())

    def __init__(self, name, address, email, company_type):
        self.name = name
        self.address = address
        self.email = email
        self.company_type = company_type

    def __repr__(self):
        return '<id {}>'.format(self.id)
