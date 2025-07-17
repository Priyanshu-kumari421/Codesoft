import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")  # More space

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    action = calculate if text == '=' else lambda t=text: click_button(t)
    tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
              command=action).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="Clear", font=("Arial", 18), bg="#f08080",
          command=clear_entry).grid(row=5, column=0, columnspan=4, sticky="we", padx=10, pady=10)

root.mainloop()
