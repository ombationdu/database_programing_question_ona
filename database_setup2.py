import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="stock"
)


cursor = conn.cursor()


def create_product_table(conn):
    query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            product_quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
    """
    cursor.execute(query)
    conn.commit()

def create_purchase_table(conn):
    query = """
        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            purchase_quantity INT NOT NULL,
            purchase_date DATE,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """
    cursor.execute(query)
    conn.commit()
    

def create_sales_table(conn):
    query = """
        CREATE TABLE IF NOT EXISTS sales (
            sales_id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            sales_quantity INT NOT NULL,
            sale_date DATE,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """
    cursor.execute(query)
    conn.commit()

def create_user_table(conn):
    query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(query)
    conn.commit()

def setup_database():
    
    if conn:
        create_product_table(conn)
        create_purchase_table(conn)
        create_sales_table(conn)
        create_user_table(conn)
        conn.close()
    else:
        print("Connection to database failed")

if __name__ == "__main__":
    setup_database()
