import pytest
from app import app, db, ExpenseCategory
from flask import current_app
from flask.testing import FlaskClient

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory SQLite database for testing
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.mark.benchmark(group="expense_function")
def test_expense_performance(client, benchmark):
    # Define the test data
    data = {
        'date': '2023-09-09',
        'spend_to': 'MD',
        'expense_category_id': 1,  # Replace with a valid category ID
        'expense_subcategory_id': 1,  # Replace with a valid subcategory ID
        'payment_type': 'Card',
        'card_id': 1,  # Replace with a valid card ID
        'amount_paid': 100.0,
        'description': 'Test Expense Description'
    }

    # Perform the benchmark
    result = benchmark(client.post, '/expense', data=data, follow_redirects=True)

    # Check the result status code and response content
    assert result.status_code == 200
    assert 'expense' in result.get_json()  # Adjust this based on your expected JSON response
