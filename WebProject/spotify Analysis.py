# Import the necessary libraries
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Prajith@1984',
    database='nba'
)

# Create a route that renders the index.html template
#@app.route('/')

def index():
    # Create a cursor object
    cur = cnx.cursor()

    # Query the database
    cur.execute('SELECT * FROM sg_dly')

    # Fetch all the records
    records = cur.fetchall()
  # Extract the first names and salaries from the records
    song = [record[3] for record in records]
    streams = [record[10] for record in records]

    # Generate a bar chart
    """plt.bar(song, streams)
    plt.xlabel('Song Name')
    plt.ylabel('Streams')
    plt.title(' Distribution')"""
    plt.plot(streams,song)
    plt.show()
    # Close the cursor
    cur.close()

    # Render the index.html template with the records
    #return render_template('spotify.html', records=records)


# Create a route that renders the index2.html template
#@app.route('/index2')
def Newpage():

    cur = cnx.cursor()
    cur.execute('SELECT * FROM sg_dt')
    records = cur.fetchall()

    cur.close()
    #return render_template('index2.html', records=records)
index()


import numpy as np

# Create some data
hours_studied = np.linspace(0, 10, 100)
test_scores = hours_studied ** 2

# Plot the data
plt.plot(hours_studied, test_scores)

# Add a title
plt.title('Hours Studied vs. Test Score')

# Add labels to the x-axis and y-axis
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')

# Show the chart
plt.show()

#Newpage()
"""
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
"""