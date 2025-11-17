import customtkinter as ctk
class MainView:
    def __init__(self, master):
        self.master = master  # Ventana principal (ctk.CTk)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        master.grid_rowconfigure(0, weight=1)

        self.lista_usuarios_frame = ctk.CTkFrame(master, corner_radius=0)
        self.lista_usuarios_frame.grid(row=0, column=0, sticky="nsew")
        self.lista_usuarios_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.lista_usuarios_frame, text="👥 Usuarios Registrados", font=ctk.CTkFont(weight="bold")).pack(
            pady=10)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.lista_usuarios_frame,
                                                                label_text="Lista de Usuarios")
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.lista_usuarios_scrollable.columnconfigure(0, weight=1)

        self.detalles_frame = ctk.CTkFrame(master, corner_radius=0)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.detalles_frame.columnconfigure(0, weight=1)
        self.detalles_frame.rowconfigure(2, weight=1)

        ctk.CTkLabel(self.detalles_frame, text="📋 Detalles del Usuario", font=ctk.CTkFont(size=18, weight="bold")).grid(
            row=0, column=0, pady=10, sticky="ew")

        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="Avatar", width=200, height=200, corner_radius=5)
        self.avatar_label.grid(row=1, column=0, pady=10)

        self.nombre_label = ctk.CTkLabel(self.detalles_frame, text="Nombre: -")
        self.nombre_label.grid(row=3, column=0, sticky="w", padx=20, pady=5)

        self.edad_label = ctk.CTkLabel(self.detalles_frame, text="Edad: -")
        self.edad_label.grid(row=4, column=0, sticky="w", padx=20, pady=5)

        self.genero_label = ctk.CTkLabel(self.detalles_frame, text="Género: -")
        self.genero_label.grid(row=5, column=0, sticky="w", padx=20, pady=5)

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

    def mostrar_detalles_usuario(self, usuario):
        if usuario:
            self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
            self.edad_label.configure(text=f"Edad: {usuario.edad} años")
            self.genero_label.configure(text=f"Género: {usuario.genero}")

            self.avatar_label.configure(text=f"Avatar: {usuario.avatar}")
        else:
            self.nombre_label.configure(text="Nombre: -")
            self.edad_label.configure(text="Edad: -")
            self.genero_label.configure(text="Género: -")
            self.avatar_label.configure(text="Seleccione un usuario")