from flask_jwt_extended import current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db,app
from flask import Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, flash
from models import ExpenseCategory, CardDetails, Expense, User, ExpenseSubcategory


@app.route('/expense', methods=['GET', 'POST'])
def expense():
    expense_categories = db.session.query(ExpenseCategory).all()
    card_details = db.session.query(CardDetails).all()
    history_data = db.session.query(Expense).order_by(Expense.id.desc()).limit(5).all()
    if request.method == 'POST':
        expense_data = request.form
        c_user = db.session.query(User).filter_by(username=current_user.username).all()
        modified_expense_data = expense_data.copy()  # Create a copy of the original data
        modified_expense_data['user_id'] = c_user[0].id
        expense = Expense(**modified_expense_data)  # pass data as parameters on Expense model
        db.session.add(expense)
        db.session.commit()
        history_data = Expense.query.order_by(Expense.id.desc()).limit(5).all()
        return render_template('final_expense.html',form_title='Create Expense',
                               card_details=card_details,
                               history_data=history_data,
                               expense_categories=expense_categories,
                               user=current_user.username)

    return render_template('final_expense.html', form_title='Create Expense',
                           card_details=card_details,
                           history_data=history_data,
                           expense_categories=expense_categories,
                           user=current_user.username)

@app.route('/expense/delete/<int:expense_id>',methods=['DELETE'])

def delete_expense(expense_id):
    print("delete")
    expense_categories = db.session.query(ExpenseCategory).all()
    card_details = db.session.query(CardDetails).all()
    history_data = db.session.query(Expense).order_by(Expense.id.desc()).limit(5).all()
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return render_template('final_expense.html', form_title='Create Expense',
                           card_details=card_details,
                           history_data=history_data,
                           expense_categories=expense_categories,
                           user=current_user.username)

@app.route('/expense/update/<int:expense_id>', methods=['GET', 'POST'])
def update_expense(expense_id):
    # Retrieve the expense to be updated from the database
    expense = Expense.query.get_or_404(expense_id)
    category_u = ExpenseCategory.query.all()
    card_u = CardDetails.query.all()

    if request.method == 'POST':
        # Update expense data based on the form input
        expense.date = request.form['date']
        expense.spend_to = request.form['spend_to']
        expense.expense_category_id = request.form['expense_category_id']
        expense.expense_subcategory_id = request.form['expense_subcategory_id']
        expense.payment_type = request.form['payment_type']
        expense.card_id = request.form['card_id']
        expense.amount_paid = request.form['amount_paid']
        expense.description = request.form['description']

        db.session.commit()
        flash('Expense updated successfully', 'success')
        return redirect(url_for('expense',
                                form_title='Create Expense',
                                user=current_user.username))

    return render_template('final_expense.html', user=current_user.username,
                           form_title='Update Expense', expense=expense,
                           category_u=category_u,card_u=card_u)


@app.route('/get_subcategories')
def get_subcategories():
    category_id = request.args.get('category_id')
    print("category_id",category_id)
    subcategories = ExpenseSubcategory.query.filter_by(category_id=category_id).all()

    # Convert subcategories to a list of dictionaries
    subcategory_list = [{"id": sub.id, "name": sub.name} for sub in subcategories]
    print("subcategory_list", subcategory_list)
    # Return subcategories as JSON response
    return jsonify(subcategory_list)


@app.route('/')
def home():
    return render_template('journal.html', user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
           # login_user(user)

            flash('Logged in successfully!', 'success')

            return redirect(url_for('home'))
        else:
            print("wrong")
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')


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
        return redirect(url_for('login'))

    # For  GETrequests, display  the  registration form
    return render_template('register.html')


@app.route('/logout')
#@login_required
def logout():
    #logout_user()
    return redirect(url_for('login'))
