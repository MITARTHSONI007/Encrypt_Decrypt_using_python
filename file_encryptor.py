import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_key():
    key = Fernet.generate_key()
    key_file = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key")])
    if key_file:
        with open(key_file, 'wb') as f:
            f.write(key)
        key_label.config(text=f"Key saved to: {key_file}")

def load_key():
    key_file = filedialog.askopenfilename(filetypes=[("Key files", "*.key")])
    if key_file:
        with open(key_file, 'rb') as f:
            global key
            key = f.read()
        key_label.config(text=f"Key loaded from: {key_file}")

def encrypt_file():
    if not key:
        messagebox.showerror("Error", "Please load or generate a key first.")
        return
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted files", "*.enc")])
        if save_path:
            with open(save_path, 'wb') as f:
                f.write(encrypted)
            messagebox.showinfo("Success", f"File encrypted and saved to: {save_path}")

def decrypt_file():
    if not key:
        messagebox.showerror("Error", "Please load or generate a key first.")
        return
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if file_path:
        with open(file_path, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)
            save_path = filedialog.asksaveasfilename()
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(decrypted)
                messagebox.showinfo("Success", f"File decrypted and saved to: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

key = None

root = tk.Tk()
root.title("File Encryptor/Decryptor")

frame = tk.Frame(root)
frame.pack(pady=20)

key_label = tk.Label(frame, text="No key loaded")
key_label.grid(row=0, column=0, columnspan=2)

generate_key_button = tk.Button(frame, text="Generate New Key", command=generate_key)
generate_key_button.grid(row=1, column=0)

load_key_button = tk.Button(frame, text="Load Encryption Key", command=load_key)
load_key_button.grid(row=1, column=1)

encrypt_button = tk.Button(frame, text="Encrypt File", command=encrypt_file)
encrypt_button.grid(row=2, column=0, pady=10)

decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt_file)
decrypt_button.grid(row=2, column=1, pady=10)

root.mainloop()
