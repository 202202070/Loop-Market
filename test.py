import unittest
from flask import Flask
from __init_py__ import create_app  
from __init_py__ import db
from models import Product, Cart, Order, Customer

class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        
        self.customer = Customer(id=1, name='firstadmin', email='admin@gmail.com')
        self.product = Product(id=1, product_name='Big chips Sour & Cream', current_price=15.0, in_stock=100)
        db.session.add(self.customer)
        db.session.add(self.product)
        db.session.commit()

    
if __name__ == '__main__':
    unittest.main()
