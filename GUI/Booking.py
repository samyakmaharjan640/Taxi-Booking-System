from tkinter import *

import sys
sys.path.append('//Users//samyak//Desktop//PycharmProjects//TaxiBooking')
# from tkcalendar import DateEntry
from tkinter import ttk
from Model.BookingModel import BookingModel
from Controller.BookingController import Book
from tkinter import messagebox
from Model import Global
import mysql.connector
from Controller.BookingController import update_booking,cancel_booking

class Booking:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.config(bg="dark gray")
        self.root.resizable(height=0,width=0)
        self.root.title("Booking")

        self.bodyFrame = Frame(self.root, bg="white")
        self.bodyFrame.place(x=0, y=100, height=600, width=1000)

        self.titleLabel = Label(self.root, text="Book Taxi Quick and Easy!", font=("bold",34), bg="dark gray")
        self.titleLabel.place(x=200, y=30, width=600, height=50)

        self.pickupAddressLabel = Label(self.bodyFrame, text="Pickup Address:", font=("bold",14), bg="white")
        self.pickupAddressLabel.place(x=700, y=20, width=250, height=50)

        self.pickupAddressEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.pickupAddressEntry.place(x=700, y=70, width=250, height=50)

        self.dropoffAddressLabel = Label(self.bodyFrame, text="Dropoff Address:", font=("bold",14), bg="white")
        self.dropoffAddressLabel.place(x=700, y=140, width=250, height=50)

        self.dropoffAddressEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.dropoffAddressEntry.place(x=700, y=190, width=250, height=50)

        self.dateLabel = Label(self.bodyFrame, text="Date:", font=("bold",14), bg="white")
        self.dateLabel.place(x=700, y=260, width=250, height=50)

        self.dateEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.dateEntry.place(x=700, y=310, width=250, height=50)

        self.timeLabel = Label(self.bodyFrame, text="Time:", font=("bold",14), bg="white")
        self.timeLabel.place(x=700, y=370, width=250, height=50)

        self.timeEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.timeEntry.place(x=700, y=420, width=250, height=50)

        self.bookButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Book Now", command=self.booking)
        self.bookButton.place(x=800, y=500, width=150, height=50)

        self.updateButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Update",command=self.update)
        self.updateButton.place(x=635, y=500, width=150, height=50)

        self.cancelButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Cancel Booking", command=self.cancel)
        self.cancelButton.place(x=305, y=500, width=150, height=50)

        self.bookingIdEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.bookingIdEntry.place(x=1800, y=430, width=150, height=30)

        self.logoutButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Log out", command=self.logout)
        self.logoutButton.place(x=105, y=500, width=150, height=50)

        self.table = ttk.Treeview(self.bodyFrame, columns=(
        'Booking Id', 'Pickup Address', 'Dropoff Address', 'Date', 'Time', 'Booking Status'), show='headings')

        self.table.heading('Booking Id', text='Booking Id')
        self.table.heading('Pickup Address', text='Pickup Address')
        self.table.heading('Dropoff Address', text='Dropoff Address')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Booking Status', text='Booking Status')

        self.table.column('Booking Id', width=80)
        self.table.column('Pickup Address', width=130)
        self.table.column('Dropoff Address', width=130)
        self.table.column('Date', width=80)
        self.table.column('Time', width=70)
        self.table.column('Booking Status', width=110)

        self.table.place(x=50,y=50,height=400,width=620)
        self.table.bind("<<TreeviewSelect>>", self.selectedRow)

        try:
            dbConnect = mysql.connector.connect(
                host ="localhost",
                user ="root",
                password ="",
                database = "samyakTaxiBooking"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM booking WHERE `customer_id`={Global.customer_information[0]}")
            rows = cursor.fetchall()
            for row in rows:
                self.table.insert("","end",values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        except Exception as err:
            print(f"{err}")

    def booking(self):
        pickup = self.pickupAddressEntry.get()
        dropoff = self.dropoffAddressEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()
        status = "Booking Pending"

        booking = BookingModel(pickup_address=pickup,dropoff_address=dropoff,date=date,time=time,booking_status=status,customer_id=Global.customer_information[0])
        booked =Book(booking)
        if booked:
            messagebox.showinfo("Booked","Taxi has been booked")
            self.root.destroy()
            new_root = Tk()
            Booking(new_root)
            new_root.mainloop()

        else:
            messagebox.showinfo("error","error")

    def selectedRow(self, event):
        selected_item = self.table.focus()
        values = self.table.item(selected_item, "values")

        if values:
            self.pickupAddressEntry.delete(0, "end")
            self.pickupAddressEntry.insert(0, values[1])

            self.dropoffAddressEntry.delete(0, "end")
            self.dropoffAddressEntry.insert(0, values[2])

            self.timeEntry.delete(0, "end")
            self.timeEntry.insert(0, values[4])

            self.dateEntry.delete(0, "end")
            self.dateEntry.insert(0, values[3])

            self.bookingIdEntry.delete(0, "end")
            self.bookingIdEntry.insert(0, values[0])

    

    def logout(self):
        messagebox.showinfo("logout", "logged out")
        from Login import Login
        self.root.destroy()
        new_root = Tk()
        Login(new_root)
        new_root.mainloop()

    def update(self):
        bookId = self.bookingIdEntry.get()
        pickup = self.pickupAddressEntry.get()
        dropoff = self.dropoffAddressEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()
        booking_update = BookingModel(booking_id=bookId, pickup_address=pickup,dropoff_address=dropoff,date=date,time=time)
        updated = update_booking(booking_update)
        if updated:
            messagebox.showinfo("Updated", "Data has been updated")
            self.root.destroy()
            new_root = Tk()
            Booking(new_root)
            new_root.mainloop()

    def cancel(self):
        bookId = self.bookingIdEntry.get()
        booking_cancel = BookingModel(booking_id=bookId)
        cancelled = cancel_booking(booking_cancel)
        if cancelled:
            messagebox.showinfo("Cancelled", "Booking has been cancelled")
            self.root.destroy()
            new_root = Tk()
            Booking(new_root)
            new_root.mainloop()


if __name__ == '__main__':
    root = Tk()
    Booking(root)
    root.mainloop()