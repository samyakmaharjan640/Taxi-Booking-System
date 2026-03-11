import mysql.connector

def login_admin(user):
    admin = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )

        cursor = dbConnect.cursor()
        command = "SELECT * FROM admins WHERE email=%s and password=%s"
        values = (user.get_email(),user.get_password())
        cursor.execute(command,values)
        admin = cursor.fetchone()
        return admin
        cursor.close()
        dbConnect.close()

    except Exception as err:
        print(f"{err}")
        return admin