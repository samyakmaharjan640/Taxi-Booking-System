from tkinter import *
import sys
sys.path.append('//Users//samyak//Desktop//PycharmProjects//TaxiBooking')
from Controller.CustomerController import login_customer
from Model.CustomerModel import CustomerModel
from Model import Global
from tkinter import messagebox
from Model.AdminModel import AdminModel
from Controller.AdminController import login_admin
from Model.DriverModel import DriverModel
from Controller.DriverController import login_driver
from PIL import Image,ImageTk

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.config(bg="dark gray")
        self.root.resizable(height=0,width=0)
        self.root.title("Login")

        self.bodyFrame = Frame(self.root, bg="white")
        self.bodyFrame.place(x=0, y=150, height=550, width=1000)

        self.titleLabel = Label(self.root, text="Digital Taxi Stand", font=("bold",34), bg="dark gray")
        self.titleLabel.place(x=300, y=50, width=400, height=50)

        self.emailLabel = Label(self.bodyFrame, text="Your Email:", font=("bold",14), bg="white")
        self.emailLabel.place(x=50, y=110, width=400, height=50)

        self.emailEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.emailEntry.place(x=50, y=160, width=400, height=50)

        self.passwordLabel = Label(self.bodyFrame, text="Your Password:", font=("bold",14), bg="white")
        self.passwordLabel.place(x=50, y=210, width=400, height=50)

        self.passwordEntry = Entry(self.bodyFrame, font=("bold",14), bg="light gray")
        self.passwordEntry.place(x=50, y=260, width=400, height=50)

        self.loginButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Login", command=self.login)
        self.loginButton.place(x=80, y=350, width=150, height=50)

        self.registerButton = Button(self.bodyFrame, font=("bold",14), bg="light gray", text="Register", command=self.register)
        self.registerButton.place(x=270, y=350, width=150, height=50)

        original_image = Image.open("Images/Taxi_picture.png")
        resized_image = original_image.resize((500, 300))
        img = ImageTk.PhotoImage(resized_image)
        self.image_label = Label(self.bodyFrame, image=img,bg="white")
        self.image_label.place(x=500,y=100)
        self.image_label.image = img

    def register(self):
        from Register import Register
        self.root.destroy()
        new_root = Tk()
        Register(new_root)
        new_root.mainloop()

    def login(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()

        customer = CustomerModel(email=email,password=password)
        registered_customer = login_customer(customer)
        admin = AdminModel(email=email,password=password)
        is_admin = login_admin(admin)
        driver = DriverModel(email=email, password=password)
        registered_driver = login_driver(driver)

        if registered_customer is not None:
            Global.customer_information=registered_customer
            messagebox.showinfo("Welcome",f"Welcome {Global.customer_information[1]}")
            self.root.destroy()
            from Booking import Booking
            new_root = Tk()
            Booking(new_root)
            new_root.mainloop()

        elif registered_driver is not None:
            Global.driver_information=registered_driver
            messagebox.showinfo("Welcome",f"Welcome {Global.driver_information[1]}")
            self.root.destroy()
            from DriverDashboard import DriverDashboard
            new_root = Tk()
            DriverDashboard(new_root)
            new_root.mainloop()

        elif is_admin is not None:
            Global.admin_information=is_admin
            messagebox.showinfo("Welcome",f"Welcome {Global.admin_information[1]}")
            self.root.destroy()
            from AdminDashboard import Admin
            new_root = Tk()
            Admin(new_root)
            new_root.mainloop()

        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")


if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()