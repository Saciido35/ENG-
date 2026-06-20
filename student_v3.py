
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- DATABASE ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

cursor = db.cursor()

# ---------------- LOGIN ----------------
def login():
    user = username_var.get()
    pw = password_var.get()

    if user == "admin" and pw == "1234":
        login_frame.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Wrong Username or Password")

# ---------------- DASHBOARD FUNCTIONS ----------------
def load_students():
    for row in table.get_children():
        table.delete(row)

    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        table.insert("", "end", values=row)

    update_stats()

def add_student():
    if name_var.get()=="" or age_var.get()=="" or dept_var.get()=="":
        messagebox.showerror("Error", "Fill all fields")
        return

    sql = "INSERT INTO students(name, age, department) VALUES(%s,%s,%s)"
    val = (name_var.get(), age_var.get(), dept_var.get())

    cursor.execute(sql, val)
    db.commit()

    clear()
    load_students()
    messagebox.showinfo("Success", "Student Added")

def update_student():
    selected = table.focus()
    if not selected:
        return

    data = table.item(selected)["values"]

    sql = "UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s"
    val = (name_var.get(), age_var.get(), dept_var.get(), data[0])

    cursor.execute(sql, val)
    db.commit()

    clear()
    load_students()
    
   

def delete_student():
    selected = table.focus()
    if not selected:
        return

    data = table.item(selected)["values"]

    cursor.execute("DELETE FROM students WHERE id=%s", (data[0],))
    db.commit()

    clear()
    load_students()

def clear():
    name_var.set("")
    age_var.set("")
    dept_var.set("")

def select(event):
    selected = table.focus()
    if selected:
        data = table.item(selected)["values"]
        name_var.set(data[1])
        age_var.set(data[2])
        dept_var.set(data[3])

def update_stats():
    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]
    stats_label.config(text=f"Total Students: {total}")

# ---------------- DASHBOARD UI ----------------
def open_dashboard():

    global name_var, age_var, dept_var, table, stats_label

    root.title("Student Dashboard")
    root.geometry("1000x600")
    root.configure(bg="#0b0f18")

    # SIDEBAR
    sidebar = tk.Frame(root, bg="#1e293b", width=200)
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="ADMIN PANEL",
             bg="#1e293b", fg="white",
             font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(sidebar, text="Load",
              bg="#38bdf8", command=load_students).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Clear",
              bg="#f97316", command=clear).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Exit",
              bg="#ef4444", command=root.quit).pack(fill="x", pady=5)

    # MAIN
    main = tk.Frame(root, bg="#0f172a")
    main.pack(side="left", fill="both", expand=True)

    tk.Label(main, text="Student Management System",
             bg="#0f172a", fg="white",
             font=("Arial", 20, "bold")).pack(pady=10)

    # STATS
    stats_label = tk.Label(main, text="Total Students: 0",
                           bg="#0f172a", fg="#22c55e",
                           font=("Arial", 14, "bold"))
    stats_label.pack()

    # FORM
    form = tk.Frame(main, bg="#0f172a")
    form.pack(pady=10)

    name_var = tk.StringVar()
    age_var = tk.StringVar()
    dept_var = tk.StringVar()

    tk.Label(form, text="Name", bg="#0f172a", fg="white").grid(row=0, column=0)
    tk.Entry(form, textvariable=name_var).grid(row=0, column=1)

    tk.Label(form, text="Age", bg="#0f172a", fg="white").grid(row=0, column=2)
    tk.Entry(form, textvariable=age_var).grid(row=0, column=3)

    tk.Label(form, text="Dept", bg="#0f172a", fg="white").grid(row=0, column=4)
    tk.Entry(form, textvariable=dept_var).grid(row=0, column=5)

    # BUTTONS
    btn = tk.Frame(main, bg="#0f172a")
    btn.pack()

    tk.Button(btn, text="Add", bg="#22c55e", command=add_student).grid(row=0, column=0)
    tk.Button(btn, text="Update", bg="#eab308", command=update_student).grid(row=0, column=1)
    tk.Button(btn, text="Delete", bg="#ef4444", command=delete_student).grid(row=0, column=2)

    # TABLE
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="#1e293b",
                    foreground="white",
                    fieldbackground="#1e293b")

    table = ttk.Treeview(main,
                         columns=("ID","Name","Age","Department"),
                         show="headings")

    for col in ("ID","Name","Age","Department"):
        table.heading(col, text=col)

    table.pack(fill="both", expand=True, pady=20)

    table.bind("<ButtonRelease-1>", select)

    load_students()

# ---------------- LOGIN UI ----------------
root = tk.Tk()

login_frame = tk.Frame(root, bg="#0f172a")
login_frame.pack(fill="both", expand=True)

username_var = tk.StringVar()
password_var = tk.StringVar()

tk.Label(login_frame, text="LOGIN",
         font=("Arial", 20, "bold"),
         fg="white", bg="#0f172a").pack(pady=20)

tk.Entry(login_frame, textvariable=username_var,
         width=30).pack(pady=5)

tk.Entry(login_frame, textvariable=password_var,
         show="*",
         width=30).pack(pady=5)

tk.Button(login_frame, text="Login",
          bg="#38bdf8", command=login).pack(pady=10)

root.mainloop()