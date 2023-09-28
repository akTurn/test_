from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key

app = Flask(__name__)

# Set the secret key for Flask session
app.secret_key = generate_secret_key()

# Initialize JWT manager
jwt = JWTManager(app)

# Configure JWT settings (you can change these according to your needs)
app.config['JWT_SECRET_KEY'] = generate_secret_key()
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # Token expiration time
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:test123@localhost:3306/python_db'

db = SQLAlchemy(app)

"""
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object("config.DevelopmentConfig")

# ORM setup
db = SQLAlchemy(app)
ma = Marshmallow(app)
"""
db.create_all()

# Routes setup
import routes

if __name__ == "__main__":
    app.run(debug=True)