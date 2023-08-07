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
    database='org'
)

# Create a route that renders the index.html template
@app.route('/')
def index():
    # Create a cursor object
    cur = cnx.cursor()

    # Query the database
    cur.execute('SELECT * FROM worker')

    # Fetch all the records
    records = cur.fetchall()

    # Close the cursor
    cur.close()

    # Render the index.html template with the records
    return render_template('index.html', records=records)


# Create a route that renders the index2.html template
@app.route('/index2')
def Newpage():

    cur = cnx.cursor()
    cur.execute('SELECT * FROM bonus')
    records = cur.fetchall()
    cur.close()
    return render_template('index2.html', records=records)

# Create a route that handles the GET request for add_record.html
@app.route('/add', methods=['GET'])
def show_add_record_form():
    # Render the add_record.html template
    return render_template('add.html')


# Create a route that handles the POST request from the add_record.html form
@app.route('/add_record', methods=['POST'])
def add_record():
    data=request.form.to_dict()
    cols=",".join(data.keys())
    phl=",".join("%s"*len(cols))
    values=list(data.values())

    # Create a cursor object
    cur = cnx.cursor()
    """
    # Get the data from the POST request
    id = request.form['WORKER_ID']
    fname = request.form['FIRST_NAME']
    lname = request.form['LAST_NAME']
    sal = request.form['SALARY']
    jndt = request.form['JOINING_DATE']
    dep = request.form['DEPARTMENT']


    # Insert the data into the database
    cur.execute('INSERT INTO worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES (%s, %s, %s, %s, %s, %s)',
                (id, fname, lname, sal, jndt, dep))
    """
    query=f" Insert INTO ({cols})values({phl})"
    cur.execute(query,values)

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cur.close()

    # Redirect the user back to the index page
    return redirect('/')


# Create a route that handles the PUT request to update a worker record
@app.route('/worker/<int:worker_id>', methods=['PUT'])
def update_worker(worker_id):
   # Get the data  from the request
    data = request.get_json()
    # Create a cursor object
    cur = cnx.cursor()
    # Generate the SET clause dynamically
    set_clause = ', '.join([f'{column} = %s' for column in data.keys()])
    # Build the query string
    query = f'UPDATE your_table SET {set_clause} WHERE record_id = %s'
    # Extract the values from the data dictionary
    values = list(data.values()) + [record_id]

    # Execute the query with the provided values
    cur.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cur.close()

    # Return a response
    return 'Record updated successfully'
    """
    # Get the data from the request
    fname = request.form['FIRST_NAME']
    lname = request.form['LAST_NAME']
    sal = request.form['SALARY']
    jndt = request.form['JOINING_DATE']
    dep = request.form['DEPARTMENT']

    # Create a cursor object
    cur = cnx.cursor()

    # Update the worker record in the database
    cur.execute('UPDATE worker SET FIRST_NAME = %s, LAST_NAME = %s, SALARY = %s, JOINING_DATE = %s, DEPARTMENT = %s WHERE WORKER_ID = %s',
                (fname, lname, sal, jndt, dep, worker_id))

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cur.close()

    # Redirect or render a response after updating the worker record
    return redirect('/')
    """
# Create a route that handles the DELETE request to delete a worker record
@app.route('/worker/<int:worker_id>', methods=['DELETE'])
def delete_worker(worker_id):
    # Create a cursor object
    cur = cnx.cursor()

    # Delete the worker record from the database
    cur.execute('DELETE FROM worker WHERE WORKER_ID = %s', (worker_id,))

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cur.close()

    # Return a response
    return 'Worker record deleted successfully'



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
