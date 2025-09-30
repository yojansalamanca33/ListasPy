
import tkinter as tk
from tkinter import messagebox

class FrmUsuarios(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Usuarios")
        self.geometry("400x400")

        
        self.lista_usuarios = []

        
        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Apellido:").pack()
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.pack()

        tk.Label(self, text="Email:").pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()

        tk.Label(self, text="Clave:").pack()
        self.entry_clave = tk.Entry(self, show="*")
        self.entry_clave.pack()

        
        tk.Button(self, text="Guardar", command=self.guardar_usuario).pack(pady=5)
        tk.Button(self, text="Listar", command=self.listar_usuarios).pack(pady=5)

        
        self.text_area = tk.Text(self, height=10, width=40)
        self.text_area.pack(pady=10)

    def guardar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email.get()
        clave = self.entry_clave.get()

        if not nombre or not apellido or not email or not clave:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        usuario = f"{nombre} {apellido} | {email} | {clave}"
        self.lista_usuarios.append(usuario)

        messagebox.showinfo("Éxito", "Usuario guardado correctamente")

        
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_clave.delete(0, tk.END)

    def listar_usuarios(self):
        self.text_area.delete("1.0", tk.END)
        for u in self.lista_usuarios:
            self.text_area.insert(tk.END, u + "\n")


if __name__ == "__main__":
    app = FrmUsuarios()
    app.mainloop()