# Import the necessary libraries
from flask import Flask, render_template, request, redirect
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Prajith@1984',
    database='joindb'
)


# Create a route that renders the index2.html templates
@app.route('/')
def index():
    records = []
    # Create a cursor object
    cur = cnx.cursor()
    cur.callproc('fac_proc')
    result_sets = cur.stored_results()
    for result_set in result_sets:
        rows = result_set.fetchall()
        # Process the fetched rows as needed

        for row in rows:
            records.append(row)

    # Close the cursor
    cur.close()

    # Render the index2.html templates with the records
    return render_template('facility.html', records=records)


# Create a route that handles the POST request from the add_record.html templates
@app.route('/add_record', methods=['POST'])
def add_record():
    # Get the data from the POST request
    data = request.form.to_dict()

    # Create a cursor object
    cur = cnx.cursor()

    # Generate the column names and placeholders
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    values = ','.join(data.values())

    # Extract the values from the data dictionary
    # values = tuple(data.values())
    # values = list(data.values())

    # Build the query string
    query = f'INSERT INTO facility ({columns}) VALUES ({placeholders})'

    # Execute the query with the provided values
    cur.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cur.close()

    # Redirect the user back to the index page
    return redirect('/')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
