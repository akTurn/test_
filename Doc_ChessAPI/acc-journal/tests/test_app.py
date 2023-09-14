import unittest
from flask import current_app

from Expense.main import Expense
from app import app, db, User, ExpenseCategory  # Import your app and database models

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_home_page_requires_login(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_login(self):
        response = self.app.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        self.assertEqual(response.status_code, 302)  # Redirects to home

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  # Redirects to login

    # Add more test cases for your routes and functionality

    class ExpenseRouteTestCase(unittest.TestCase):

        def setUp(self):
            self.app = app.test_client()
            self.app_context = app.app_context()
            self.app_context.push()
            db.create_all()

            # Create a test user
            user = User(username='test_user', email='test@example.com', password_hash='hashed_password')
            db.session.add(user)
            db.session.commit()

            # Log in the test user
            self.app.post('/login', data={'username': 'test_user', 'password': 'hashed_password'})

        def tearDown(self):
            db.session.remove()
            db.drop_all()
            self.app_context.pop()

        def test_expense_route_requires_login(self):
            response = self.app.get('/expense')
            self.assertEqual(response.status_code, 200)  # Assuming you return a template even if not logged in

        def test_add_expense(self):
            category = ExpenseCategory(name='Test Category')
            db.session.add(category)
            db.session.commit()

            data = {
                'date': '2023-09-09',  # Adjust the date format as needed
                'spend_to': 'MD',
                'expense_category_id': category.id,
                'expense_subcategory_id': 1,  # Replace with a valid subcategory ID
                'payment_type': 'Card',
                'card_id': 1,  # Replace with a valid card ID
                'amount_paid': 100.0,
                'description': 'Test Expense Description'
            }

            response = self.app.post('/expense', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Assuming you return JSON data

            # Check if the expense was added to the database
            added_expense = db.session.query(Expense).first()
            self.assertIsNotNone(added_expense)
            self.assertEqual(added_expense.date, '2023-09-09')  # Adjust the date format as needed
            self.assertEqual(added_expense.spend_to, 'MD')
            self.assertEqual(added_expense.expense_category_id, category.id)
            self.assertEqual(added_expense.payment_type, 'Card')
            self.assertEqual(added_expense.card_id, 1)
            self.assertEqual(added_expense.amount_paid, 100.0)
            self.assertEqual(added_expense.description, 'Test Expense Description')


if __name__ == '__main__':
    unittest.main()
