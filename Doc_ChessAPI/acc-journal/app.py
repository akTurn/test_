from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import secrets
import string
from werkzeug.security import check_password_hash, generate_password_hash


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
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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
        """
        print(username, user.username,password)
        print("Database Hashed Password:", user.password_hash)
        p1=user.password_hash

        # Hash a password
        hashed_password = generate_password_hash(p1, method='sha256')
        print("Hashed Password:", hashed_password)

        # Verify the password
        is_valid = check_password_hash(hashed_password, p1)
        print("Password Verification:", is_valid)
        """
        if user and check_password_hash(user.password_hash, password):
            print("hi")
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['POST'])
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
