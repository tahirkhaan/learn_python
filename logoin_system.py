from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1350x700+0+0")

        # Images
        self.bg_icon = ImageTk.PhotoImage(file="image/bg.jpg")
        self.user_icon = PhotoImage(file="image/main_user.png")
        self.pswd_icon = ImageTk.PhotoImage(file="image/paswd.png")
        self.logo_icon = ImageTk.PhotoImage(file="image/logo.png")

        # Variable
        self.uname = StringVar()
        self.paswd = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        tittle = Label(self.root, text="Logon System", font=("time new roman", 40, "bold"), bg="yellow", fg="red",
                       bd=10, relief=GROOVE)
        tittle.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=150)

        logolbl = Label(self.root, image=self.logo_icon)
        logolbl = Label(login_frame, image=self.logo_icon,
                        bd=0).grid(row=0, columnspan=2)

        lbluser = Label(login_frame, text="Username", image=self.user_icon, compound=LEFT, font=(
            "times new roman", 20, "bold"), bg="white").grid(row=1, column=0)
        txtuser = Entry(login_frame, bd=5, textvariable=self.uname,
                        relief=GROOVE, font=("", 15)).grid(row=1, column=1)

        lblpaswd = Label(login_frame, text="Pasword", image=self.pswd_icon, compound=LEFT, font=(
            "times new roman", 20, "bold"), bg="white").grid(row=2, column=0)
        txtpswd = Entry(login_frame, bd=5, relief=GROOVE, textvariable=self.paswd, font=(
            "", 15)).grid(row=2, column=1, padx=20)

        btn_log = Button(login_frame, text="login", width=15, command=self.login, font=(
            "time new roman", 14, "bold"), bg="yellow", fg="red").grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.paswd.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.uname.get() == "fahad" and self.paswd.get() == "123456":
            messagebox.showerror("Successfull", f"wellcome {self.uname.get()}")
        else:
            messagebox.showerror("Error", "Invalid user ame or Password")


root = Tk()
obj = login_system(root)
root.mainloop()