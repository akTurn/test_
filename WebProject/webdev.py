# Import the necessary libraries
from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL

# Create a Flask app
app = Flask(__name__)

# Connect to the MySQL database
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Prajith@1984'
app.config['MYSQL_DATABASE'] = 'joindb'

# Initialize the MySQL database
mysql = MySQL(app)
# Create a cursor  object
#cur = mysql.connection.cursor()

with app.app_context():
    cur = mysql.connection.cursor()

# Create a route that renders the index2.html templates
@app.route('/')
def index():
    # Query the database
    cur.execute('SELECT * FROM facility')

    # Fetch all the records
    records = cur.fetchall()

    # Close the cursor
    cur.close()

    # Render the index2.html templates with the records
    return render_template('index2.html', records=records)

# Create a route that handles the POST request from the add_record.html templates
@app.route('/add_record', methods=['POST'])
def add_record():
    # Get the data from the POST request
    fac_id = request.form['fac_id']
    fac_name = request.form['fac_name']

    # Insert the data into the database
    cur.execute('INSERT INTO facility (fac_id, fac_name) VALUES (%s, %s)', (fac_id, fac_name))

    # Redirect the user back to the index page
    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
