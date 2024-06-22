class Asignatura:
    def __init__(self, nombre, profesor):
        self.__nombre = nombre
        self.__profesor = profesor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_profesor(self):
        return self.__profesor

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def mostrar_info(self):
        print(f"Asignatura: {self.__nombre}, Profesor: {self.__profesor.nombre} {self.__profesor.__apellido}")