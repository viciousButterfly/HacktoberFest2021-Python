import tkinter as tk

# Creating a GUI Window
window = tk.Tk()
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",tk.END)
    t1.insert(tk.END, ounce)
    t2.delete("1.0", tk.END)
    t2.insert(tk.END, pound)
    t3.delete("1.0", tk.END)
    t3.insert(tk.END, gram)

e1 = tk.Label(window, text="Weight in KG :")
e2_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e3 = tk.Label(window, text="Ounce")
e4 = tk.Label(window, text="Pound")
e5 = tk.Label(window, text="Gram")

t1 = tk.Text(window, height=5, width=30,border=3)
t2 = tk.Text(window, height=5, width=30,border=3)
t3 = tk.Text(window, height=5, width=30,border=3)

b1 = tk.Button(window, text="Convert", command=from_kg,border=2)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()