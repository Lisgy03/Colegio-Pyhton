from tkinter import Tk, Label, Entry, Button, Frame, messagebox, Listbox, Toplevel
from tkinter import PhotoImage

from Curso import Curso
from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura
from Horario import Horario

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Proceso de inscripción de Cursos")

        self.bg_color = "#CFFFE5"  # Verde menta suave
        self.label_color = "#333333"
        self.button_color = "#5DB7A1"
        self.button_text_color = "black"  # Letra negra

        self.root.configure(background=self.bg_color)

        self.frame = Frame(root, bg=self.bg_color)
        self.frame.pack(padx=20, pady=20)

        image_path = "Academia.png"
        self.image = PhotoImage(file=image_path)
        self.image_label = Label(self.frame, image=self.image, bg=self.bg_color)
        self.image_label.grid(row=0, columnspan=2, pady=(0, 20))

        Label(self.frame, text="Nombre del Estudiante:", bg=self.bg_color, fg=self.label_color).grid(row=1, column=0, pady=5, sticky="w")
        self.estudiante_entry = Entry(self.frame)
        self.estudiante_entry.grid(row=1, column=1, pady=5, padx=10)

        Label(self.frame, text="Apellido del Estudiante:", bg=self.bg_color, fg=self.label_color).grid(row=2, column=0, pady=5, sticky="w")
        self.apellido_estudiante_entry = Entry(self.frame)
        self.apellido_estudiante_entry.grid(row=2, column=1, pady=5, padx=10)

        Label(self.frame, text="ID del Estudiante:", bg=self.bg_color, fg=self.label_color).grid(row=3, column=0, pady=5, sticky="w")
        self.id_estudiante_entry = Entry(self.frame)
        self.id_estudiante_entry.grid(row=3, column=1, pady=5, padx=10)

        self.boton_registrar = Button(self.frame, text="Registrar Estudiante", bg=self.button_color, fg=self.button_text_color, command=self.registrar_estudiante)
        self.boton_registrar.grid(row=4, columnspan=2, pady=10)

        self.boton_mostrar_horario = Button(self.frame, text="Mostrar Horario", bg=self.button_color, fg=self.button_text_color, command=self.mostrar_horario)
        self.boton_mostrar_horario.grid(row=5, columnspan=2, pady=10)

        self.estudiantes = []
        self.asignaturas = [
            Asignatura("Matemáticas", Profesor("Carlos", "Sanchez")),
            Asignatura("Español", Profesor("Maria", "Velez")),
            Asignatura("Naturales", Profesor("Valentina", "Claro")),
        ]
        self.horarios = [
            Horario("Lunes", "10:00", "12:00"),
            Horario("Lunes", "06:00", "08:00"),
            Horario("Lunes", "08:00", "10:00"),
            Horario("Jueves", "10:00", "12:00"),
            Horario("Jueves", "06:00", "08:00"),
            Horario("Jueves", "08:00", "10:00"),
        ]

        self.cursos = [
            Curso("6-A", Profesor("Carlos", "Sanchez"), self.horarios[0], Asignatura("Matemáticas", Profesor("Carlos", "Sanchez"))),
            Curso("6-A", Profesor("Maria", "Velez"), self.horarios[1], Asignatura("Español", Profesor("Maria", "Velez"))),
            Curso("6-A", Profesor("Valentina", "Claro"), self.horarios[2], Asignatura("Naturales", Profesor("Valentina", "Claro"))),
            Curso("6-B", Profesor("Carlos", "Sanchez"), self.horarios[3], Asignatura("Matemáticas", Profesor("Carlos", "Sanchez"))),
            Curso("6-B", Profesor("Maria", "Velez"), self.horarios[4], Asignatura("Español", Profesor("Maria", "Velez"))),
            Curso("6-B", Profesor("Valentina", "Claro"), self.horarios[5], Asignatura("Naturales", Profesor("Valentina", "Claro"))),
        ]

    def registrar_estudiante(self):
        top = Toplevel(self.root)
        top.title("Registrar Estudiante en Curso")
        top.configure(background=self.bg_color)

        Label(top, text="Seleccione un Curso:", bg=self.bg_color, fg=self.label_color).pack(pady=5)

        self.lista_cursos = Listbox(top)
        self.lista_cursos.pack(pady=5)

        for curso in self.cursos:
            self.lista_cursos.insert('end', f"{curso.get_nombre()} - {curso.get_profesor().get_nombre()}")

        Button(top, text="Registrar en Curso", bg=self.button_color, fg=self.button_text_color, command=self.registrar_estudiante_curso).pack(pady=10)

    def registrar_estudiante_curso(self):
        nombre_estudiante = self.estudiante_entry.get()
        apellido_estudiante = self.apellido_estudiante_entry.get()
        id_estudiante = self.id_estudiante_entry.get()

        if not nombre_estudiante or not apellido_estudiante or not id_estudiante:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        selected_index = self.lista_cursos.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Seleccione un curso.")
            return

        selected_curso = self.cursos[selected_index[0]]

        if selected_curso.get_nombre== "6-A" and selected_curso.get_horario().get_dia() != "Lunes":
            messagebox.showerror("Error", "El curso seleccionado es solo para los lunes.")
            return
        elif selected_curso.get_nombre() == "6-B" and selected_curso.get_horario().get_dia() != "Jueves":
            messagebox.showerror("Error", "El curso seleccionado es solo para los jueves.")
            return

        estudiante = Estudiante(nombre_estudiante, apellido_estudiante, id_estudiante)

        if estudiante in selected_curso.get_estudiantes():
            messagebox.showerror("Error", "El estudiante ya está registrado en este curso.")
            return

        selected_curso.agregar_estudiante(estudiante)

        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

        self.estudiante_entry.delete(0, 'end')
        self.apellido_estudiante_entry.delete(0, 'end')
        self.id_estudiante_entry.delete(0, 'end')

        self.lista_cursos.delete(selected_index)

        horario = selected_curso.get_horario()
        horario_str = f"Horario del Curso Registrado:\nDía: {horario.get_dia()}\nHora de inicio: {horario.get_hora_inicio()}\nHora de fin: {horario.get_hora_fin()}"
        messagebox.showinfo("Registro realizado", f"El estudiante ha sido registrado en el curso con éxito.\n\n{horario_str}")

    def mostrar_horario(self):
        if not self.estudiantes:
            messagebox.showerror("Error", "No hay estudiantes registrados.")
            return

        top = Toplevel(self.root)
        top.title("Horario de Clases")
        top.configure(background=self.bg_color)

        Label(top, text="Seleccione un Estudiante:", bg=self.bg_color, fg=self.label_color).pack(pady=5)

        self.lista_estudiantes = Listbox(top)
        self.lista_estudiantes.pack(pady=5)

        for estudiante in self.estudiantes:
            self.lista_estudiantes.insert('end', f"{estudiante.get_nombre()} {estudiante.get_apellido()}")

        self.boton_ver_horario = Button(top, text="Ver Horario", bg=self.button_color, fg="white", command=self.ver_horario)
        self.boton_ver_horario.pack(pady=10)

    def ver_horario(self):
        selected_index = self.lista_estudiantes.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Seleccione un estudiante.")
            return

        selected_estudiante = self.estudiantes[selected_index[0]]
        horarios_estudiante = []

        for curso in self.cursos:
            if selected_estudiante in curso.get_estudiantes():
                horarios_estudiante.append((curso.get_horario(), curso.get_asignatura().get_nombre(), curso.get_profesor().get_nombre()))

        if not horarios_estudiante:
            messagebox.showinfo("Horario", "El estudiante seleccionado no está inscrito en ningún curso.")
            return

        horario_str = "Horario del Estudiante:\n"
        for horario, asignatura, profesor in horarios_estudiante:
            horario_str += f"Asignatura: {asignatura}, Profesor: {profesor}, Día: {horario.get_dia()}, Hora de inicio: {horario.get_hora_inicio()}, Hora de fin: {horario.get_hora_fin()}\n"

        messagebox.showinfo("Horario", horario_str)


if __name__ == "__main__":
    root = Tk()
    menu = Interfaz(root)
    root.mainloop()