import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """This opens a file for editing"""
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
        txt_edit.delete(1.0,tk.END)
        with open(filepath,"r") as input_file:
            text = input.file.read()
            text_edit.insert(tk.END, text)
        window.title()(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
        with open(filepath,"w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title("Simple Text Editor = {filepath}")

window = tk.TK()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Tk(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid()