import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")
        
        self.password_var = tk.StringVar()
        
        # Complexity options
        self.complexity_label = tk.Label(root, text="Select Complexity:")
        self.complexity_label.pack(pady=5)
        self.complexity_options = tk.StringVar(value="Medium")
        self.complexity_menu = tk.OptionMenu(root, self.complexity_options, "Low", "Medium", "High")
        self.complexity_menu.pack()
        
        # Security rules checkboxes
        self.security_label = tk.Label(root, text="Select Security Rules:")
        self.security_label.pack(pady=5)
        self.upper_case_var = tk.BooleanVar()
        self.upper_case_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=self.upper_case_var)
        self.upper_case_checkbox.pack()
        self.lower_case_var = tk.BooleanVar()
        self.lower_case_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=self.lower_case_var)
        self.lower_case_checkbox.pack()
        self.digits_var = tk.BooleanVar()
        self.digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=self.digits_var)
        self.digits_checkbox.pack()
        self.special_chars_var = tk.BooleanVar()
        self.special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_chars_var)
        self.special_chars_checkbox.pack()
        
        # Generate password button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        # Display generated password
        self.password_label = tk.Label(root, textvariable=self.password_var, font=("Helvetica", 14), wraplength=300)
        self.password_label.pack(pady=5)
        
        # Copy to clipboard button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
    
    def generate_password(self):
        complexity = self.complexity_options.get()
        length = 12  # Default length
        
        if complexity == "Low":
            length = 8
        elif complexity == "Medium":
            length = 12
        elif complexity == "High":
            length = 16
        
        chars = ""
        if self.upper_case_var.get():
            chars += string.ascii_uppercase
        if self.lower_case_var.get():
            chars += string.ascii_lowercase
        if self.digits_var.get():
            chars += string.digits
        if self.special_chars_var.get():
            chars += string.punctuation
        
        if chars:
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_var.set(password)
        else:
            self.password_var.set("Please select at least one option.")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
