
class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero  # 'Masculino', 'Femenino', 'Otro'
        self.avatar = avatar  # Nombre del archivo del avatar (ej: 'avatar1.png')

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', edad={self.edad})"


class GestorUsuarios:

    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()
        self._usuario_seleccionado_indice = None

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 28, "Femenino", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 34, "Masculino", "avatar2.png"))
        self._usuarios.append(Usuario("Eli Smith", 22, "Otro", "avatar3.png"))

    def listar(self):
        return self._usuarios

    def get_usuario(self, indice: int) -> Usuario:
        if 0 <= indice < len(self._usuarios):
            self._usuario_seleccionado_indice = indice
            return self._usuarios[indice]
        return None

    def get_usuario_seleccionado_indice(self):
        return self._usuario_seleccionado_indice