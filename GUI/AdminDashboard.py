from tkinter import *
from tkinter import ttk
import sys
sys.path.append('//Users//samyak//Desktop//PycharmProjects//TaxiBooking')
from tkinter import messagebox
import mysql.connector
from Model.BookingModel import BookingModel
from Controller.BookingController import assign_driver

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.config(bg="dark gray")
        self.root.resizable(height=0,width=0)
        self.root.title("Admin Dashboard")

        self.bodyFrame = Frame(self.root, bg="white")
        self.bodyFrame.place(x=0, y=100, height=600, width=1000)

        self.titleLabel = Label(self.root, text="Admin Dashboard", font=("bold",34), bg="dark gray", fg="red")
        self.titleLabel.place(x=200, y=30, width=600, height=50)

        self.pickupAddressLabel = Label(self.bodyFrame, text="Pickup Address:", font=("bold",14), bg="white")
        self.pickupAddressLabel.place(x=800, y=20, width=150, height=50)

        self.pickupAddressEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.pickupAddressEntry.place(x=800, y=70, width=150, height=30)

        self.dropoffAddressLabel = Label(self.bodyFrame, text="Dropoff Address:", font=("bold",14), bg="white")
        self.dropoffAddressLabel.place(x=800, y=110, width=150, height=50)

        self.dropoffAddressEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.dropoffAddressEntry.place(x=800, y=160, width=150, height=30)

        self.dateLabel = Label(self.bodyFrame, text="Date:", font=("bold",14), bg="white")
        self.dateLabel.place(x=800, y=200, width=150, height=50)

        self.dateEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.dateEntry.place(x=800, y=250, width=150, height=30)

        self.timeLabel = Label(self.bodyFrame, text="Time:", font=("bold",14), bg="white")
        self.timeLabel.place(x=800, y=290, width=150, height=50)

        self.timeEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.timeEntry.place(x=800, y=340, width=150, height=30)

        self.driverIdLabel = Label(self.bodyFrame, text="Driver Id:", font=("bold",14), bg="white")
        self.driverIdLabel.place(x=800, y=380, width=150, height=50)

        self.driverIdEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.driverIdEntry.place(x=800, y=430, width=150, height=30)

        self.bookingIdEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.bookingIdEntry.place(x=1800, y=430, width=150, height=30)

        self.logoutButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Logout", command=self.logout)
        self.logoutButton.place(x=800, y=500, width=150, height=50)

        self.checkButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Check",command= self.check)
        self.checkButton.place(x=105, y=500, width=150, height=50)

        self.assignDriverButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Assign Driver", command=self.assign)
        self.assignDriverButton.place(x=270, y=500, width=150, height=50)

        self.table = ttk.Treeview(self.bodyFrame, columns=(
        'Booking Id', 'Pickup Address', 'Dropoff Address', 'Date', 'Time', 'Booking Status', 'Driver Id'), show='headings')

        self.table.heading('Booking Id', text='Booking Id')
        self.table.heading('Pickup Address', text='Pickup Address')
        self.table.heading('Dropoff Address', text='Dropoff Address')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Booking Status', text='Booking Status')
        self.table.heading('Driver Id', text='Driver Id')

        self.table.column('Booking Id', width=80)
        self.table.column('Pickup Address', width=130)
        self.table.column('Dropoff Address', width=130)
        self.table.column('Date', width=110)
        self.table.column('Time', width=70)
        self.table.column('Booking Status', width=90)
        self.table.column('Driver Id', width=90)
        self.table.bind("<<TreeviewSelect>>", self.selectedRow)

        self.table.place(x=50,y=50,height=400,width=720)

        try:
            dbConnect = mysql.connector.connect(
                host ="localhost",
                user ="root",
                password ="",
                database = "samyakTaxiBooking"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM booking")
            rows = cursor.fetchall()
            for row in rows:
                self.table.insert("","end",values=(row[0], row[1], row[2], row[3], row[4], row[5], row[7]))

        except Exception as err:
            print(f"{err}")


    def logout(self):
        logout_confirmation = messagebox.askyesno("logout","Do you want to logout?")
        if logout_confirmation:
            from Login import Login
            self.root.destroy()
            new_root = Tk()
            Login(new_root)
            new_root.mainloop()

        else:
            return

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

    def check(self):
        from CheckDriver import CheckDriver
        new_root = Tk()
        CheckDriver(new_root)
        new_root.mainloop

    def assign(self):
        driverId = self.driverIdEntry.get()
        bookId = self.bookingIdEntry.get()
        driver = BookingModel(driver_id=driverId,booking_id=bookId)
        assigned = assign_driver(driver)
        if assigned:
            messagebox.showinfo("Assigned", "Driver has been assigned")
            self.root.destroy()
            new_root = Tk()
            Admin(new_root)
            new_root.mainloop()

if __name__ == '__main__':
    root = Tk()
    Admin(root)
    root.mainloop()