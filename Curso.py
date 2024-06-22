class Curso:
    def __init__(self, nombre, profesor, horario, asignatura):
        self.__nombre = nombre
        self.__profesor = profesor
        self.__estudiantes = []
        self.__horario = horario
        self.__asignatura = asignatura

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_profesor(self):
        return self.__profesor

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def get_estudiantes(self):
        return self.__estudiantes

    def set_estudiantes(self, estudiantes):
        self.__estudiantes = estudiantes

    def get_horario(self):
        return self.__horario

    def set_horario(self, horario):
        self.__horario = horario

    def get_asignatura(self):
        return self.__asignatura

    def set_asignatura(self, asignatura):
        self.__asignatura = asignatura

    def mostrar_info(self):
        print(f"Curso: {self.__nombre}, Profesor: {self.__profesor.nombre} {self.__profesor.__apellido}, Horario: {self.__horario.__dia} {self.__horario.__inicio}-{self.__horario.__fin}")

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
