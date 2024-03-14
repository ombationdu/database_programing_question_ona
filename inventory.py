import database_setup2
import product_management
import purchase_management
import sales_management
import user_management
import mysql.connector

conn = mysql.connector.connect(
           host="127.0.0.1",
          user="ombati",
            password="your_password",
           database="stock"
     )

    

database_setup2.create_product_table(conn)
database_setup2.create_purchase_table(conn)
database_setup2.create_sales_table(conn)
database_setup2.create_user_table(conn)
database_setup2.setup_database()
print("1. login\n"
      "2. exit"
)
option = int(input("Enter: "))
while (option == 1):
    #Authentication
    print("------Authentication-----")
    user = input("Enter user: ")
    password = input("Enter password: ")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query,(user,password))
    result = cursor.fetchone()


    if result:
        print("------Main Menu-----\n"
            "1. Product Management\n"
            "2. Purchase Management\n"
            "3. Sales Management\n"
            "4. User Management\n"
            "5. Exit"
            )
        option1= input("Enter: ")
        option1 = int(option1)

        #Product management
        if option1 == 1:
            print("----- Product Management -----\n"
                "1. Add Product\n"
                "2. Update Product\n"
                "3. Delete Product")
            option2 = input("Enter: ")
            option2 = int(option2)
            if option2 == 1:
                product_name = input("Product name: ")
                product_quantity = input("Product quantity: ")
                product_quantity = int(product_quantity)
                product_price = input("Product price: ")
                product_price = int(product_price)
                product_management.add_product(product_name,product_quantity,product_price)
            
            elif option2 == 2:
                product_id = input("Product ID: ")
                product_id = int(product_id)
                product_name = input("Product name: ")
                product_quantity = input("Product quantity: ")
                product_quantity = int(product_quantity)
                product_price = input("Product price: ")
                product_price = int(product_price)
                product_management.update_product(product_id,product_name,product_quantity,product_price)

            elif option2 == 3:
                product_id = input("Product ID: ")
                product_id = int(product_id)
                product_management.delete_product(product_id)

        #Purchase Management
        if option1 == 2:
            product_id = input("Product ID: ")
            product_id = int(product_id)
            product_quantity = input("Product quantity: ")
            product_quantity = int(product_quantity)
            purchase_management.add_purchase(product_id,product_quantity)
            

        #Sales Management
        if option1 == 3:
            product_id = input("Product ID: ")
            product_id = int(product_id)
            product_quantity = input("Product quantity: ")
            product_quantity = int(product_quantity)
            sales_management.add_sale(product_id,product_quantity)

        #User Management
        if option1 == 4:
            print("-----User Management\n"
            "1. Add User\n"
            "2. Delete User\n"
            )
            option2 = int(input("Enter: "))
            if option2 == 1:
                user_name = input("User name: ")
                User_password = input("Password: ")
                user_management.add_user(user_name,User_password)

            if option2 == 2:
                user_id = int(input("Enter: "))
                user_management.delete_user(user_id)
        if option1 == 5:
            break

    else:
        print("User not found")

