import tkinter as tk
from tkinter import ttk

def submit():
    print("Full Name: ", entry1.get())
    print("Email: ", entry2.get())
    print("Gender: ", gender.get())
    print("Country: ", country.get())
    print("Programming: ", java.get(), python.get())

window = tk.Tk()
window.title("Registration Form")

tk.Label(window, text="Registration Form", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)

tk.Label(window, text="Full Name").grid(row=1, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1)

tk.Label(window, text="Email").grid(row=2, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=2, column=1)

tk.Label(window, text="Gender").grid(row=3, column=0)
gender = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender, value="Male").grid(row=3, column=1)
tk.Radiobutton(window, text="Female", variable=gender, value="Female").grid(row=3, column=2)

tk.Label(window, text="Country").grid(row=5, column=0)
country = ttk.Combobox(window, values=["India", "USA", "UK", "Germany", "Austrailia"])
country.grid(row=5, column=1)

tk.Label(window, text="Programming").grid(row=6, column=0)
java = tk.IntVar()
python = tk.IntVar()
tk.Checkbutton(window, text="Java", variable=java).grid(row=6, column=1)
tk.Checkbutton(window, text="Python", variable=python).grid(row=6, column=2)

tk.Button(window, text="Submit",bg="red", fg="white", command=submit).grid(row=8, column=0, columnspan=1)

window.mainloop()