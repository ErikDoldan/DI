from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView, EditUserView
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
        self.filtro_actual = ""

        self.modelo = GestorUsuarios(self.CSV_PATH)
        self.view = MainView(master)

        self.view.add_button.configure(command=self.abrir_ventana_añadir)
        self.view.exit_button.configure(command=master.quit)

        self.view.configurar_comandos_menu(
            cargar_callback=self.cargar_datos,
            guardar_callback=self.guardar_datos
        )
        self.view.configurar_comandos_acciones(
            editar_callback=self.abrir_ventana_editar,
            eliminar_callback=self.eliminar_usuario
        )

        self.view.search_bar.bind("<KeyRelease>", self.filtrar_usuarios)

        self.refrescar_lista_usuarios()

        if self.modelo.listar():
            self.seleccionar_usuario(0)

    def cargar_datos(self):
        try:
            num_cargados = self.modelo.cargar_csv()
            self.refrescar_lista_usuarios()
            self.view.mostrar_detalles_usuario(None)
            self.view.set_status_bar(f"Estado: Carga manual exitosa. Se cargaron {num_cargados} usuarios.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar los datos: {e}")
            self.view.set_status_bar("Estado: Error al cargar datos manualmente.")

    def guardar_datos(self):
        try:
            num_guardados = self.modelo.guardar_csv()
            self.view.set_status_bar(f"Estado: Guardado manual exitoso. Se guardaron {num_guardados} usuarios.")
        except Exception as e:
            messagebox.showerror("Error de Guardado", f"No se pudieron guardar los datos: {e}")
            self.view.set_status_bar("Estado: Error al guardar datos manualmente.")

    def filtrar_usuarios(self, event=None):
        nuevo_filtro = self.view.search_bar.get().strip()
        if nuevo_filtro != self.filtro_actual:
            self.filtro_actual = nuevo_filtro
            self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios_filtrados = self.modelo.buscar_usuarios(self.filtro_actual)
        self.view.actualizar_lista_usuarios(usuarios_filtrados, self.seleccionar_usuario_filtrado)

        if self.filtro_actual:
            self.view.set_status_bar(
                f"Estado: {len(usuarios_filtrados)} usuarios encontrados con el filtro '{self.filtro_actual}'.")
        elif not self.modelo.listar():
            self.view.set_status_bar("Estado: Lista de usuarios vacía.")

    def seleccionar_usuario_filtrado(self, indice_filtrado: int):
        usuarios_filtrados = self.modelo.buscar_usuarios(self.filtro_actual)
        if 0 <= indice_filtrado < len(usuarios_filtrados):
            usuario_seleccionado = usuarios_filtrados[indice_filtrado]

            try:
                indice_real = self.modelo.listar().index(usuario_seleccionado)
                self.seleccionar_usuario(indice_real)
            except ValueError:
                self.view.set_status_bar("Advertencia: El usuario seleccionado no se encuentra en la lista principal.")

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
                self.view.set_status_bar(f"Advertencia: Avatar '{usuario.avatar}' no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al cargar la imagen: {e}")

            self.view.mostrar_detalles_usuario(usuario, ctk_image)
            self.view.set_status_bar(f"Estado: Usuario '{usuario.nombre}' seleccionado.")
        else:
            self.view.mostrar_detalles_usuario(None)
            self.view.set_status_bar("Estado: Ningún usuario seleccionado.")

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

            self.view.set_status_bar(f"Estado: Usuario '{nombre}' añadido exitosamente.")

        except Exception as e:
            messagebox.showerror("Error Interno", f"No se pudo guardar el usuario: {e}")

    def abrir_ventana_editar(self):
        indice = self.modelo.get_usuario_seleccionado_indice()
        usuario = self.modelo.get_usuario(indice)

        if usuario is None:
            messagebox.showwarning("Error", "Debe seleccionar un usuario para editar.")
            return

        for widget in self.master.winfo_children():
            if isinstance(widget, ctk.CTkToplevel):
                widget.lift()
                return

        edit_view = EditUserView(self.master, usuario)
        edit_view.guardar_button.configure(
            command=lambda: self.editar_usuario(edit_view, indice)
        )
        self.view.set_status_bar(f"Estado: Editando usuario '{usuario.nombre}'.")

    def editar_usuario(self, edit_view: EditUserView, indice_original: int):
        data = edit_view.get_data()

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
            usuario_actualizado = Usuario(nombre, edad, data['genero'], avatar)

            self.modelo.actualizar(indice_original, usuario_actualizado)

            self.refrescar_lista_usuarios()
            edit_view.window.destroy()
            self.seleccionar_usuario(indice_original)

            self.view.set_status_bar(f"Estado: Usuario '{nombre}' actualizado exitosamente.")

        except Exception as e:
            messagebox.showerror("Error Interno", f"No se pudo actualizar el usuario: {e}")

    def eliminar_usuario(self):
        indice = self.modelo.get_usuario_seleccionado_indice()
        usuario = self.modelo.get_usuario(indice)

        if usuario is None:
            messagebox.showwarning("Error", "No hay usuario seleccionado para eliminar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Está seguro que desea eliminar a '{usuario.nombre}'?"
        )

        if confirmar:
            if self.modelo.eliminar(indice):
                nombre_eliminado = usuario.nombre

                self.filtro_actual = ""
                self.view.search_bar.delete(0, 'end')

                self.refrescar_lista_usuarios()
                self.view.mostrar_detalles_usuario(None)

                self.view.set_status_bar(f"Estado: Usuario '{nombre_eliminado}' eliminado exitosamente.")

                if self.modelo.listar():
                    self.seleccionar_usuario(0)
            else:
                messagebox.showerror("Error", "Error al eliminar el usuario del modelo.")