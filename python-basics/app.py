#Name : Patience Mukuhi Gichango 
#Date : 24/02/2026
# Program to perform file operations in python 

from tkinter import * 

def hello():
    print("Hello from Joey")

root = Tk()
root.geometry("600x600") 

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text="Say Hello",command = hello)
button_one.pack()
root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SupermarketPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f4f4f4")

        self.cart = []
        self.total_amount = 0

        self.create_widgets()

    def create_widgets(self):

        # ===== TITLE =====
        title = tk.Label(self.root, text="SUPERMARKET POS SYSTEM",
                         font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        title.pack(fill=tk.X)

        # ===== INPUT FRAME =====
        input_frame = tk.Frame(self.root, bg="#f4f4f4")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Product Name:", bg="#f4f4f4").grid(row=0, column=0, padx=5, pady=5)
        self.product_name = tk.Entry(input_frame)
        self.product_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Price:", bg="#f4f4f4").grid(row=0, column=2, padx=5, pady=5)
        self.price = tk.Entry(input_frame)
        self.price.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:", bg="#f4f4f4").grid(row=0, column=4, padx=5, pady=5)
        self.quantity = tk.Entry(input_frame)
        self.quantity.grid(row=0, column=5, padx=5, pady=5)

        add_btn = tk.Button(input_frame, text="Add to Cart",
                            bg="#27ae60", fg="white",
                            command=self.add_to_cart)
        add_btn.grid(row=0, column=6, padx=10)

        # ===== CART TABLE =====
        columns = ("Product", "Price", "Quantity", "Total")

        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(pady=20)

        # ===== TOTAL DISPLAY =====
        self.total_label = tk.Label(self.root, text="Total: KSh 0.00",
                                    font=("Arial", 16, "bold"),
                                    bg="#f4f4f4", fg="#c0392b")
        self.total_label.pack()

        # ===== BUTTONS =====
        btn_frame = tk.Frame(self.root, bg="#f4f4f4")
        btn_frame.pack(pady=10)

        remove_btn = tk.Button(btn_frame, text="Remove Selected",
                               bg="#e74c3c", fg="white",
                               command=self.remove_item)
        remove_btn.grid(row=0, column=0, padx=10)

        checkout_btn = tk.Button(btn_frame, text="Checkout",
                                 bg="#2980b9", fg="white",
                                 command=self.checkout)
        checkout_btn.grid(row=0, column=1, padx=10)

        clear_btn = tk.Button(btn_frame, text="Clear Cart",
                              bg="#7f8c8d", fg="white",
                              command=self.clear_cart)
        clear_btn.grid(row=0, column=2, padx=10)

    # ===== FUNCTIONS =====
    def add_to_cart(self):
        try:
            name = self.product_name.get()
            price = float(self.price.get())
            quantity = int(self.quantity.get())

            if name == "":
                messagebox.showerror("Error", "Product name required")
                return

            total = price * quantity
            self.cart.append((name, price, quantity, total))

            self.tree.insert("", tk.END, values=(name, price, quantity, total))

            self.total_amount += total
            self.update_total()

            self.product_name.delete(0, tk.END)
            self.price.delete(0, tk.END)
            self.quantity.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity")

    def remove_item(self):
        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            values = self.tree.item(item, "values")
            self.total_amount -= float(values[3])
            self.tree.delete(item)

        self.update_total()

    def clear_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.cart.clear()
        self.total_amount = 0
        self.update_total()

    def update_total(self):
        self.total_label.config(text=f"Total: KSh {self.total_amount:.2f}")

    def checkout(self):
        if self.total_amount == 0:
            messagebox.showinfo("Info", "Cart is empty")
            return

        receipt = f"===== SUPERMARKET RECEIPT =====\n"
        receipt += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            receipt += f"{values[0]} x{values[2]} - KSh {values[3]}\n"

        receipt += f"\nTotal: KSh {self.total_amount:.2f}\n"
        receipt += "Thank you for shopping!"

        messagebox.showinfo("Receipt", receipt)
        self.clear_cart()


# ===== RUN APP =====
if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketPOS(root)
    root.mainloop()

