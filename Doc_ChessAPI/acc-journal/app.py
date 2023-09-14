from flask import Flask, render_template, request, redirect, url_for, flash,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_session import Session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import secrets
import string
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key


app = Flask(__name__)

# To run Testing
if app.config['TESTING']:
    app.config.from_pyfile('test_config.py')  # Load the test config

# Initialize the session

app.config['SECRET_KEY'] = generate_secret_key()
app.config['SESSION_TYPE'] = 'filesystem'  # Use a persistent session type
app.config['SESSION_PERMANENT'] = True  # Session doesn't expire on browser close
app.config['SESSION_USE_SIGNER'] = True  # Sign the session data
app.config['SESSION_KEY_PREFIX'] = 'your_session_prefix_'  # Change to a unique prefix
app.config['SESSION_COOKIE_SECURE'] = True  # Enable secure session cookies in production


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:test123@localhost:3306/pythondb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/database_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account_journal.db'
Session(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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
        c_user = db.session.query(User).filter_by(username=current_user.username).all()
        modified_expense_data = expense_data.copy()  # Create a copy of the original data
        modified_expense_data['user_id'] = c_user[0].id
        print("expense_data",modified_expense_data)
        expense = Expense(**modified_expense_data)#pass data as parameters on Expense model
        db.session.add(expense)
        db.session.commit()

    user = User.query.filter_by(username=current_user.username).first()

    if 'first-login'  not in session:
        session['first_login'] = True

        # User is not logging in for the first time, show the last 5 entries
        last_5_expenses = Expense.query.order_by(Expense.id.desc()).limit(5).all()
    else:
        # User is logging in for the first time or doesn't exist, don't show last entries
        last_5_expenses = []

    return render_template('expense.html', last_5_expenses=last_5_expenses)
      #  return jsonify(expense.to_dict())

    expense_categories = db.session.query(ExpenseCategory).all()

    card_details =db.session.query(CardDetails).all()

    return render_template('final_expense.html',card_details=card_details,
                           expense_categories=expense_categories,user=current_user.username)


"""
@app.route('/get_subcategories')
def get_subcategories():
    category_id = request.args.get('category_id')
    subcategories = ExpenseSubcategory.query.filter_by(category_id=category_id).all()
    # Convert subcategories to a list of dictionaries or any desired format
    subcategory_list = [{"id": sub.id, "name": sub.name} for sub in subcategories]
    subcategory_json = json.dumps(subcategory_list)
    print(subcategory_json)
    return render_template('expense.html',expense_subcategory=subcategory_json,user=current_user.username)
"""


# Define the /get_subcategories route
@app.route('/get_subcategories')
def get_subcategories():
    category_id = request.args.get('category_id')
    subcategories = ExpenseSubcategory.query.filter_by(category_id=category_id).all()

    # Convert subcategories to a list of dictionaries
    subcategory_list = [{"id": sub.id, "name": sub.name} for sub in subcategories]
    print(jsonify(subcategory_list),"$$$$$$$$$$$$")
    # Return subcategories as JSON response
    return jsonify(subcategory_list)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('journal.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        print(user,"gggggg")
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            print("test1")
            flash('Logged in successfully!', 'success')
            print("test2")
            return redirect(url_for('home'))
        else:
            print("wrong")
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user instance and store the hashed password
        new_user = User(username=username, email=email, password_hash=hashed_password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    # For  GETrequests, display  the  registration form
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0')
