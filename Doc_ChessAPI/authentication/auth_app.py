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

# Configuration settings
app.config['SECRET_KEY'] = generate_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:test123@localhost:3306/pythondb'

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define a user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the home route, accessible only when logged in
@app.route('/')
@login_required
def home():
    return render_template('journal.html', user=current_user)

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

# Define the registration route
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

# Define the logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Run the Flask app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
