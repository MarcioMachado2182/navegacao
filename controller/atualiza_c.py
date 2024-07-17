from model.usuario_m import UsuarioModel
from view.atualiza_v import AtualizaView
import tkinter as tk


class AtualizaController:
    def __init__(self, view:AtualizaView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.atualizar_button.config(command=self.atualizar_usuario)
        self.carregar_usuarios()

    def atualizar_usuario(self):
        id = self.view.get_id()
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        if id and nome and idade.isdigit():
            self.model.atualizar_usuario(id,nome,idade)
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_usuarios()
        else:
            self.view.show_info()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()#retorna uma lista de tuplas
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)