import customtkinter as ctk
import tkinter as tk


class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")
        self.window.grab_set()
        self.window.resizable(False, False)

        self.window.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.window, text="Nombre:").grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")
        self.nombre_entry = ctk.CTkEntry(self.window, placeholder_text="Ej: Juan Pérez")
        self.nombre_entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.window, text="Edad:").grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
        self.edad_entry = ctk.CTkEntry(self.window, placeholder_text="Ej: 30")
        self.edad_entry.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.window, text="Género:").grid(row=4, column=0, padx=20, pady=(10, 0), sticky="w")
        self.genero_combobox = ctk.CTkComboBox(self.window, values=["Masculino", "Femenino", "Otro"])
        self.genero_combobox.set("Masculino")
        self.genero_combobox.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.window, text="Avatar:").grid(row=6, column=0, padx=20, pady=(10, 0), sticky="w")
        self.avatar_combobox = ctk.CTkComboBox(self.window, values=["avatar1.png", "avatar2.png"])
        self.avatar_combobox.set("avatar1.png")
        self.avatar_combobox.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.guardar_button = ctk.CTkButton(self.window, text="Guardar Usuario", fg_color="green")
        self.guardar_button.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

        cancelar_button = ctk.CTkButton(self.window, text="Cancelar", command=self.window.destroy, fg_color="gray")
        cancelar_button.grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")

    def get_data(self):
        return {
            'nombre': self.nombre_entry.get().strip(),
            'edad': self.edad_entry.get().strip(),
            'genero': self.genero_combobox.get(),
            'avatar': self.avatar_combobox.get()
        }


class EditUserView(AddUserView):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.window.title("Editar Usuario: " + usuario.nombre)
        self.guardar_button.configure(text="Aplicar Cambios", fg_color="darkblue")

        self.nombre_entry.delete(0, 'end')
        self.edad_entry.delete(0, 'end')

        self.nombre_entry.insert(0, usuario.nombre)
        self.edad_entry.insert(0, str(usuario.edad))
        self.genero_combobox.set(usuario.genero)
        self.avatar_combobox.set(usuario.avatar)


class MainView:
    def __init__(self, master):
        self.master = master

        self.crear_barra_menu()

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)

        self.lista_usuarios_frame = ctk.CTkFrame(master, corner_radius=0)
        self.lista_usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.lista_usuarios_frame.grid_columnconfigure(0, weight=1)

        self.add_button = ctk.CTkButton(self.lista_usuarios_frame, text="➕ Añadir Usuario", fg_color="blue")
        self.add_button.pack(fill="x", padx=10, pady=(10, 5))

        self.search_bar = ctk.CTkEntry(self.lista_usuarios_frame,
                                       placeholder_text="🔍 Buscar por nombre, edad o género...")
        self.search_bar.pack(fill="x", padx=10, pady=(5, 10))

        ctk.CTkLabel(self.lista_usuarios_frame, text="👥 Usuarios Registrados", font=ctk.CTkFont(weight="bold")).pack(
            pady=10)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.lista_usuarios_frame,
                                                                label_text="Lista de Usuarios")
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.lista_usuarios_scrollable.columnconfigure(0, weight=1)

        self.exit_button = ctk.CTkButton(self.lista_usuarios_frame, text="❌ Salir de la aplicación", fg_color="red")
        self.exit_button.pack(fill="x", padx=10, pady=(0, 10))

        self.detalles_frame = ctk.CTkFrame(master, corner_radius=0)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.detalles_frame.columnconfigure(0, weight=1)
        self.detalles_frame.columnconfigure(1, weight=1)
        self.detalles_frame.rowconfigure(2, weight=1)

        ctk.CTkLabel(self.detalles_frame, text="📋 Detalles del Usuario", font=ctk.CTkFont(size=18, weight="bold")).grid(
            row=0, column=0, pady=10, sticky="ew", columnspan=2)

        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="Avatar", width=200, height=200, corner_radius=5)
        self.avatar_label.grid(row=1, column=0, pady=10, columnspan=2)

        self.nombre_label = ctk.CTkLabel(self.detalles_frame, text="Nombre: -")
        self.nombre_label.grid(row=3, column=0, sticky="w", padx=20, pady=5, columnspan=2)

        self.edad_label = ctk.CTkLabel(self.detalles_frame, text="Edad: -")
        self.edad_label.grid(row=4, column=0, sticky="w", padx=20, pady=5, columnspan=2)

        self.genero_label = ctk.CTkLabel(self.detalles_frame, text="Género: -")
        self.genero_label.grid(row=5, column=0, sticky="w", padx=20, pady=5, columnspan=2)

        self.edit_button = ctk.CTkButton(self.detalles_frame, text="✏️ Editar", fg_color="orange", state="disabled")
        self.edit_button.grid(row=6, column=0, padx=10, pady=20, sticky="ew")

        self.delete_button = ctk.CTkButton(self.detalles_frame, text="🗑️ Eliminar", fg_color="darkred",
                                           state="disabled")
        self.delete_button.grid(row=6, column=1, padx=10, pady=20, sticky="ew")

        self.usuario_seleccionado = None

        self.status_bar = ctk.CTkLabel(master, text="Listo.", fg_color="gray", corner_radius=0, padx=10)
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")

    def crear_barra_menu(self):
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        self.menu_archivo = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.menu_archivo.add_command(label="Cargar usuarios (CSV)", command=lambda: None)
        self.menu_archivo.add_command(label="Guardar usuarios (CSV)", command=lambda: None)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Activar Auto-Guardado", command=lambda: None)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.master.quit)

        self.menu_ayuda = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=lambda: None)

    def configurar_comandos_menu(self, cargar_callback, guardar_callback, toggle_auto_save_callback,
                                 acerca_de_callback):
        self.menu_archivo.entryconfig(0, command=cargar_callback)
        self.menu_archivo.entryconfig(1, command=guardar_callback)
        self.menu_archivo.entryconfig(3, command=toggle_auto_save_callback)

        self.menu_ayuda.entryconfig(0, command=acerca_de_callback)

    def set_auto_save_menu_state(self, is_active: bool):
        label = "Desactivar Auto-Guardado" if is_active else "Activar Auto-Guardado"
        self.menu_archivo.entryconfig(3, label=label)

    def configurar_comandos_acciones(self, editar_callback, eliminar_callback):
        self.edit_button.configure(command=editar_callback)
        self.delete_button.configure(command=eliminar_callback)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                fg_color="transparent",
                hover_color="gray",
                anchor="w",
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def set_status_bar(self, texto):
        self.status_bar.configure(text=texto)

    def mostrar_detalles_usuario(self, usuario, ctk_image=None):
        self.usuario_seleccionado = usuario

        if usuario:
            self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
            self.edad_label.configure(text=f"Edad: {usuario.edad} años")
            self.genero_label.configure(text=f"Género: {usuario.genero}")

            if ctk_image:
                self.avatar_label.configure(image=ctk_image, text="")
            else:
                self.avatar_label.configure(image=None, text="Sin Avatar")

            self.edit_button.configure(state="normal")
            self.delete_button.configure(state="normal")

        else:
            self.nombre_label.configure(text="Nombre: -")
            self.edad_label.configure(text="Edad: -")
            self.genero_label.configure(text="Género: -")
            self.avatar_label.configure(image=None, text="Seleccione un usuario")

            self.edit_button.configure(state="disabled")
            self.delete_button.configure(state="disabled")