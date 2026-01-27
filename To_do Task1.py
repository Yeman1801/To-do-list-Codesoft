import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

tk1 = tk.Tk()
tk1.title("To-do-list")
tk1.geometry("760x510")

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview", font=("Segoe UI", 10, "bold"), background="white", foreground="#2c3e50",
                rowheight=30, fieldbackground="white")
style.configure("Treeview.Heading",background="#2563eb",foreground="black",font=("Segoe UI", 11, "bold"))

def time(t1, t2):
    s = datetime.strptime(t1, "%H:%M")
    e = datetime.strptime(t2, "%H:%M")
    if e <= s:
        return None
    return str(e - s)


def add():
    t, s, e = e1.get().strip().capitalize(), e2.get(), e3.get()
    if not t or not s or not e:
        return messagebox.showwarning("Warning", "All fields are required")
    d = time(s, e)
    if not d:
        return messagebox.showerror("Error", "Invalid time")
    tt2.insert("", tk.END, values=(t, s, e, d))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

def delete():
    sel = tt2.selection()
    if not sel:
        messagebox.showwarning("Warning", "Select task then delete")
        return
    for i in sel:
        tt2.delete(i)


def colon(event, box):
    v = ''.join(c for c in box.get() if c.isdigit())
    if len(v) > 2:
        v = v[:2] + ':' + v[2:4]
    box.delete(0, tk.END)
    box.insert(0, v)


t1 = tk.Label(tk1, text="To-Do List with Time Tracker", bg="#d8ebfd", fg="#2c3e50", font=("Segoe UI", 20, "bold"))
t1.pack()

l1 = tk.Label(tk1, text="Task-Name", font=("Arial", 14, "bold"))
l1.place(x=75, y=60)

l2 = tk.Label(tk1, text="Start-Time", font=("Arial", 14, "bold"))
l2.place(x=320, y=60)

l3 = tk.Label(tk1, text="End-Time", font=("Arial", 14, "bold"))
l3.place(x=560, y=60)


e1 = tk.Entry(tk1, width=30)
e1.place(x=40, y=100, height=30)

e2 = tk.Entry(tk1, width=30)
e2.place(x=280, y=100, height=30)
e2.bind("<KeyRelease>", lambda e: colon(e, e2))

e3 = tk.Entry(tk1, width=30)
e3.place(x=520, y=100, height=30)
e3.bind("<KeyRelease>", lambda e: colon(e, e3))


b1 = tk.Button(tk1, text="Add Task", command=add, font=("Arial", 12, "bold"))
b1.place(x=200, y=150)

b2 = tk.Button(tk1, text="Delete Task", command=delete, font=("Arial", 12, "bold"))
b2.place(x=400, y=150)


cols = ("Task", "Start", "End", "Duration")
tt2 = ttk.Treeview(tk1, columns=cols, show="headings")

for c in cols:
    tt2.heading(c, text=c)
    tt2.column(c, width=170)

tt2.place(x=40, y=190)

tk1.mainloop()
