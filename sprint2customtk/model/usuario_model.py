import csv
from pathlib import Path


class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', edad={self.edad})"


class GestorUsuarios:
    def __init__(self, csv_path: Path):
        self._usuarios = []
        self.csv_path = csv_path
        self._usuario_seleccionado_indice = None
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        try:
            if self.csv_path.exists() and self.csv_path.stat().st_size > 0:
                self.cargar_csv()
                if self._usuarios:
                    return

        except Exception as e:
            print(f"Advertencia: Error al cargar CSV inicial ({e}). Usando datos de ejemplo.")

        self._usuarios.append(Usuario("Ana García", 28, "Femenino", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 34, "Masculino", "avatar2.png"))
        self._usuarios.append(Usuario("Eli Smith", 22, "Otro", "avatar1.png"))

    def cargar_csv(self):
        if not self.csv_path.exists() or self.csv_path.stat().st_size == 0:
            self._usuarios = []
            return 0

        nuevos_usuarios = []
        with open(self.csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    usuario = Usuario(
                        nombre=row['nombre'],
                        edad=int(row['edad']),
                        genero=row['genero'],
                        avatar=row['avatar']
                    )
                    nuevos_usuarios.append(usuario)
                except (ValueError, KeyError):
                    continue

        self._usuarios = nuevos_usuarios
        self._usuario_seleccionado_indice = None
        return len(self._usuarios)

    def guardar_csv(self):
        fieldnames = ['nombre', 'edad', 'genero', 'avatar']
        with open(self.csv_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for usuario in self._usuarios:
                writer.writerow({
                    'nombre': usuario.nombre,
                    'edad': usuario.edad,
                    'genero': usuario.genero,
                    'avatar': usuario.avatar
                })
        return len(self._usuarios)

    def listar(self):
        return self._usuarios

    def get_usuario(self, indice: int) -> Usuario:
        if 0 <= indice < len(self._usuarios):
            self._usuario_seleccionado_indice = indice
            return self._usuarios[indice]
        return None

    def get_usuario_seleccionado_indice(self):
        return self._usuario_seleccionado_indice

    def agregar(self, usuario):
        self._usuarios.append(usuario)

    def actualizar(self, indice: int, datos_actualizados: Usuario):
        if 0 <= indice < len(self._usuarios):
            self._usuarios[indice] = datos_actualizados
            return True
        return False

    def eliminar(self, indice: int):
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
            if self._usuario_seleccionado_indice == indice:
                self._usuario_seleccionado_indice = None
            elif self._usuario_seleccionado_indice is not None and self._usuario_seleccionado_indice > indice:
                self._usuario_seleccionado_indice -= 1
            return True
        return False

    def buscar_usuarios(self, filtro: str):
        if not filtro:
            return self._usuarios

        filtro = filtro.lower()
        return [
            u for u in self._usuarios
            if filtro in u.nombre.lower() or filtro in u.genero.lower() or filtro in str(u.edad)
        ]
