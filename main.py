import tkinter as tk
import os
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = {}

    def check_book_existence(self, book_name):
        if os.path.exists(book_name):
            with open('Book_Info.txt', 'r') as file:
                for line in file:
                    book_info = line.strip().split('\t')
                    if len(book_info) >= 2 and book_info[1] == book_name:
                        return True
        return False

    def check_out_book(self, member_id, book_name):
        if not (0 <= member_id <= 999):
            return "Invalid Member ID"

        if not self.check_book_existence(book_name):
            return "Invalid Book Name"

        if book_name in self.books:
            return "Book is already checked out"

        self.books[book_name] = member_id
        return f"Book '{book_name}' checked out by Member {member_id}"

    def return_book(self, member_id, book_name):
        if not (0 <= member_id <= 999):
            return "Invalid Member ID"

        if book_name not in self.books or self.books[book_name] != member_id:
            return "Invalid Book Name or Member ID"

        del self.books[book_name]
        return f"Book '{book_name}' returned by Member {member_id}"

class GUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Library Management System")

        self.load_button = tk.Button(root, text="Load Books", command=self.check_book_existence)
        self.load_button.pack()

        self.checkout_label = tk.Label(root, text="Enter Member ID and Book Name to Checkout:")
        self.checkout_label.pack()

        self.member_id_entry = tk.Entry(root)
        self.member_id_entry.pack()

        self.book_name_entry = tk.Entry(root)
        self.book_name_entry.pack()

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout_book)
        self.checkout_button.pack()

        self.return_label = tk.Label(root, text="Enter Member ID and Book Name to Return:")
        self.return_label.pack()

        self.return_member_id_entry = tk.Entry(root)
        self.return_member_id_entry.pack()

        self.return_book_name_entry = tk.Entry(root)
        self.return_book_name_entry.pack()

        self.return_button = tk.Button(root, text="Return", command=self.return_book)
        self.return_button.pack()

    def check_book_existence(self):
        self.library.check_book_existence("Book_Info.txt")
        messagebox.showinfo("Info", "Books loaded from file.")

    def checkout_book(self):
        member_id = int(self.member_id_entry.get())
        book_name = self.book_name_entry.get()
        if self.library.check_out_book(member_id, book_name):
            messagebox.showinfo("Success", f"Book '{book_name}' checked out successfully.")
        else:
            messagebox.showerror("Error", "Invalid member ID or book not found.")

    def return_book(self):
        member_id = int(self.return_member_id_entry.get())
        book_name = self.return_book_name_entry.get()
        if self.library.return_book(member_id, book_name):
            messagebox.showinfo("Success", f"Book '{book_name}' returned to the library.")
        else:
            messagebox.showerror("Error", "Invalid member ID or book not found.")

if __name__ == "__main__":
    root = tk.Tk()
    library = Library()
    app = GUI(root, library)
    root.mainloop()

