from flask_login import UserMixin

from app import db

from werkzeug.security import check_password_hash, generate_password_hash
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    spend_to = db.Column(db.Enum('MD', 'Family'), nullable=False, default='MD')
    expense_category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)
    expense_subcategory_id = db.Column(db.Integer, db.ForeignKey('expense_subcategories.id'), nullable=False)
    payment_type = db.Column(db.Enum('Card', 'Cash'), nullable=False, default='Card')
    card_id = db.Column(db.Integer, db.ForeignKey('card_details.id'))
    amount_paid = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    source = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))
    card_id = db.Column(db.Integer, db.ForeignKey('card_details.id'))
    tax_deductions = db.Column(db.Float)
    tax_year = db.Column(db.Integer)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class ExpenseCategory(db.Model):
    __tablename__ = 'expense_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class ExpenseSubcategory(db.Model):
    __tablename__ = 'expense_subcategories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)


class CardDetails(db.Model):
    __tablename__ = 'card_details'
    id = db.Column(db.Integer, primary_key=True)
    card_type = db.Column(db.String(50), nullable=False)
    card_name = db.Column(db.String(255), nullable=False)

