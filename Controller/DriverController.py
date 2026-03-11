import mysql.connector

def register_driver(user):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )

        cursor = dbConnect.cursor()
        command = "INSERT INTO `drivers`(`driver_id`, `name`, `address`, `phone_number`, `email`, `password`, `licence_number`,`is_available`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (user.get_driver_id(),user.get_name(),user.get_address(),user.get_phone_number(),user.get_email(),user.get_password(),user.get_licence_number(),user.get_is_available())
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def login_driver(user):
    driver = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )

        cursor = dbConnect.cursor()
        command = "SELECT * FROM drivers WHERE email=%s and password=%s"
        values = (user.get_email(),user.get_password())
        cursor.execute(command,values)
        driver = cursor.fetchone()
        return driver
        cursor.close()
        dbConnect.close()

    except Exception as err:
        print(f"{err}")
        return driver