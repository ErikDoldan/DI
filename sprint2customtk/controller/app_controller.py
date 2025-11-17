from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView
from pathlib import Path
from PIL import Image
import customtkinter as ctk
import tkinter.messagebox as messagebox


class AppController:
    def __init__(self, master):
        self.master = master

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.CSV_PATH = self.BASE_DIR / "usuarios.csv"
        self.avatar_images = {}

        self.modelo = GestorUsuarios(self.CSV_PATH)
        self.view = MainView(master)

        self.view.add_button.configure(command=self.abrir_ventana_añadir)
        self.view.exit_button.configure(command=master.quit)

        self.view.configurar_comandos_menu(
            cargar_callback=self.cargar_datos,
            guardar_callback=self.guardar_datos
        )

        self.refrescar_lista_usuarios()

        if self.modelo.listar():
            self.seleccionar_usuario(0)

    def cargar_datos(self):
        try:
            num_cargados = self.modelo.cargar_csv()
            self.refrescar_lista_usuarios()
            self.view.mostrar_detalles_usuario(None)
            messagebox.showinfo("Carga Exitosa", f"Se cargaron {num_cargados} usuarios desde {self.CSV_PATH.name}.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar los datos: {e}")

    def guardar_datos(self):
        try:
            num_guardados = self.modelo.guardar_csv()
            messagebox.showinfo("Guardado Exitoso", f"Se guardaron {num_guardados} usuarios en {self.CSV_PATH.name}.")
        except Exception as e:
            messagebox.showerror("Error de Guardado", f"No se pudieron guardar los datos: {e}")

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice: int):
        usuario = self.modelo.get_usuario(indice)
        ctk_image = None

        if usuario:
            try:
                image_path = self.ASSETS_PATH / usuario.avatar
                path_key = str(image_path)

                if path_key in self.avatar_images:
                    ctk_image = self.avatar_images[path_key]
                else:
                    pil_image = Image.open(image_path)
                    ctk_image = ctk.CTkImage(
                        light_image=pil_image, dark_image=pil_image, size=(200, 200)
                    )
                    self.avatar_images[path_key] = ctk_image

            except FileNotFoundError:
                messagebox.showwarning("Error de Avatar", f"No se encontró el archivo de avatar: {usuario.avatar}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al cargar la imagen: {e}")

            self.view.mostrar_detalles_usuario(usuario, ctk_image)
        else:
            self.view.mostrar_detalles_usuario(None)

    def abrir_ventana_añadir(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, ctk.CTkToplevel):
                widget.lift()
                return

        add_view = AddUserView(self.master)
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))

    def añadir_usuario(self, add_view: AddUserView):
        data = add_view.get_data()

        nombre = data['nombre']
        edad_str = data['edad']
        avatar = data['avatar'] or "avatar1.png"

        if not nombre:
            messagebox.showwarning("Error de Validación", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(edad_str)
            if not (1 <= edad <= 120):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error de Validación", "La edad debe ser un número entero válido (1-120).")
            return

        try:
            nuevo_usuario = Usuario(nombre, edad, data['genero'], avatar)
            self.modelo.agregar(nuevo_usuario)

            self.refrescar_lista_usuarios()
            add_view.window.destroy()
            self.seleccionar_usuario(len(self.modelo.listar()) - 1)

            messagebox.showinfo("Éxito", f"Usuario '{nombre}' añadido.")

        except Exception as e:
            messagebox.showerror("Error Interno", f"No se pudo guardar el usuario: {e}")