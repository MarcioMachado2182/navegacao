from model.usuario_m import UsuarioModel
from view.delete_v import DeleteView
import tkinter as tk


class DeleteController:
    def __init__(self, view:DeleteView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.deletar_button.config(command=self.deletar_usuario)
        self.carregar_usuarios()

    def deletar_usuario(self):
        id = self.view.get_id()
        if id:
            self.model.deletar_usuario(id)
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_usuarios()
        else:
            self.view.show_info()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()#retorna uma lista de tuplas
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)