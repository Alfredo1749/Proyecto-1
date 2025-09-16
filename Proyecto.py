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
    
#16/09/25
class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []    # NUEVO: registro de estudiantes
        self.evaluaciones  = []  # NUEVO: registro de evaluaciones

    def inscribir_estudiante(self, alumno):
        if alumno not in self.estudiantes:  # Verifica si el alumno ya está inscrito
            self.estudiantes.append(alumno)
            alumno.inscribirse(self.nombre)
            print(f"Alumno {alumno.get_nombre()} inscrito en {self.nombre}.")
        else:
            print(f"El alumno {alumno.get_nombre()} ya está inscrito en {self.nombre}.")

    def crear_evaluacion(self, nombre_eval, tipo):
        evaluacion = Evaluacion(nombre_eval, tipo)  # NUEVO: relación con Evaluación
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación {nombre_eval} creada en el curso {self.nombre}.")
        return evaluacion
    
    def listar_estudiantes(self):
        # NUEVO: recorrer alumnos inscritos
        return [alumno.get_nombre() for alumno in self.estudiantes]
    
    def listar_evaluaciones(self):
        # NUEVO: recorrer evaluaciones del curso
        return [eval.nombre for eval in self.evaluaciones]

class Evaluacion: 
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.calificaciones = {}  # diccionario {alumno: nota}

    def registrar_notas(self, alumno, nota):
        self.calificaciones[alumno.get_nombre()] = nota  # Guardar nota del alumno
        print(f"Nota registrada {alumno.get_nombre()} = {nota}")

    def ver_calificaciones(self):
        return self.calificaciones if self.calificaciones else "No hay calificaciones registradas."

def generar_reporte(curso):
    print(f"\n--- Reporte del curso {curso.nombre} ---")
    for alumno in curso.estudiantes:
        notas = []
        for eval in curso.evaluaciones:
            if alumno.get_nombre() in eval.calificaciones:
                notas.append(eval.calificaciones[alumno.get_nombre()])
        
        if notas:
            promedio = sum(notas)/len(notas)
            estado = "Bajo" if promedio < 60 else "Aprobado"
            print(f"{alumno.get_nombre()} -> Promedio {promedio:.2f} Estado -> {estado}")
        else:
            print(f"{alumno.get_nombre()} -> sin notas registradas")