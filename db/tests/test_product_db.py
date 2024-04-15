import os
import tempfile
import pytest
from db.sqlite_db import ProductDB
from db.db_connector import DBConnector

@pytest.fixture
def db():
    db_fd, db_path = tempfile.mkstemp()
    connector = DBConnector(db_path)
    db_name = "mydatabase.db"
    db = ProductDB(connector, db_name)  # Передаємо db_name як аргумент
    with db:
        db.create_table()
    yield db
    os.close(db_fd)
    os.unlink(db_path)


def test_insert_product(db):
    with db as db_conn:
        db_conn.insert_product('Product 1', 10.99, 100, 'Description 1', 'Category 1')
        product = db_conn.select_product(1)
        assert product is not None
        assert product[1] == 'Product 1'


def test_select_product(db):
    with db as db_conn:
        product = db_conn.select_product(1)
        assert product is None


def test_update_product(db):
    with db as db_conn:
        db_conn.insert_product('Product 3', 30.99, 30, 'Description 3', 'Category 3')
        db_conn.update_product(1, 25.99)
        product = db_conn.select_product(1)
        assert product[2] == 25.99


def test_delete_product(db):
    with db as db_conn:
        db_conn.insert_product('Product 4', 40.99, 20, 'Description 4', 'Category 4')
        db_conn.delete_product(1)
        product = db_conn.select_product(1)
        assert product is None