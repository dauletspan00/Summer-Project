import tkinter as tk
from tkinter import ttk

class Printer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multiple Inventory Tables")

    def create_table(self, items, title):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=title, font=('Arial', 16))
        label.pack()
        tree = ttk.Treeview(frame, columns=("ISBN", "Title", "Author", "Stock", "Price"), show='headings')
        tree.heading("ISBN", text="ISBN")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.heading("Stock", text="Stock")
        tree.heading("Price", text="Price")
        for item in items:
            tree.insert("", "end", values=(item.isbn, item.title, item.author, item.stock, item.price))

        scrollbar = ttk.Scrollbar(frame, orient = tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(expand=True, fill=tk.BOTH)
        frame.pack(pady=10)
    