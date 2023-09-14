from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import secrets
import string
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import json

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key


app = Flask(__name__)

app.config['SECRET_KEY'] = generate_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:test123@localhost:3306/pythondb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/database_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account_journal.db'

db = SQLAlchemy(app)

class User(UserMixin,db.Model):
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

@app.route('/expense', methods=['GET','POST'])
def expense():

    if request.method == 'POST':
        expense_data = request.form
        expense = Expense(**expense_data)
        db.session.add(expense)
        db.session.commit()
        return jsonify(expense.to_dict())

    expense_categories = db.session.query(ExpenseCategory).all()

    card_details = db.session.query(CardDetails).all()
    print("card_details",card_details)

    return render_template('home.html',card_details=card_details,
                           expense_categories=expense_categories)



@app.route('/get_subcategories')
def get_subcategories():
    category_id = request.args.get('category_id')
    subcategories = ExpenseSubcategory.query.filter_by(category_id=category_id).all()
    subcategory_list = [{"id": sub.id, "name": sub.name} for sub in subcategories]
    print(subcategory_list)
    return json.dumps(subcategory_list)

@app.route('/expense2', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        expense_data = request.form
        expense = Expense(**expense_data)
        db.session.add(expense)
        db.session.commit()
        return jsonify(expense.to_dict())

    expense_categories = db.session.query(ExpenseCategory).all()

    # Fetch all subcategories for each category
    subcategories_dict = {}
    for category in expense_categories:
        subcategories = ExpenseSubcategory.query.filter_by(category_id=category.id).all()
        subcategories_dict[category.id] = [{"id": sub.id, "name": sub.name} for sub in subcategories]

    card_details = db.session.query(CardDetails).all()
    return render_template('home1.html', card_details=card_details, expense_categories=expense_categories, subcategories_dict=subcategories_dict)



@app.route('/')

def home():
    return render_template('index.html', user=current_user)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0')