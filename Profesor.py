class Profesor:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__asignaturas = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_asignaturas(self):
        return self.__asignaturas

    def set_asignaturas(self, asignaturas):
        self.__asignaturas = asignaturas

    def mostrar_info(self):
        print(f"Profesor: {self.__nombre} {self.__apellido}")