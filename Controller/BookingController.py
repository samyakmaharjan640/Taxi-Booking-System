import mysql.connector

def Book(booking):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )
        cursor = dbConnect.cursor()
        command = "INSERT INTO `booking`(`booking_id`, `pickup_address`, `dropoff_address`, `date`, `time`, `booking_status`, `customer_id`, `driver_id`, `admin_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            booking.get_booking_id(),
            booking.get_pickup_address(),
            booking.get_dropoff_address(),
            booking.get_date(),
            booking.get_time(),
            booking.get_booking_status(),
            booking.get_customer_id(),
            booking.get_driver_id(),
            booking.get_admin_id()
        )
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def assign_driver(asign):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )
        cursor = dbConnect.cursor()
        command = "UPDATE `booking` SET `driver_id`=%s WHERE `booking_id`=%s"
        command2 = "UPDATE `drivers` SET `is_available`='No' WHERE `driver_id`=%s"
        values = (
            asign.get_driver_id(),
            asign.get_booking_id(),
        )
        values2 = (
            asign.get_driver_id(),
        )
        cursor.execute(command,values)
        cursor.execute(command2,values2)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def update_booking(asign):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )
        cursor = dbConnect.cursor()
        command = "UPDATE `booking` SET `pickup_address`=%s,`dropoff_address`=%s,`date`=%s,`time`=%s WHERE `booking_id`=%s"
        values = (
            asign.get_pickup_address(),
            asign.get_dropoff_address(),
            asign.get_date(),
            asign.get_time(),
            asign.get_booking_id(),
        )
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def cancel_booking(asign):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )
        cursor = dbConnect.cursor()
        command = "UPDATE `booking` SET `booking_status`='Booking Cancelled' WHERE `booking_id`=%s"
        values = (
            asign.get_booking_id(),
        )
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False

def complete_booking(complete):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="samyakTaxiBooking"
        )
        cursor = dbConnect.cursor()
        command = "UPDATE `booking` SET `booking_status`='Booking Completed' WHERE `booking_id`=%s"
        command2 = "UPDATE `drivers` SET `is_available`='Yes' WHERE `driver_id`=%s"
        values = (
            complete.get_booking_id(),
        )
        values2 = (
            complete.get_driver_id(),
        )
        cursor.execute(command,values)
        cursor.execute(command2,values2)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as err:
        print(f"{err}")
        return False