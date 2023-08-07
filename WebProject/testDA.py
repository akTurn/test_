import matplotlib.pyplot as plt
from flask import Flask,request,redirect,render_template
import mysql.connector

app = Flask(__name__)

cnx=mysql.connector.connect(
    host = "Localhost",
    user = "root",
    password = "Prajith@1984",
    database = "org"
)

@app.route('/')
def index():
    # Create a cursor object
    cur = cnx.cursor()

    # Query the database
    cur.execute('SELECT * from worker')

    # Fetch all the records
    records = cur.fetchall()

    # Close the cursor
    cur.close()

    # Extract the first names and salaries from the records
    names = [record[1] for record in records]
    salaries = [record[3] for record in records]

    # Generate a bar chart
    plt.bar(names, salaries)
    plt.xlabel('Worker Name')
    plt.ylabel('Salary')
    plt.title('Salary Distribution')

    # Save the chart as an image
    plt.savefig('chart.png')

    # Render the index.html template with the chart image file path
    return render_template('chart.html', chart_image='chart.png')
if __name__ == '__main__':
    app.run(debug=True)