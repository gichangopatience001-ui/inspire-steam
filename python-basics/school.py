import tkinter as tk
from tkinter import messagebox, ttk

class SchoolSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.students = [] # Data storage

        # UI Layout
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.ent_name = tk.Entry(root)
        self.ent_name.grid(row=0, column=1)

        tk.Label(root, text="National ID:").grid(row=1, column=0)
        self.ent_id = tk.Entry(root)
        self.ent_id.grid(row=1, column=1)

        tk.Label(root, text="Course:").grid(row=2, column=0)
        self.ent_course = tk.Entry(root)
        self.ent_course.grid(row=2, column=1)

        tk.Button(root, text="Register", command=self.register).grid(row=3, column=0, columnspan=2)
        
        # Display Area
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Grade"), show='headings')
        self.tree.heading("ID", text="National ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Grade", text="Grade")
        self.tree.grid(row=4, column=0, columnspan=2)

    def register(self):
        data = {"id": self.ent_id.get(), "name": self.ent_name.get(), 
                "course": self.ent_course.get(), "grade": "N/A"}
        self.students.append(data)
        self.tree.insert("", "end", values=(data['id'], data['name'], data['course'], data['grade']))
        messagebox.showinfo("Success", "Student Registered!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolSystem(root)
    root.mainloop()



# Option 2
import tkinter as tk
from tkinter import messagebox, ttk

class SchoolSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.students = {} # Using a dict with ID as key for easier lookups

        # UI Input Fields
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.ent_name = tk.Entry(root); self.ent_name.grid(row=0, column=1)
        
        tk.Label(root, text="ID:").grid(row=1, column=0)
        self.ent_id = tk.Entry(root); self.ent_id.grid(row=1, column=1)
        
        tk.Label(root, text="Course:").grid(row=2, column=0)
        self.ent_course = tk.Entry(root); self.ent_course.grid(row=2, column=1)
        
        tk.Label(root, text="Grade:").grid(row=3, column=0)
        self.ent_grade = tk.Entry(root); self.ent_grade.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Register", command=self.register).grid(row=4, column=0)
        tk.Button(root, text="Update Record", command=self.update_student).grid(row=4, column=1)

        # Table
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Grade"), show='headings')
        for col in ("ID", "Name", "Course", "Grade"): self.tree.heading(col, text=col)
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def register(self):
        sid, name, course = self.ent_id.get(), self.ent_name.get(), self.ent_course.get()
        self.students[sid] = {"name": name, "course": course, "grade": "N/A"}
        self.tree.insert("", "end", values=(sid, name, course, "N/A"))

    def on_select(self, event):
        # Fill entries with data from selected row
        selected = self.tree.item(self.tree.focus())['values']
        if selected:
            self.ent_id.delete(0, tk.END); self.ent_id.insert(0, selected[0])
            self.ent_name.delete(0, tk.END); self.ent_name.insert(0, selected[1])
            self.ent_course.delete(0, tk.END); self.ent_course.insert(0, selected[2])
            self.ent_grade.delete(0, tk.END); self.ent_grade.insert(0, selected[3])

    def update_student(self):
        sid = self.ent_id.get()
        if sid in self.students:
            self.students[sid] = {"name": self.ent_name.get(), "course": self.ent_course.get(), "grade": self.ent_grade.get()}
            # Refresh Table
            for item in self.tree.get_children(): self.tree.delete(item)
            for s_id, data in self.students.items():
                self.tree.insert("", "end", values=(s_id, data['name'], data['course'], data['grade']))
        else:
            messagebox.showerror("Error", "Student ID not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolSystem(root)
    root.mainloop()    