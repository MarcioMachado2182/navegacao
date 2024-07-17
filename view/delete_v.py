import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DeleteView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
       
        self.id_label = ttk.Label(self, text="ID que você quer deletar:")
        self.id_label.grid(row=1, column=0, padx=10, pady=5)
       
        self.id_entry = ttk.Entry(self)
        self.id_entry.grid(row=1, column=1, padx=10, pady=5)
       
        self.deletar_button = ttk.Button(self, text="deletar")
        self.deletar_button.grid(row=2, column=0, columnspan=2, pady=10)
       
        self.usuarios_listbox = tk.Listbox(self)
        self.usuarios_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
       
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def get_id(self):
        return self.id_entry.get()

    def adicionar_usuario_lista(self, usuario):
        self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")

    def show_info(self):
        messagebox.showinfo("Aviso!", "Os campos não podem estar vazios e a idade deve ser digito.")