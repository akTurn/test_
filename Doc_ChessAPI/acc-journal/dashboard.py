import mpld3
import plotly.io as pio
import pandas as pd
from sqlalchemy import func,extract
import plotly.express as px
import matplotlib.pyplot as plt

import requests
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, json
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
from flask_sqlalchemy import SQLAlchemy
from flask_login import  UserMixin
import secrets
import string
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta

from flask_jwt_extended import jwt_required, get_jwt_identity


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


class User(UserMixin, db.Model):
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

class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    source = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))
    card_id = db.Column(db.Integer, db.ForeignKey('card_details.id'))
    tax_deductions = db.Column(db.Float)
    tax_year = db.Column(db.Integer)
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


@app.route('/dashboard',methods=['GET', 'POST'])
@jwt_required()
def dashboard():

    # Get the identity (user) from the JWT token
    current_user = get_jwt_identity()

    # Calculate total expenses over a specific period
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    total_expenses = db.session.query(func.sum(Expense.amount_paid)).filter(
        Expense.date >= start_date, Expense.date <= end_date
    ).scalar()

    print(f"Total Expenses: Rs.{total_expenses:.2f}")
    """ ----By Week Analysis----"""
    # Generate a list of dates for the entire year
    date_range = pd.date_range(start=start_date, end=end_date, freq='W-MON')

    # Calculate weekly expenses
    weekly_expenses = []
    for week_start in date_range:
        week_end = week_start + pd.DateOffset(6)  # Calculate the end of the week
        weekly_total = db.session.query(func.sum(Expense.amount_paid)).filter(
            Expense.date >= week_start.date(), Expense.date <= week_end.date()
        ).scalar()
        weekly_expenses.append(weekly_total or 0)

    print("weekly_expenses", weekly_expenses)

    """     weekday and weekend segregations """

    # Generate a list of dates for the entire year
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate daily expenses
    daily_expenses = []
    for date in date_range:
        daily_total = db.session.query(func.sum(Expense.amount_paid)).filter(
            Expense.date == date.date()
        ).scalar()
        daily_expenses.append(daily_total or 0)

    # Create a DataFrame with date and daily expenses
    df = pd.DataFrame({'Date': date_range, 'Daily Expenses': daily_expenses})

    # Group data by weekdays and weekends
    weekdays = df[df['Date'].dt.weekday < 5]
    weekends = df[df['Date'].dt.weekday >= 5]

    # Calculate weekly expenses for weekdays and weekends
    weekly_weekdays = weekdays.groupby(weekdays['Date'].dt.strftime('%U'))['Daily Expenses'].sum()
    weekly_weekends = weekends.groupby(weekends['Date'].dt.strftime('%U'))['Daily Expenses'].sum()

    # Calculate average monthly expenses for a specific year
    year = 2023
    monthly_expenses = db.session.query(
        extract('month', Expense.date).label('expense_month'),
        func.avg(Expense.amount_paid).label('avg_monthly_expense')
    ).filter(
        extract('year', Expense.date) == year
    ).group_by(extract('month', Expense.date)).all()

    for entry in monthly_expenses:
        print(f"Month {entry.expense_month}: Rs.{entry.avg_monthly_expense:.2f}")

    # Calculate total income for the same period
    total_income = db.session.query(func.sum(Income.amount)).filter(
        Income.date >= start_date, Income.date <= end_date
    ).scalar()

    # Calculate the expense ratio
    expense_ratio = (total_expenses / total_income) * 100 if total_income else 0

    print(f"Expense Ratio: {expense_ratio:.2f}%")

    # Calculate the savings rate
    savings_rate = ((total_income - total_expenses) / total_income) * 100 if total_income else 0

    print(f"Savings Rate: {savings_rate:.2f}%")

    # Calculate total debt payments for the same period
    debt_category_id = db.session.query(ExpenseCategory.id).filter_by(name='Debt Payments').scalar()
    print("debt_category_id", debt_category_id)
    total_debt_payments = db.session.query(func.sum(Expense.amount_paid)).filter(
        Expense.expense_category_id == debt_category_id,
        Expense.date >= start_date,
        Expense.date <= end_date
    ).scalar() or 0

    print("total_debt_payments", total_debt_payments)

    # Calculate the debt-to-income ratio
    debt_to_income_ratio = (total_debt_payments / total_income) * 100 if total_income else 0

    print(f"Debt-to-Income Ratio: {debt_to_income_ratio:.2f}%")

    # Example: Query to calculate total expenses by category
    category_expenses = db.session.query(
        ExpenseCategory.name,
        func.sum(Expense.amount_paid).label('total')
    ).join(Expense).group_by(ExpenseCategory.name).all()

    # Prepare data for Plotly chart
    chart_data = [
        {
            'labels': [row.name for row in category_expenses],
            'values': [row.total for row in category_expenses],
            'type': 'pie',
            'hoverinfo': 'label+percent+value',
            'textinfo': 'percent',
            'textposition': 'inside',
            'hole': 0.4,  # Create a donut chart with a hole in the center
        }
    ]
    # Total Expenses
    plt.figure(figsize=(8, 4))
    plt.bar('Total Expenses', total_expenses, color='blue')
    plt.xlabel('Category')
    plt.ylabel('Amount (Rs)')
    plt.title('Total Expenses')
    plt.savefig('total_expenses1.png')
    # plt.show()
    """
    # Create a bar chart for weekly expenses
    plt.figure(figsize=(12, 6))
    plt.bar(date_range, weekly_expenses, width=5, align='center')
    plt.xlabel('Week Starting Date')
    plt.ylabel('Total Expenses (Rs.)')
    plt.title('Weekly Expenses for the Year 2023')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig('weekly_expenses_chart.png')
    plt.show()
    """
    # Create a line chart for weekly expenses (weekdays and weekends)
    plt.figure(figsize=(12, 6))
    plt.plot(weekly_weekdays.index, weekly_weekdays, marker='o', linestyle='-', label='Weekdays')
    plt.plot(weekly_weekends.index, weekly_weekends, marker='o', linestyle='-', label='Weekends')
    plt.xlabel('Week Number')
    plt.ylabel('Total Expenses (Rs.)')
    plt.title('Weekly Expenses Segregated by Weekdays and Weekends for the Year 2023')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    # plt.savefig('weekly_expenses_segregated_line_chart.png')
    plt.show()

    # Monthly Expenses
    months = [f"Month {entry.expense_month}" for entry in monthly_expenses]
    monthly_values = [entry.avg_monthly_expense for entry in monthly_expenses]
    plt.figure(figsize=(10, 6))
    plt.bar(months, monthly_values, color='green')
    plt.xlabel('Month')
    plt.ylabel('Average Monthly Expense (Rs)')
    plt.title('Monthly Expenses for the Year')
    plt.xticks(rotation=45)
    plt.savefig('Monthly_Expenses1.png')
    # plt.show()

    # Expense Ratio and Savings Rate
    labels = ['Expense Ratio', 'Savings Rate']
    values = [expense_ratio, savings_rate]
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['red', 'yellow'])
    plt.title('Expense Ratio vs. Savings Rate')
    # plt.savefig('Expense_savings_ratio.png')
    # plt.show()
    # Convert Matplotlib plot to HTML
    expense_ratio_html = mpld3.fig_to_html(plt.gcf())
    plt.close()  # Close the Matplotlib plot

    # Total Debt Payments and Debt-to-Income Ratio
    labels = ['Total Debt Payments', 'Debt-to-Income Ratio']
    values = [total_debt_payments, debt_to_income_ratio]
    plt.figure(figsize=(6, 6))
    plt.bar(labels, values, color=['purple', 'orange'])
    plt.xlabel('Category')
    plt.ylabel('Amount (Rs) / Ratio (%)')
    plt.title('Total Debt Payments and Debt-to-Income Ratio')
    # plt.show()

    # Monthly Expenses (Plotly Bar Chart)
    monthly_df = pd.DataFrame(monthly_expenses)
    fig = px.bar(monthly_df, x='expense_month', y='avg_monthly_expense',
                 labels={'expense_month': 'Month', 'avg_monthly_expense': 'Average Monthly Expense (Rs.)'},
                 title='Monthly Expenses for the Year')
    # fig.show()

    # Example for Plotly (convert to HTML div)

    fig = px.bar(monthly_df, x='expense_month', y='avg_monthly_expense',
                 labels={'expense_month': 'Month', 'avg_monthly_expense': 'Average Monthly Expense (Rs.)'},
                 title='Monthly Expenses for the Year')
    div = pio.to_html(fig, full_html=False)

    # Expense Ratio and Savings Rate (Plotly Pie Chart)
    expense_df = pd.DataFrame({'Category': ['Expense Ratio', 'Savings Rate'], 'Value': [expense_ratio, savings_rate]})
    fig = px.pie(expense_df, values='Value', names='Category', title='Expense Ratio vs. Savings Rate')
    fig.show()

    # Total Debt Payments and Debt-to-Income Ratio (Plotly Bar Chart)
    debt_df = pd.DataFrame({'Category': ['Total Debt Payments', 'Debt-to-Income Ratio'],
                            'Value': [total_debt_payments, debt_to_income_ratio]})
    fig = px.bar(debt_df, x='Category', y='Value',
                 labels={'Category': '', 'Value': 'Amount (RS.) / Ratio (%)'},
                 title='Total Debt Payments and Debt-to-Income Ratio')
    fig.show()

    return render_template('dashboard.html', total_expenses_image='total_expenses.png',
                           # total_expenses=total_expenses,
                           # monthly_expenses=monthly_expenses
                           monthly_expenses_div=div, expense_ratio_html=expense_ratio_html,
                           # expense_ratio=expense_ratio,
                           savings_rate=savings_rate, total_debt_payments=total_debt_payments,
                           debt_to_income_ratio=debt_to_income_ratio,
                           chart_data=chart_data, user=current_user)




