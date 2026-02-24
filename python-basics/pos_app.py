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





# second app
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ModernPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f8f9fa")

        self.total_amount = 0

        self.setup_style()
        self.create_widgets()

    # ===== MODERN STYLE =====
    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#f8f9fa")
        style.configure("TLabel", background="#f8f9fa", font=("Segoe UI", 11))
        style.configure("TButton",
                        font=("Segoe UI", 11, "bold"),
                        padding=8)

        style.configure("Treeview",
                        font=("Segoe UI", 11),
                        rowheight=30)
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 12, "bold"))

    # ===== UI LAYOUT =====
    def create_widgets(self):

        # HEADER
        header = tk.Label(self.root,
                          text="SUPERMARKET POS SYSTEM",
                          font=("Segoe UI", 24, "bold"),
                          bg="#343a40",
                          fg="white",
                          pady=15)
        header.pack(fill="x")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # LEFT PANEL (INPUTS)
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="y", padx=10)

        ttk.Label(left_frame, text="Product Name").pack(anchor="w")
        self.product_entry = ttk.Entry(left_frame, width=25)
        self.product_entry.pack(pady=5)

        ttk.Label(left_frame, text="Price").pack(anchor="w")
        self.price_entry = ttk.Entry(left_frame, width=25)
        self.price_entry.pack(pady=5)

        ttk.Label(left_frame, text="Quantity").pack(anchor="w")
        self.qty_entry = ttk.Entry(left_frame, width=25)
        self.qty_entry.pack(pady=5)

        ttk.Button(left_frame, text="Add to Cart",
                   command=self.add_to_cart).pack(pady=15, fill="x")

        ttk.Button(left_frame, text="Clear Cart",
                   command=self.clear_cart).pack(pady=5, fill="x")

        # RIGHT PANEL (TABLE)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        columns = ("Product", "Price", "Qty", "Total")

        self.tree = ttk.Treeview(right_frame,
                                 columns=columns,
                                 show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # TOTAL DISPLAY
        self.total_label = tk.Label(self.root,
                                    text="Total: KSh 0.00",
                                    font=("Segoe UI", 18, "bold"),
                                    bg="#f8f9fa",
                                    fg="#dc3545")
        self.total_label.pack(pady=10)

        # CHECKOUT BUTTON
        checkout_btn = tk.Button(self.root,
                                 text="CHECKOUT",
                                 font=("Segoe UI", 14, "bold"),
                                 bg="#28a745",
                                 fg="white",
                                 padx=20,
                                 pady=10,
                                 command=self.checkout)
        checkout_btn.pack(pady=10)

    # ===== FUNCTIONS =====
    def add_to_cart(self):
        try:
            name = self.product_entry.get()
            price = float(self.price_entry.get())
            qty = int(self.qty_entry.get())

            total = price * qty

            self.tree.insert("", tk.END,
                             values=(name, f"{price:.2f}", qty, f"{total:.2f}"))

            self.total_amount += total
            self.update_total()

            self.product_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity")

    def clear_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.total_amount = 0
        self.update_total()

    def update_total(self):
        self.total_label.config(text=f"Total: KSh {self.total_amount:.2f}")

    def checkout(self):
        if self.total_amount == 0:
            messagebox.showinfo("Info", "Cart is empty")
            return

        receipt = f"===== RECEIPT =====\n"
        receipt += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            receipt += f"{values[0]} x{values[2]} - KSh {values[3]}\n"

        receipt += f"\nTotal: KSh {self.total_amount:.2f}"
        receipt += "\nThank you!"

        messagebox.showinfo("Receipt", receipt)
        self.clear_cart()


# RUN APP
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPOS(root)
    root.mainloop()