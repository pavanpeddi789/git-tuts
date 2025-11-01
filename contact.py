# Import modules
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ================== DATABASE ==================
def Database():
    conn = sqlite3.connect("contact_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            gender TEXT,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)
    cursor.execute("SELECT * FROM contact ORDER BY lastname ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


# ================== FUNCTIONS ==================
def SubmitData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or PHONE.get() == "":
        messagebox.showwarning("Warning", "Please complete all required fields!")
        return

    conn = sqlite3.connect("contact_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contact (firstname, lastname, gender, phone, email)
        VALUES (?, ?, ?, ?, ?)
    """, (FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), PHONE.get(), EMAIL.get()))
    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Contact added successfully!")
    Reset()
    DisplayData()


def DisplayData():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect("contact_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contact ORDER BY lastname ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def DeleteData():
    if not tree.selection():
        messagebox.showerror("Error", "Please select a record to delete!")
        return
    result = messagebox.askquestion("Confirm", "Are you sure you want to delete this contact?")
    if result == 'yes':
        selected_item = tree.selection()[0]
        selected_id = tree.item(selected_item)['values'][0]
        conn = sqlite3.connect("contact_app.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contact WHERE contact_id=?", (selected_id,))
        conn.commit()
        cursor.close()
        conn.close()
        tree.delete(selected_item)
        messagebox.showinfo("Deleted", "Contact deleted successfully!")


def UpdateData():
    if not tree.selection():
        messagebox.showerror("Error", "Please select a record to update!")
        return

    selected_item = tree.selection()[0]
    selected_id = tree.item(selected_item)['values'][0]

    conn = sqlite3.connect("contact_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contact
        SET firstname=?, lastname=?, gender=?, phone=?, email=?
        WHERE contact_id=?
    """, (FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), PHONE.get(), EMAIL.get(), selected_id))
    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Updated", "Contact updated successfully!")
    Reset()
    DisplayData()


def Reset():
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    PHONE.set("")
    EMAIL.set("")


def OnSelect(event):
    item = tree.selection()
    if item:
        data = tree.item(item[0], "values")
        FIRSTNAME.set(data[1])
        LASTNAME.set(data[2])
        GENDER.set(data[3])
        PHONE.set(data[4])
        EMAIL.set(data[5])


# ================== GUI ==================
root = Tk()
root.title("Contact Management System")
root.geometry("800x500")
root.config(bg="#f0f3f5")

# Variables
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
PHONE = StringVar()
EMAIL = StringVar()

# Title
Label(root, text="Contact Management", font=("Arial", 20, "bold"), bg="#f0f3f5").pack(pady=10)

# Form Frame
FormFrame = Frame(root, bg="#f0f3f5")
FormFrame.pack(pady=10)

Label(FormFrame, text="First Name:", font=("Arial", 12), bg="#f0f3f5").grid(row=0, column=0, padx=10, pady=5, sticky=W)
Entry(FormFrame, textvariable=FIRSTNAME, width=25).grid(row=0, column=1)

Label(FormFrame, text="Last Name:", font=("Arial", 12), bg="#f0f3f5").grid(row=1, column=0, padx=10, pady=5, sticky=W)
Entry(FormFrame, textvariable=LASTNAME, width=25).grid(row=1, column=1)

Label(FormFrame, text="Gender:", font=("Arial", 12), bg="#f0f3f5").grid(row=2, column=0, padx=10, pady=5, sticky=W)
ttk.Combobox(FormFrame, textvariable=GENDER, values=("Male", "Female", "Other"), width=22).grid(row=2, column=1)

Label(FormFrame, text="Phone:", font=("Arial", 12), bg="#f0f3f5").grid(row=0, column=2, padx=10, pady=5, sticky=W)
Entry(FormFrame, textvariable=PHONE, width=25).grid(row=0, column=3)

Label(FormFrame, text="Email:", font=("Arial", 12), bg="#f0f3f5").grid(row=1, column=2, padx=10, pady=5, sticky=W)
Entry(FormFrame, textvariable=EMAIL, width=25).grid(row=1, column=3)

# Buttons
ButtonFrame = Frame(root, bg="#f0f3f5")
ButtonFrame.pack(pady=10)

Button(ButtonFrame, text="Add", width=10, bg="#58d68d", command=SubmitData).grid(row=0, column=0, padx=5)
Button(ButtonFrame, text="Update", width=10, bg="#f7dc6f", command=UpdateData).grid(row=0, column=1, padx=5)
Button(ButtonFrame, text="Delete", width=10, bg="#ec7063", command=DeleteData).grid(row=0, column=2, padx=5)
Button(ButtonFrame, text="Clear", width=10, bg="#85c1e9", command=Reset).grid(row=0, column=3, padx=5)

# Table Frame
TableFrame = Frame(root)
TableFrame.pack(pady=10, fill=BOTH, expand=True)

scroll_y = Scrollbar(TableFrame, orient=VERTICAL)
tree = ttk.Treeview(TableFrame, columns=("ID", "First Name", "Last Name", "Gender", "Phone", "Email"),
                    yscrollcommand=scroll_y.set, show="headings")
scroll_y.config(command=tree.yview)
scroll_y.pack(side=RIGHT, fill=Y)

tree.heading("ID", text="ID")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Gender", text="Gender")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")

tree.column("ID", width=30)
tree.column("First Name", width=120)
tree.column("Last Name", width=120)
tree.column("Gender", width=80)
tree.column("Phone", width=120)
tree.column("Email", width=160)

tree.bind("<ButtonRelease-1>", OnSelect)
tree.pack(fill=BOTH, expand=True)

Database()
root.mainloop()
root.mainloop()
