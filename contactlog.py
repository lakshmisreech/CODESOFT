import tkinter as tk
from tkinter import messagebox, Scrollbar
import re

class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.contacts = []

        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("800x700")
        self.root.resizable(False, False)

        # Create frames
        self.frame = tk.Frame(root)
        self.frame.pack(pady=15)

        self.contact_list_frame = tk.Frame(root)
        self.contact_list_frame.pack(pady=15)
        label_font = ('Arial')
        entry_font = ('Arial')
        button_font = ('Arial')


        # Contact Form
        tk.Label(self.frame, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Label(self.frame, text="Phone Number").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Label(self.frame, text="Email").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Label(self.frame, text="Address").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

        self.store_name = tk.Entry(self.frame, width=40)
        self.phone_number = tk.Entry(self.frame, width=40)
        self.email = tk.Entry(self.frame, width=40)
        self.address = tk.Entry(self.frame, width=40)

        self.store_name.grid(row=0, column=1, padx=5, pady=5)
        self.phone_number.grid(row=1, column=1, padx=5, pady=5)
        self.email.grid(row=2, column=1, padx=5, pady=5)
        self.address.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Contact", width=20, height=2, bg="#fe9037", fg="white", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2, pady=10)

        # Contact List with headings
        self.contact_listbox = tk.Listbox(self.contact_list_frame, width=85, height=20)
        self.contact_listbox.pack(pady=10, padx=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.show_contact_details)

        scrollbar = Scrollbar(self.contact_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contact_listbox.yview)

        # Column headings
        self.contact_listbox.insert(tk.END, f"{'Name':<20}{'Phone Number':<20}{'Email':<30}{'Address':<25}")
        self.contact_listbox.itemconfig(0, {'bg':'#fe9037', 'fg':'white'})

        # Buttons for actions
        self.view_button = tk.Button(self.contact_list_frame, text="View All Contacts", width=15, height=2, command=self.view_contacts)
        self.view_button.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.contact_list_frame, text="Search Contact", width=15, height=2, command=self.search_contact)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.contact_list_frame, text="Update Contact", width=15, height=2, command=self.update_contact)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.contact_list_frame, text="Delete Contact", width=15, height=2, command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_contact(self):
        store_name = self.store_name.get()
        phone_number = self.phone_number.get()
        email = self.email.get()
        address = self.address.get()

        if store_name and phone_number:
            if not re.fullmatch(r'\d{10}', phone_number):
                messagebox.showerror("Error", "Phone Number must contain exactly 10 digits.")
                return
            
            if '@' not in email:
                messagebox.showerror("Error", "Email must contain @ symbol.")
                return

            new_contact = Contact(store_name, phone_number, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_fields()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Store Name and Phone Number are required fields")

    def view_contacts(self):
        self.contact_listbox.delete(1, tk.END)  # Keep the header
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.store_name:<20}{contact.phone_number:<20}{contact.email:<30}{contact.address:<25}")

    def show_contact_details(self, event):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index and selected_contact_index[0] != 0:  # Ignore the header
            contact = self.contacts[selected_contact_index[0] - 1]
            self.store_name.delete(0, tk.END)
            self.store_name.insert(0, contact.store_name)
            self.phone_number.delete(0, tk.END)
            self.phone_number.insert(0, contact.phone_number)
            self.email.delete(0, tk.END)
            self.email.insert(0, contact.email)
            self.address.delete(0, tk.END)
            self.address.insert(0, contact.address)

    def search_contact(self):
        search_term = self.store_name.get() or self.phone_number.get() or self.email.get() 
        if search_term:
            matching_contacts = [contact for contact in self.contacts if
                                 search_term.lower() in contact.store_name.lower() or
                                 search_term in contact.phone_number or
                                 search_term.lower() in contact.email.lower()]
            self.contact_listbox.delete(1, tk.END)  # Keep the header
            for contact in matching_contacts:
                self.contact_listbox.insert(tk.END, f"{contact.store_name:<20}{contact.phone_number:<20}{contact.email:<30}{contact.address:<25}")
        else:
            messagebox.showerror("Error", "Please enter a name, phone number, email, or address to search")

    def update_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index and selected_contact_index[0] != 0:  # Ignore the header
            contact = self.contacts[selected_contact_index[0] - 1]
            contact.store_name = self.store_name.get()
            contact.phone_number = self.phone_number.get()
            contact.email = self.email.get()
            contact.address = self.address.get()
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_fields()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to update")

    def delete_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index and selected_contact_index[0] != 0:  # Ignore the header
            del self.contacts[selected_contact_index[0] - 1]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_fields()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def clear_fields(self):
        self.store_name.delete(0, tk.END)
        self.phone_number.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
