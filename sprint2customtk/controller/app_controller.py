from model.usuario_model import GestorUsuarios
from view.main_view import MainView
class AppController:

    def __init__(self, master):
        self.master = master
        self.modelo = GestorUsuarios()
        self.view = MainView(master)

        self.refrescar_lista_usuarios()

        self.seleccionar_usuario(0)

    def refrescar_lista_usuarios(self):

        usuarios = self.modelo.listar()

        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice: int):

        usuario = self.modelo.get_usuario(indice)
        if usuario:
            self.view.mostrar_detalles_usuario(usuario)