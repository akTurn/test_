from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
"""

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    expense_category = db.Column(db.String(255), nullable=False)
    expense_subcategory = db.Column(db.String(255), nullable=False)
    payment_type = db.Column(db.String(50), nullable=False)
    card_type = db.Column(db.String(50))  # Optional, only if payment_type is "card"
    amount_paid = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    # Add a foreign key to associate expenses with a user (if needed)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Expense(id={self.id}, date={self.date}, category={self.expense_category}, amount={self.amount_paid})"


"""
class Expense(db.Model):
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


class ExpenseCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class ExpenseSubcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'), nullable=False)

class CardDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_type = db.Column(db.String(50), nullable=False)
    card_name = db.Column(db.String(255), nullable=False)

"""
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(250),unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    #Exp_transactions = db.relationship('ExpenseTransaction', backref='user', lazy=True)
    #Inc_transactions = db.relationship('IncomeTransaction', backref ='user', lazy=True)

class ExpenseTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exp_category = db.Column(db.String(250),nullable=False)
    Exp_sub_category = db.Column(db.String(250),nullable=False)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float,nullable=False)
    amt_type = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class IncomeTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Income_category = db.Column(db.String(250),nullable=False)
    In_sub_category = db.Column(db.String(250),nullable=False)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float,nullable=False)
    amt_type = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


"""
