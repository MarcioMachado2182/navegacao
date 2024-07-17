import tkinter as tk

from controller.user_c import UsuarioController
from controller.delete_c import DeleteController
from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
from view.delete_v import DeleteView
from view.menu_v import MenuView

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("adicionar usuário")
        MenuView(self).pack(fill=tk.BOTH, expand=True)
        self.switch_frame(UsuarioView)
   
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if frame_class ==  UsuarioView:
            model =  UsuarioModel()
            UsuarioController(new_frame,model)
        elif frame_class == DeleteView:
            model =  UsuarioModel()
            DeleteController(new_frame, model)


        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()