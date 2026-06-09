import tkinter as tk
from tkinter import ttk, messagebox
import DatabaseEngine as db

class JobTrackerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Application Tracker Core")
        self.root.geometry("850x500")
        self.root.configure(bg="#121212") # Clean modern dark theme backing
        
        # Initialize Database file framework
        db.initialize_database()

        # Define sleek corporate styling configs
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1e1e1e", fieldbackground="#1e1e1e", foreground="#ffffff", rowheight=25)
        style.map("Treeview", background=[("selected", "#007acc")])

        # --- LEFT PANEL: ENTRY FORM ---
        form_frame = tk.Frame(root, bg="#1a1a1a", bd=1, relief="solid")
        form_frame.pack(side="left", fill="y", padx=15, pady=15)
        
        form_title = tk.Label(form_frame, text="Log New Application", font=("Consolas", 12, "bold"), fg="#00ff00", bg="#1a1a1a")
        form_title.pack(pady=15, padx=20)

        # Inputs Fields
        tk.Label(form_frame, text="Company Name:", fg="#ffffff", bg="#1a1a1a", font=("Consolas", 10)).pack(anchor="w", padx=15)
        self.company_ent = tk.Entry(form_frame, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0)
        self.company_ent.pack(fill="x", padx=15, pady=(2, 10))

        tk.Label(form_frame, text="Job Role/Title:", fg="#ffffff", bg="#1a1a1a", font=("Consolas", 10)).pack(anchor="w", padx=15)
        self.role_ent = tk.Entry(form_frame, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0)
        self.role_ent.pack(fill="x", padx=15, pady=(2, 10))

        tk.Label(form_frame, text="Application Status:", fg="#ffffff", bg="#1a1a1a", font=("Consolas", 10)).pack(anchor="w", padx=15)
        self.status_box = ttk.Combobox(form_frame, values=["Applied", "Interview Scheduled", "Offer Received", "Rejected"], state="readonly")
        self.status_box.set("Applied")
        self.status_box.pack(fill="x", padx=15, pady=(2, 10))

        tk.Label(form_frame, text="Interview Date (YYYY-MM-DD):", fg="#ffffff", bg="#1a1a1a", font=("Consolas", 10)).pack(anchor="w", padx=15)
        self.date_ent = tk.Entry(form_frame, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0)
        self.date_ent.pack(fill="x", padx=15, pady=(2, 10))

        # Submit Action Button
        submit_btn = tk.Button(form_frame, text="SAVE APPLICATION", bg="#00ff00", fg="#000000", font=("Consolas", 10, "bold"), bd=0, activebackground="#00cc00", command=self.save_record)
        submit_btn.pack(fill="x", padx=15, pady=20)

        # --- RIGHT PANEL: LIVE DATABASE VIEW ---
        view_frame = tk.Frame(root, bg="#121212")
        view_frame.pack(side="right", fill="both", expand=True, padx=(0, 15), pady=15)

        # Table Layout Columns
        columns = ("id", "company", "role", "status", "date")
        self.table = ttk.Treeview(view_frame, columns=columns, show="headings")
        
        self.table.heading("id", text="ID")
        self.table.heading("company", text="Company")
        self.table.heading("role", text="Role")
        self.table.heading("status", text="Status")
        self.table.heading("date", text="Interview Date")

        self.table.column("id", width=40, anchor="center")
        self.table.column("company", width=150, anchor="w")
        self.table.column("role", width=150, anchor="w")
        self.table.column("status", width=130, anchor="center")
        self.table.column("date", width=120, anchor="center")
        
        self.table.pack(fill="both", expand=True, pady=(0, 10))

        # Action Execution Tray Block
        btn_tray = tk.Frame(view_frame, bg="#121212")
        btn_tray.pack(fill="x")

        delete_btn = tk.Button(btn_tray, text="DELETE SELECTED ROLE", bg="#ff3333", fg="#ffffff", font=("Consolas", 9, "bold"), bd=0, command=self.delete_record)
        delete_btn.pack(side="right", padx=5)

        self.refresh_table_view()

    def save_record(self):
        company = self.company_ent.get().strip()
        role = self.role_ent.get().strip()
        status = self.status_box.get()
        date = self.date_ent.get().strip()

        if not company or not role:
            messagebox.showwarning("Validation Error", "Company Name and Job Role fields cannot be left blank!")
            return

        db.add_application(company, role, status, date)
        
        # Clear fields for the next entry layout allocation
        self.company_ent.delete(0, tk.END)
        self.role_ent.delete(0, tk.END)
        self.date_ent.delete(0, tk.END)
        self.status_box.set("Applied")

        self.refresh_table_view()
        messagebox.showinfo("Success", "Application metrics saved securely to SQL layer.")

    def refresh_table_view(self):
        # Clear existing visual table elements
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Reload fresh values from internal database connection stream
        for row in db.fetch_all_applications():
            # row structure: (id, company, role, status, interview_date, notes)
            self.table.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))

    def delete_record(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please highlight an application row from the data table first.")
            return

        item_values = self.table.item(selected_item, 'values')
        record_id = item_values[0]

        if messagebox.askyesno("Confirm Deletion", f"Permanently wipe application entry ID {record_id} from SQL archive?"):
            db.delete_application(record_id)
            self.refresh_table_view()

if __name__ == "__main__":
    main_window = tk.Tk()
    app = JobTrackerDashboard(main_window)
    main_window.mainloop()