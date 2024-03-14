import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="ombati",
            password="your_password",
            database="stock"
        )
        
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)

def add_product(name, quantity, price):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
            conn.commit()
            print("Product added successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")

def update_product(product_id, name, quantity, price):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET name = %s, quantity = %s, price = %s WHERE id = %s", (name, quantity, price, product_id))
            conn.commit()
            print("Product updated successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")

def delete_product(product_id):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            conn.commit()
            print("Product deleted successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")
