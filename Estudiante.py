class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id_estudiante = id_estudiante
        self.__cursos = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_id_estudiante(self):
        return self.__id_estudiante

    def set_id_estudiante(self, id_estudiante):
        self.__id_estudiante = id_estudiante

    def get_cursos(self):
        return self.__cursos

    def set_cursos(self, cursos):
        self.__cursos = cursos

    def mostrar_info(self):
        print(f"Estudiante: {self.get_nombre()} {self.get_apellido()}, ID: {self.get_id_estudiante()}")