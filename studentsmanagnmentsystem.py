from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import pymysql


class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Managemnt System", bd=10, relief=GROOVE,
                      font=("time new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)
        # All Variables
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        # Manage frame

        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_frame.place(x=20, y=90, width=450, height=600)

        m_title = Label(Manage_frame, text="Manage Students", font=("time new roman", 20, "bold"), bg="crimson",
                        fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_frame, text="Roll Number.", font=("time new roman", 10, "bold"), bg="crimson",
                         fg="white")
        lbl_roll.grid(row=1, column=0, pady=20, sticky="w")

        txt_roll = Entry(Manage_frame, textvariable=self.roll_no_var, font=("time new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_frame, text="Name.", font=("time new roman", 10, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=20, sticky="w")

        txt_name = Entry(Manage_frame, textvariable=self.name_var, font=("time new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_frame, text="Email.", font=("time new roman", 10, "bold"), bg="crimson", fg="white")
        lbl_email.grid(row=3, column=0, pady=20, sticky="w")

        txt_email = Entry(Manage_frame, textvariable=self.email_var, font=("time new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_frame, text="Gender", font=("time new roman", 10, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=4, column=0, pady=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, font=("time new roman", 13, "bold"),
                                    state="readonly")
        combo_gender["values"] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(Manage_frame, text="Contact.", font=("time new roman", 10, "bold"), bg="crimson",
                            fg="white")
        lbl_contact.grid(row=5, column=0, pady=20, sticky="w")

        txt_contact = Entry(Manage_frame, textvariable=self.contact_var, font=("time new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_frame, text="D.O.B.", font=("time new roman", 10, "bold"), bg="crimson", fg="white")
        lbl_DOB.grid(row=6, column=0, pady=20, sticky="w")

        txt_DOB = Entry(Manage_frame, textvariable=self.dob_var, font=("time new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_frame, text="Address.", font=("time new roman", 10, "bold"), bg="crimson",
                            fg="white")
        lbl_address.grid(row=7, column=0, pady=20, sticky="w")

        txt_address = Text(Manage_frame, width=35, height=4, font=("", 10))
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Button frame
        btn_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_frame.place(x=10, y=535, width=430)

        addbtn = Button(btn_frame, text="ADD", width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        updatebtn = Button(btn_frame, text="UPDATE", width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="DELETE", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="CLEAR", width=10).grid(row=0, column=3, padx=10, pady=10)

        # Detail frame

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=90, width=800, height=600)

        lbl_search = Label(detail_frame, text="Search By", font=("time new roman", 20, "bold"), bg="crimson",
                           fg="white")
        lbl_search.grid(row=0, column=0, pady=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, width=10, font=("time new roman", 13, "bold"), state="readonly")
        combo_search["values"] = ("Roll No", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(detail_frame, width=20, font=("time new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(detail_frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(detail_frame, text="Show all", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        # Table frame
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=750, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        student_table = ttk.Treeview(table_frame,
                                     columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("roll", text="Roll No.")
        student_table.heading("name", text="name.")
        student_table.heading("email", text="email.")
        student_table.heading("gender", text="gender.")
        student_table.heading("contact", text="contact.")
        student_table.heading("dob", text="dob.")
        student_table.heading("address", text="address.")
        student_table["show"] = "headings"
        student_table.column("roll", width=100)
        student_table.column("name", width=100)
        student_table.column("email", width=100)
        student_table.column("gender", width=100)
        student_table.column("contact", width=100)
        student_table.column("dob", width=100)
        student_table.column("address", width=150)
        student_table.pack(fill=BOTH, expand=1)

    def add_students(self):
        con = pymysql.connect(database="stm", host="localhost", user="root", password="root")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.roll_no_var.get(),
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.address.get('1.0', END)
                                                                          ))
        con.commit()
        con.close()


root = Tk()
ob = student(root)
root.mainloop(