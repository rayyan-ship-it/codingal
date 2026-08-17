import tkinter as tk

root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("600x500")
root.configure(bg="#e8f0f7")
tk.Label(root, text="ATM PIN Setup", font=("Arial", 22, "bold"),
         bg="#e8f0f7").place(x=210, y=20)
frame = tk.Frame(root, bg="white", bd=3, relief="raised")
frame.place(x=40, y=80, width=350, height=190)

tk.Label(frame, text="Account Details", font=("Arial", 14, "bold"),
         bg="white").pack(pady=8)

tk.Label(frame, text="Account No.", bg="white").place(x=20, y=55)
account = tk.Entry(frame, bd=2, relief="sunken")
account.place(x=110, y=55)

tk.Label(frame, text="Name", bg="white").place(x=20, y=90)
name = tk.Entry(frame, bd=2, relief="sunken")
name.place(x=110, y=90)

tk.Label(frame, text="PIN", bg="white").place(x=20, y=125)
pin = tk.Entry(frame, show="*", bd=2, relief="sunken")
pin.place(x=110, y=125)
keypad = tk.Frame(root, bg="#d9e6f2", bd=3, relief="sunken")
keypad.place(x=410, y=80, width=150, height=190)

def add(n):
    pin.insert(tk.END, n)

for i in range(10):
    tk.Button(keypad, text=str(i), width=3,
              command=lambda n=i: add(n)).grid(
                  row=i//3, column=i%3, padx=3, pady=3)

# Output
output = tk.Text(root, width=60, height=8, bd=2, relief="sunken")
output.place(x=40, y=330)

def submit():
    output.delete("1.0", tk.END)
    output.insert(tk.END,
        f"Account No: {account.get()}\n"
        f"Name: {name.get()}\n"
        f"PIN: {pin.get()}")

tk.Button(root, text="Submit", font=("Arial", 11, "bold"),
          command=submit, bg="#1976d2", fg="white",
          relief="raised").place(x=250, y=285, width=100, height=35)

root.mainloop()
