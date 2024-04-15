from db.db_base.db_connector import DBConnector
class ProductDB():
    def __init__(self, connector, db_name):
        self.connector = connector
        self.db_name = db_name

    def create_table(self):
        with self.connector as conn:
            cursor = self.connector.cursor()  # Використовуйте вже існуючий курсор
            cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    price REAL,
                                    quantity INTEGER,
                                    description TEXT,
                                    category TEXT
                                )''')

    def insert_product(self, name, price, quantity, description, category):
        with self.connector as conn:
            cursor = self.connector.cursor()  # Використовуйте вже існуючий курсор
            cursor.execute('''INSERT INTO products (name, price, quantity, description, category) 
                                  VALUES (?, ?, ?, ?, ?)''', (name, price, quantity, description, category))

    def select_product(self, product_id):
        with self.connector as conn:
            cursor = self.connector.cursor()  # Використовуйте вже існуючий курсор
            cursor.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
            return cursor.fetchone()

    def update_product(self, product_id, price):
        with self.connector as conn:
            cursor = self.connector.cursor()  # Використовуйте вже існуючий курсор
            cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (price, product_id))

    def delete_product(self, product_id):
        with self.connector as conn:
            cursor = self.connector.cursor()  # Використовуйте вже існуючий курсор
            cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