@app.route('/', methods=['GET', 'POST'])
def home():
    #print("home")
    try:
       # Verify the JWT token
       verify_jwt_in_request()
       #print("access_token")
       # User is authenticated, render protected content
       current_user = get_jwt_identity()

       # Split the identity to get user ID and name
       #user_id, username = current_user.split(':')

       #Retrieve the JWT token from the request headers
       jwt_token = request.headers.get('Authorization')
       print(jwt_token)

       print(current_user,"current_user")
       return render_template('journal.html', user=current_user,jwt_token=jwt_token)


    except Exception as e:
        # User is not authenticated or token is invalid, render the login form
        return render_template('login_jwt.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            """# Assuming user.id is an integer and user.username is a string
            identity = f"{user.id}:{user.username}"
            access_token = create_access_token(identity=identity)
"""
            # Credentials are valid, create a JWT token
            access_token = create_access_token(identity=user.id)
           # print(access_token,"login")            # Include the token in the Authorization header
            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            # Redirect to the home route
            response = requests.get(url_for('home', _external=True), headers=headers)

            if response.status_code == 200:
                return response.text
            else:
                flash('Failed to access protected content.', 'danger')
                return redirect(url_for('login_jwt'))

        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login_jwt.html')

@app.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('login_jwt'))
    return render_template('register.html')


@app.route('/logout')
#@jwt_required()
def logout():
     return redirect(url_for('login_jwt'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
