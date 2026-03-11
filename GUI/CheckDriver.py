from tkinter import *

import sys
sys.path.append('//Users//samyak//Desktop//PycharmProjects//TaxiBooking')
import mysql.connector
from tkinter import ttk

class CheckDriver:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("All Drivers")

        self.table = ttk.Treeview(self.root, columns=(
        "Driver_id", "Name","Availability"), show="headings")
        self.table.heading("Driver_id", text="Driver_id")
        self.table.heading("Name", text="Name")
        self.table.heading("Availability", text="Availability")
        self.table.place(x=0, y=0, height=300, width=300)

        for column in (
        "Driver_id", "Name","Availability"):
            self.table.column(column, width=100)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="samyakTaxiBooking"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM drivers")
            rows = cursor.fetchall()
            for row in rows:
                self.table.insert("", "end", values=(row[0], row[1], row[7]))

        except Exception as err:
            print(f"{err}")

if __name__ == '__main__':
    root = Tk()
    CheckDriver(root)
    root.mainloop()