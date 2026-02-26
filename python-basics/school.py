import tkinter as tk
from tkinter import messagebox, ttk

class SchoolSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("600x400")

        # --- Frames ---
        input_frame = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        # --- Input Widgets ---
        tk.Label(input_frame, text="Name:").grid(row=0, column=0)
        self.ent_name = tk.Entry(input_frame)
        self.ent_name.grid(row=0, column=1)

        tk.Label(input_frame, text="National ID:").grid(row=0, column=2, padx=5)
        self.ent_id = tk.Entry(input_frame)
        self.ent_id.grid(row=0, column=3)

        tk.Label(input_frame, text="Course:").grid(row=1, column=0)
        self.ent_course = tk.Entry(input_frame)
        self.ent_course.grid(row=1, column=1)

        tk.Label(input_frame, text="Grade:").grid(row=1, column=2, padx=5)
        self.ent_grade = tk.Entry(input_frame)
        self.ent_grade.grid(row=1, column=3)

        # --- Action Buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Add Student", command=self.add_student, bg="green", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update Selection", command=self.update_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=5)

        # --- Treeview Display ---
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Grade"), show='headings')
        for col in ("ID", "Name", "Course", "Grade"): self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def clear_fields(self):
        for entry in [self.ent_name, self.ent_id, self.ent_course, self.ent_grade]:
            entry.delete(0, tk.END)

    def add_student(self):
        if not self.ent_id.get():
            return messagebox.showwarning("Input Error", "National ID is required!")
        self.tree.insert("", "end", values=(self.ent_id.get(), self.ent_name.get(), self.ent_course.get(), self.ent_grade.get()))
        self.clear_fields()

    def on_select(self, event):
        selected = self.tree.focus()
        if selected:
            vals = self.tree.item(selected)['values']
            self.clear_fields()
            self.ent_id.insert(0, vals[0]); self.ent_name.insert(0, vals[1])
            self.ent_course.insert(0, vals[2]); self.ent_grade.insert(0, vals[3])

    def update_student(self):
        selected = self.tree.focus()
        if not selected:
            return messagebox.showwarning("Selection Error", "Please select a student from the list first.")
        self.tree.item(selected, values=(self.ent_id.get(), self.ent_name.get(), self.ent_course.get(), self.ent_grade.get()))
        messagebox.showinfo("Success", "Record Updated!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolSystem(root)
    root.mainloop()
