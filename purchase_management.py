import mysql.connector
from datetime import date

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

def add_purchase(product_id, quantity):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            purchase_date = date.today()
            cursor.execute("INSERT INTO purchases (product_id, quantity, purchase_date) VALUES (%s, %s, %s)", (product_id, quantity, purchase_date))
            conn.commit()
            print("Purchase added successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")
