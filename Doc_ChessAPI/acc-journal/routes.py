from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, flash

db = SQLAlchemy()

users_bp = Blueprint('users', __name__)
expenses_bp = Blueprint('expenses', __name__)

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
        
@app.route('/submit_expense', methods=['POST'])
@login_required  # Protect this page with authentication
def submit_expense():
    if request.method == 'POST':
        # Retrieve form data
        date = request.form['date']
        expense_category = request.form['expense_category']
        expense_subcategory = request.form['expense_subcategory']
        payment_type = request.form['payment_type']
        card_type = request.form['card_type']
        amount_paid = request.form['amount_paid']
        description = request.form['description']

        # Validate and process the expense entry (e.g., save to the database)
        # Implement your logic here

        flash('Expense entry submitted successfully!', 'success')
        return redirect(url_for('expense'))  # Redirect to the expense entry page


@app.route('/expense', methods=['GET'])
@login_required  # Protect this page with authentication
def expense():
    # Fetch expense categories from the database (you'll need to implement this)
    expense_categories = get_expense_categories()

    return render_template('expense.html', expense_categories=expense_categories)

@app.route('/submit_expense', methods=['POST'])
@login_required
def submit_expense():
    if request.method == 'POST':
        date = request.form['date']
        expense_category = request.form['expense_category']
        expense_subcategory = request.form['expense_subcategory']
        payment_type = request.form['payment_type']
        card_type = request.form['card_type']
        amount_paid = request.form['amount_paid']
        description = request.form['description']

        # Create a new Expense object and add it to the database
        expense = Expense(
            date=date,
            expense_category=expense_category,
            expense_subcategory=expense_subcategory,
            payment_type=payment_type,
            card_type=card_type,
            amount_paid=amount_paid,
            description=description,
            user_id=current_user.id  # Set the user ID associated with this expense
        )

        db.session.add(expense)
        db.session.commit()

        flash('Expense entry submitted successfully!', 'success')
        return redirect(url_for('expense'))
"""

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

@expenses_bp.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])

@expenses_bp.route('/expenses', methods=['POST'])
def create_expense():
    expense_data = request.json
    expense = Expense(**expense_data)
    db.session.add(expense)
    db.session.commit()
    return jsonify(expense.to_dict())
