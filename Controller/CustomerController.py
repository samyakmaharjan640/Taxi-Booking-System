import mysql.connector

def register(user):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )

        cursor = dbConnect.cursor()
        command = "INSERT INTO `customers`(`customer_id`, `name`, `address`, `phone_number`, `email`, `password`, `payment_method`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (user.get_customer_id(),user.get_name(),user.get_address(),user.get_phone_number(),user.get_email(),user.get_password(),user.get_payment_method())
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def login_customer(user):
    customer = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )

        cursor = dbConnect.cursor()
        command = "SELECT * FROM customers WHERE email=%s and password=%s"
        values = (user.get_email(),user.get_password())
        cursor.execute(command,values)
        customer = cursor.fetchone()
        return customer
        cursor.close()
        dbConnect.close()

    except Exception as err:
        print(f"{err}")
        return customer

