class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.__curso = curso
        self.__estudiante = estudiante
        self.__nota = nota

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def get_estudiante(self):
        return self.__estudiante

    def set_estudiante(self, estudiante):
        self.__estudiante = estudiante

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def mostrar_info(self):
        print(f"Evaluación del curso {self.__curso.__nombre} para {self.__estudiante.__nombre} {self.__estudiante.__apellido}:\nNota: {self.__nota}")