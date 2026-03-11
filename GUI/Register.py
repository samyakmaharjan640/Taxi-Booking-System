from tkinter import *
from tkinter import ttk
import sys
import sys
sys.path.append('//Users//samyak//Desktop//PycharmProjects//TaxiBooking')
from Model.CustomerModel import CustomerModel
from Controller.CustomerController import register
from tkinter import messagebox
from Model.DriverModel import DriverModel
from Controller.DriverController import register_driver

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.config(bg="dark gray")
        self.root.resizable(height=0,width=0)
        self.root.title("Register")

        self.bodyFrame = Frame(self.root, bg="white")
        self.bodyFrame.place(x=0, y=100, height=600, width=1000)

        self.titleLabel = Label(self.root, text="Register Here!", font=("bold",34), bg="dark gray")
        self.titleLabel.place(x=300, y=30, width=400, height=50)

        self.nameLabel = Label(self.bodyFrame, text="Name:", font=("bold",14), bg="white")
        self.nameLabel.place(x=50, y=20, width=400, height=50)

        self.nameEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.nameEntry.place(x=50, y=70, width=400, height=50)

        self.addressLabel = Label(self.bodyFrame, text="Address:", font=("bold",14), bg="white")
        self.addressLabel.place(x=50, y=140, width=400, height=50)

        self.addressEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.addressEntry.place(x=50, y=190, width=400, height=50)

        self.phoneNumberLabel = Label(self.bodyFrame, text="Phone Number:", font=("bold",14), bg="white")
        self.phoneNumberLabel.place(x=50, y=260, width=400, height=50)

        self.phoneNumberEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.phoneNumberEntry.place(x=50, y=310, width=400, height=50)

        self.emailLabel = Label(self.bodyFrame, text="Email:", font=("bold",14), bg="white")
        self.emailLabel.place(x=550, y=20, width=400, height=50)

        self.emailEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.emailEntry.place(x=550, y=70, width=400, height=50)

        self.methodLabel = Label(self.bodyFrame, text="Method of Payment:", font=("bold",14), bg="white")
        self.methodLabel.place(x=550, y=140, width=400, height=50)

        methodOption = ["Online Payments","Mobile Wallets","Credit/Debit Cards"]
        self.methodEntry = ttk.Combobox(self.bodyFrame, font=("bold",14), values=methodOption)
        self.methodEntry.place(x=550, y=190, width=400, height=50)

        self.typeLabel = Label(self.bodyFrame, text="Account Type:", font=("bold",14), bg="white")
        self.typeLabel.place(x=550, y=260, width=400, height=50)

        typeOptions = ["Driver Account","Customer Account"]
        self.typeEntry = ttk.Combobox(self.bodyFrame, font=("bold", 14), values=typeOptions)
        self.typeEntry.place(x=550, y=310, width=400, height=50)

        self.licenceLabel = Label(self.bodyFrame, text="Licence:", font=("bold",14), bg="white")
        self.licenceLabel.place(x=50, y=370, width=400, height=50)

        self.licenceEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.licenceEntry.place(x=50, y=420, width=400, height=50)

        self.passwordLabel = Label(self.bodyFrame, text="Password:", font=("bold",14), bg="white")
        self.passwordLabel.place(x=550, y=370, width=400, height=50)

        self.passwordEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.passwordEntry.place(x=550, y=420, width=400, height=50)

        self.backButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Back", command=self.back)
        self.backButton.place(x=540, y=500, width=150, height=50)

        self.registerButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Register", command=self.register)
        self.registerButton.place(x=305, y=500, width=150, height=50)

    def back(self):
        from Login import Login
        self.root.destroy()
        new_root = Tk()
        Login(new_root)
        new_root.mainloop()

    def register(self):
        name = self.nameEntry.get()
        address = self.addressEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        payment = self.methodEntry.get()
        phone = self.phoneNumberEntry.get()
        licence = self.licenceEntry.get()
        available = "Yes"

        if self.typeEntry.get() == "Customer Account":
            customer = CustomerModel(name=name,address=address,email=email,password=password,payment_method=payment,phone_number=phone)
            registered = register(customer)
            if registered:
                messagebox.showinfo("Registered","Customer has been registered")
            else:
                messagebox.showinfo("Error","Error")

        if self.typeEntry.get() == "Driver Account":
            driver = DriverModel(name=name,address=address,email=email,password=password,phone_number=phone,licence_number=licence,is_available=available)
            registered = register_driver(driver)
            if registered:
                messagebox.showinfo("Registered","Driver has been registered")
            else:
                messagebox.showinfo("Error","Error")


if __name__ == '__main__':
    root = Tk()
    Register(root)
    root.mainloop()