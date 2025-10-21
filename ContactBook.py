
import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        root.title("Contact Book")
        root.geometry("500x400")
        root.configure(bg="#b2ebf2")
        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        labels = ["Name:", "Phone:", "Email:", "Address:"]
        self.entries = {}
        entry_width = 40
        label_font = ("Arial", 12, "bold")

        for i, label_text in enumerate(labels):
            tk.Label(self.root, text=label_text, bg="#b2ebf2", font=label_font, fg="black").grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=entry_width)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.entries[label_text[:-1].lower()] = entry  # Store entries for easier access

        self.entries['phone'].config(validate="key", validatecommand=(self.root.register(self.validate_phone), "%P"))

        button_font = ("Arial", 10)
        button_width = 12
        buttons = [
            ("Add", self.add_contact),
            ("View", self.view_contacts),
            ("Search", self.search_contact),
            ("Update", self.update_contact),
            ("Delete", self.delete_contact),
        ]

        for i, (text, command) in enumerate(buttons):
            tk.Button(self.root, text=text, font=button_font, width=button_width, command=command).grid(row=i + len(labels), column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def validate_phone(self, value):
        return all(char.isdigit() or char == "+" for char in value) or value == ""

    def add_contact(self):
        name = self.entries['name'].get()
        phone = self.entries['phone'].get()
        email = self.entries['email'].get()
        address = self.entries['address'].get()

        if not name or not phone:
            messagebox.showinfo("Error", "Name and Phone Number are mandatory fields.")
            return

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully.")
        self.clear_entries()

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
        else:
            contacts_info = "\n--------------\n".join(
                f"{i}. Name: {contact.name}\n   Phone: {contact.phone}\n   Email: {contact.email}\n   Address: {contact.address}"
                for i, contact in enumerate(self.contacts, start=1)
            )
            messagebox.showinfo("Contacts", contacts_info)

    def search_contact(self):
        self._process_contact_action("Search", self._search_contacts)

    def update_contact(self):
        self._process_contact_action("Update Contact", self._update_contacts)

    def delete_contact(self):
        self._process_contact_action("Delete Contact", self._delete_contacts)

    def _process_contact_action(self, title, action_function):
        search_term = simpledialog.askstring(title, f"Enter a letter of the name or any letter inside the name to {title.lower()}:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
            action_function(found_contacts, search_term)

    def _search_contacts(self, found_contacts, search_term):
        if not found_contacts:
            messagebox.showinfo("Info", "No matching contacts found.")
        else:
            contacts_info = "\n--------------\n".join(
                f"{i}. Name: {contact.name}\n   Phone: {contact.phone}\n   Email: {contact.email}\n   Address: {contact.address}"
                for i, contact in enumerate(found_contacts, start=1)
            )
            messagebox.showinfo("Matching Contacts", contacts_info)

    def _update_contacts(self, found_contacts, search_term):
        if not found_contacts:
            messagebox.showinfo("Info", "Contact not found.")
            return
        elif len(found_contacts) > 1:
            self._show_selection_window(found_contacts, "Select Contact to Update", self.update_contact_details)
        else:
            self.update_contact_details(found_contacts[0])

    def _delete_contacts(self, found_contacts, search_term):
        if not found_contacts:
            messagebox.showinfo("Info", "Contact not found.")
        else:
            if len(found_contacts) == 1:
                contact_to_delete = found_contacts[0]
                self.contacts.remove(contact_to_delete)
                messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                self._show_selection_window(found_contacts, "Select Contact to Delete", self._delete_selected_contact)

    def _show_selection_window(self, found_contacts, title, action_function):
        selection_window = tk.Toplevel(self.root)
        selection_window.title(title)

        listbox = tk.Listbox(selection_window, selectmode=tk.SINGLE, font=("Arial", 12))
        listbox.pack(fill=tk.BOTH, expand=True)

        for contact in found_contacts:
            listbox.insert(tk.END, f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}")

        action_button = tk.Button(selection_window, text=title.replace("to ", ""), font=("Arial", 10), command=lambda: self._handle_selection(listbox, found_contacts, action_function, selection_window))
        action_button.pack(pady=5)

    def _handle_selection(self, listbox, found_contacts, action_function, selection_window):
        selected_index = listbox.curselection()
        if selected_index:
            contact_to_act = found_contacts[selected_index[0]]
            if action_function == self._delete_selected_contact:
                action_function(contact_to_act)
            else:
                action_function(contact_to_act)
            selection_window.destroy()
        else:
            messagebox.showinfo("Info", "Please select a contact.")

    def update_contact_details(self, contact):
        fields_to_update = simpledialog.askstring("Update Contact", "Enter the fields you want to update (separated by commas, Example:, name, email, phone, address):")
        if fields_to_update:
            fields_to_update = [field.strip().lower() for field in fields_to_update.split(',')]
            updated_info = []
            for field in fields_to_update:
                if field in self.entries:
                    new_value = simpledialog.askstring("Update Contact", f"Enter new {field}:", initialvalue=getattr(contact, field))
                    if new_value:
                        setattr(contact, field, new_value)
                        updated_info.append(f"{field.capitalize()}: {new_value}")
                else:
                    messagebox.showinfo("Info", f"Invalid field '{field}' will be skipped.")
            if updated_info:
                messagebox.showinfo("Success", "Contact updated successfully.\nUpdated info:\n" + '\n'.join(updated_info))

    def _delete_selected_contact(self, contact_to_delete):
        self.contacts.remove(contact_to_delete)
        messagebox.showinfo("Success", "Contact deleted successfully.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()