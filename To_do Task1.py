import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

tk1 = tk.Tk()
tk1.title("To-do-list")
tk1.geometry("760x510")

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview", font=("Segoe UI", 10, "bold"), rowheight=30)
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

def taskadd():
    t = e1.get().strip().capitalize()
    s, e = e2.get(), e3.get()
    if not all((t, s, e)):
        return messagebox.showwarning("Missing data", "All fields is required")
    d = time(s, e)
    if not d:
        return messagebox.showerror("Time error", "Invalid time (24 hours time)")
    tt2.insert("", tk.END, values=(t, s, e, d))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)



def time(t1, t2):
    s = datetime.strptime(t1, "%H:%M")
    e = datetime.strptime(t2, "%H:%M")
    if e <= s:
        return None
    return str(e - s)


def taskdelete():
    sel = tt2.selection()
    if not sel:
        messagebox.showwarning("Not Selection", "Select task then delete")
        return
    for i in sel:
        tt2.delete(i)


def colon(event, box):
    v = ""
    for c in box.get():
        if c.isdigit():
            v += c
    if len(v) > 2:
        v = v[:2] + ":" + v[2:4]
    box.delete(0, tk.END)
    box.insert(0, v)

button = {"font": ("bold", 13), "bd": 4, "relief": "solid"}

t1 = tk.Label(tk1, text="To-Do-list with Time traker", bg="#d8ebfd", font=("Segoe UI", 20, "bold"))
t1.pack()

l1 = tk.Label(tk1, text="Task-Name", font=("Arial", 14, "bold"))
l1.place(x=75, y=60)
l2 = tk.Label(tk1, text="Start-Time", font=("Arial", 14, "bold"))
l2.place(x=320, y=60)
l3 = tk.Label(tk1, text="End-Time", font=("Arial", 14, "bold"))
l3.place(x=560, y=60)

enter = {"width" : 30, "bd": 4, "relief": "solid"}

e1 = tk.Entry(tk1, **enter)
e1.place(x=40, y=100, height=30)

e2 = tk.Entry(tk1, **enter)
e2.place(x=280, y=100, height=30)
e2.bind("<KeyRelease>", lambda e: colon(e, e2))

e3 = tk.Entry(tk1, **enter)
e3.place(x=520, y=100, height=30)
e3.bind("<KeyRelease>", lambda e: colon(e, e3))


b1 = tk.Button(tk1, text="Add Task", command=taskadd, **button)
b1.place(x=200, y=140)

b2 = tk.Button(tk1, text="Delete Task", command=taskdelete, **button)
b2.place(x=400, y=140)


cols = ("Task", "Start", "End", "Duration")
tt2 = ttk.Treeview(tk1, columns=cols, show="headings")

for c in cols:
    tt2.heading(c, text=c)
    tt2.column(c, width=170)

tt2.place(x=40, y=190)

tk1.mainloop()
