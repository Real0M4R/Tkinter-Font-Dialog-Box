import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter.font import Font

class FontDialog(tk.Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback

        self.title("Choose Font")
        self.resizable(False, False)

        self.font_family = tk.StringVar(value="Arial")
        self.font_size = tk.IntVar(value=12)
        self.font_bold = tk.BooleanVar(value=False)
        self.font_italic = tk.BooleanVar(value=False)

        self.create_widgets()
        self.update_sample()

    def create_widgets(self):
        family_frame = ttk.LabelFrame(self, text="Font Family")
        family_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.family_listbox = tk.Listbox(family_frame, listvariable=tk.StringVar(value=sorted(font.families())), height=6)
        self.family_listbox.bind('<<ListboxSelect>>', self.update_sample)
        self.family_listbox.grid(row=0, column=0, padx=10, pady=10)

        size_frame = ttk.LabelFrame(self, text="Font Size")
        size_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.size_spinbox = tk.Spinbox(size_frame, from_=1, to=100, textvariable=self.font_size, command=self.update_sample)
        self.size_spinbox.grid(row=0, column=0, padx=10, pady=10)

        style_frame = ttk.LabelFrame(self, text="Font Style")
        style_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.bold_checkbutton = ttk.Checkbutton(style_frame, text="Bold", variable=self.font_bold, command=self.update_sample)
        self.bold_checkbutton.grid(row=0, column=0, padx=10, pady=10)

        self.italic_checkbutton = ttk.Checkbutton(style_frame, text="Italic", variable=self.font_italic, command=self.update_sample)
        self.italic_checkbutton.grid(row=0, column=1, padx=10, pady=10)

        self.sample_label = ttk.Label(self, text="Sample Text")
        self.sample_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button_frame = ttk.Frame(self)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.ok_button = ttk.Button(button_frame, text="OK", command=self.on_ok)
        self.ok_button.grid(row=0, column=0, padx=5)

        self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def update_sample(self, event=None):
        selected_family = self.family_listbox.get(self.family_listbox.curselection())
        self.font_family.set(selected_family)

        font_settings = Font(
            family=self.font_family.get(),
            size=self.font_size.get(),
            weight="bold" if self.font_bold.get() else "normal",
            slant="italic" if self.font_italic.get() else "roman"
        )

        self.sample_label.configure(font=font_settings)

    def on_ok(self):
        selected_font = Font(
            family=self.font_family.get(),
            size=self.font_size.get(),
            weight="bold" if self.font_bold.get() else "normal",
            slant="italic" if self.font_italic.get() else "roman"
        )
        self.callback(selected_font)
        self.destroy()

    def on_cancel(self):
        self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Font Dialog Example")
        self.geometry("400x200")

        self.label = ttk.Label(self, text="Sample Text")
        self.label.pack(pady=20)

        self.change_font_button = ttk.Button(self, text="Change Font", command=self.open_font_dialog)
        self.change_font_button.pack(pady=10)

    def open_font_dialog(self):
        FontDialog(self, self.apply_font)

    def apply_font(self, font):
        self.label.configure(font=font)

if __name__ == "__main__":
    app = App()
    app.mainloop()
