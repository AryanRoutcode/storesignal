from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Merchant(db.Model):
    __tablename__ = "merchants"

    id = db.Column(db.Integer, primary_key=True)

    store_name = db.Column(db.String(255), nullable=False)

    store_url = db.Column(db.String(500), nullable=False)

    industry = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship("Product", backref="merchant", lazy=True)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    merchant_id = db.Column(
        db.Integer,
        db.ForeignKey("merchants.id"),
        nullable=False
    )

    title = db.Column(db.String(500))

    description = db.Column(db.Text)

    price = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)