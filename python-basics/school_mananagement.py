import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f4f6f7")

        self.students = []

        # ===== TITLE =====
        title = tk.Label(root,
                         text="SCHOOL MANAGEMENT SYSTEM",
                         font=("Arial", 20, "bold"),
                         bg="#1f618d",
                         fg="white")
        title.pack(fill="x")

        # ===== INPUT FRAME =====
        input_frame = tk.Frame(root, bg="#f4f6f7")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Student ID", bg="#f4f6f7").grid(row=0, column=0)
        self.id_entry = tk.Entry(input_frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="First Name", bg="#f4f6f7").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(input_frame)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Last Name", bg="#f4f6f7").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(input_frame)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Course", bg="#f4f6f7").grid(row=3, column=0)
        self.course_entry = tk.Entry(input_frame)
        self.course_entry.grid(row=3, column=1)

        tk.Label(input_frame, text="Phone Number", bg="#f4f6f7").grid(row=4, column=0)
        self.phone_entry = tk.Entry(input_frame)
        self.phone_entry.grid(row=4, column=1)

        tk.Button(input_frame,
                  text="Add Student",
                  command=self.add_student,
                  bg="green",
                  fg="white",
                  width=20).grid(row=5, columnspan=2, pady=10)

        # ===== TABLE =====
        self.tree = ttk.Treeview(root,
                                 columns=("ID", "First Name", "Last Name",
                                          "Course", "Phone"),
                                 show="headings")

        for col in ("ID", "First Name", "Last Name", "Course", "Phone"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # ===== UPDATE COURSE FRAME =====
        update_frame = tk.Frame(root, bg="#f4f6f7")
        update_frame.pack(pady=5)

        tk.Label(update_frame, text="New Course", bg="#f4f6f7").grid(row=0, column=0)
        self.new_course_entry = tk.Entry(update_frame)
        self.new_course_entry.grid(row=0, column=1)

        tk.Button(update_frame,
                  text="Assign / Update Course",
                  command=self.update_course,
                  bg="blue",
                  fg="white").grid(row=0, column=2, padx=10)

        # ===== EXPORT BUTTON =====
        tk.Button(root,
                  text="Export Students to Text File",
                  command=self.export_to_text,
                  bg="orange",
                  fg="black",
                  width=30).pack(pady=10)

    # ===== ADD STUDENT =====
    def add_student(self):
        student_id = self.id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        course = self.course_entry.get()
        phone = self.phone_entry.get()

        if not student_id or not first_name or not last_name or not course or not phone:
            messagebox.showerror("Error", "All fields are required!")
            return

        student = {
            "id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "course": course,
            "phone": phone
        }

        self.students.append(student)

        self.tree.insert("", "end",
                         values=(student_id, first_name,
                                 last_name, course, phone))

        self.clear_entries()

    # ===== UPDATE COURSE =====
    def update_course(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showerror("Error", "Select a student first!")
            return

        new_course = self.new_course_entry.get()

        if not new_course:
            messagebox.showerror("Error", "Enter new course!")
            return

        for item in selected:
            values = self.tree.item(item, "values")
            updated_values = (values[0], values[1],
                              values[2], new_course, values[4])
            self.tree.item(item, values=updated_values)

        self.new_course_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Course Updated Successfully!")

    # ===== EXPORT TO TEXT FILE =====
    def export_to_text(self):
        if not self.students:
            messagebox.showerror("Error", "No students to export!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_path:
            return

        with open(file_path, "w") as file:
            file.write("===== STUDENT REPORT =====\n\n")

            for student in self.tree.get_children():
                values = self.tree.item(student, "values")
                file.write(f"ID: {values[0]}\n")
                file.write(f"Name: {values[1]} {values[2]}\n")
                file.write(f"Course: {values[3]}\n")
                file.write(f"Phone: {values[4]}\n")
                file.write("--------------------------\n")

        messagebox.showinfo("Success", "Students Exported Successfully!")

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


# ===== RUN PROGRAM =====
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()


   # ===== DELETE STUDENT =====
def delete_student(self):
    selected = self.tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a student to delete!")
        return

    confirm = messagebox.askyesno("Confirm Delete",
                                   "Are you sure you want to delete this student?")

    if not confirm:
        return

    for item in selected:
        values = self.tree.item(item, "values")
        student_id = values[0]

        # Remove from internal list
        self.students = [student for student in self.students
                         if student["id"] != student_id]

        # Remove from table
        self.tree.delete(item)

    messagebox.showinfo("Deleted", "Student deleted successfully!") 