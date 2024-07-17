import tkinter as tk

from view.user_v import UsuarioView
from view.delete_v import DeleteView


class MenuView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def opcao_selecionada(self, opcao):
        if opcao == "1":
            self.master.switch_frame(UsuarioView)
            self.master.title("adicionar usuário")
        elif opcao == "2":
            self.master.switch_frame(UsuarioView)
            self.master.title("atualizar usuário")
        elif opcao == "3":
            self.master.switch_frame(DeleteView)
            self.master.title("deletar usuário")

    def criar_menu_dropdown(self, master):
        menu_dropdown = tk.Menu(master, tearoff=0)
        menu_dropdown.add_command(label="adicionar usuário", command=lambda: self.opcao_selecionada("1"))
        menu_dropdown.add_command(label="atualizar usuário", command=lambda: self.opcao_selecionada("2"))
        menu_dropdown.add_command(label="deletar usuário", command=lambda: self.opcao_selecionada("3"))
        return menu_dropdown

    def create_widgets(self):
        mb = tk.Menubutton(self, text="Escolha uma opção", relief=tk.RAISED)
        mb.menu = self.criar_menu_dropdown(mb)
        mb["menu"] = mb.menu
        mb.pack(anchor="e", pady=12, padx=12)
