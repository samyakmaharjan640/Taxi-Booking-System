from tkinter import *
from tkinter import ttk

class AllDrivers:
    def __init__(self,root):
        self.root = root
        root.geometry("300x300")
        root.title("Drivers")

        self.table = ttk.Treeview(self.root, columns=(
            'Driver Id', 'Name', 'Dropoff Address', 'Date', 'Time', 'Booking Status'), show='headings')

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

        self.table.place(x=50, y=50, height=400, width=620)

if __name__ == '__main__':
    root = Tk()
    AllDrivers(root)
    root.mainloop()