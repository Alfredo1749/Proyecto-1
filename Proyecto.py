#Comenzar con clases para registrar usuarios dentro del codigo 
#Definir funciones Basicas dnetro de la clase
#Integrar destructores al programa
#Añadir funciones extras fuera de la clase3 poniendo en practica conocimientos nuevos
#Definir un bucle while para integrar un menú

class Usuario:
    def _init_(self, id_usuario, nombre):
        self.__id_usuario = id_usuario   #Atributo privado
        self.__nombre = nombre
    
    
    def get_id(self): # Fundion get para acceder al atributo
        return self.__id_usuario
  
    def get_nombre(self):
        return self.__nombre
    
    def mostrar_info(self):#Implemnentacion del primer metodo de usuario
        return f"Usuario: {self._nombre} (ID: {self._id_usuario})"
    
    def _del_(self):
        print(f"Usuario {self.__nombre} eliminado del sistema.")#Destructor si se necesita


class Alumno(Usuario):
    def _init_(self, id_usuario, nombre):
        super()._init_(id_usuario, nombre)
        self.cursos = []  #Definicion de lista para los cursos 
    
    def inscribirse(self, curso): #Inscripciones para alumnos
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"{self.get_nombre()} se inscribió en el curso {curso}.")
        else:
            print(f"{self.get_nombre()} ya está inscrito en el curso {curso}.")
    
    def ver_cursos(self):#Proyeccion de la funcion si cumple o no
        return self.cursos if self.cursos else "No está inscrito en ningún curso."


class Profesor(Usuario):
    def _init_(self, id_usuario, nombre):
        super()._init_(id_usuario, nombre)
        self.cursos_asignados = []  #Lista de cursos a impartir
    
    def crear_curso(self, nombre_curso, codigo): #Primera funcion
        curso = {"nombre": nombre_curso, "codigo": codigo}
        self.cursos_asignados.append(curso)
        print(f"Curso '{nombre_curso}' creado por el profesor {self.get_nombre()}.")
        return curso
    
    def ver_cursos(self): #Proyeccion de la funcion y o sino cumple 
        return self.cursos_asignados if self.cursos_asignados else "No tiene cursos asignados."