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

def add_user(username, password):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            print("User added successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")

def delete_user(user_id):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User deleted successfully")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()
    else:
        print("Connection to database failed")
