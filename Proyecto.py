#Comenzar con clases para registrar usuarios dentro del codigo 
#Definir funciones Basicas dentro de la clase
#Integrar destructores al programa
#Añadir funciones extras fuera de la clase poniendo en practica conocimientos nuevos
#Definir un bucle while para integrar un menú

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id_usuario = id_usuario   #Atributo privado
        self.__nombre = nombre
    
    def get_id(self):  # Función get para acceder al atributo
        return self.__id_usuario
  
    def get_nombre(self):
        return self.__nombre
    
    def mostrar_info(self):  # Implementación del primer método de usuario
        return f"Usuario: {self.__nombre} (ID: {self.__id_usuario})"
    
    def __del__(self):
        print(f"Usuario {self.__nombre} eliminado del sistema.")  # Destructor si se necesita


class Alumno(Usuario):
    def __init__(self, id_usuario, nombre):
        super().__init__(id_usuario, nombre)
        self.cursos = []  # Definición de lista para los cursos 
    
    def inscribirse(self, curso):  # Inscripciones para alumnos
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"{self.get_nombre()} se inscribió en el curso {curso}.")
        else:
            print(f"{self.get_nombre()} ya está inscrito en el curso {curso}.")
    
    def ver_cursos(self):  # Ver cursos inscritos
        return self.cursos if self.cursos else "No está inscrito en ningún curso."


class Profesor(Usuario):
    def __init__(self, id_usuario, nombre):
        super().__init__(id_usuario, nombre)
        self.cursos_asignados = []  # Lista de cursos a impartir
    
    def crear_curso(self, nombre_curso, codigo):  # Crear curso
        curso = {"nombre": nombre_curso, "codigo": codigo}
        self.cursos_asignados.append(curso)
        print(f"Curso '{nombre_curso}' creado por el profesor {self.get_nombre()}.")
        return curso
    
    def ver_cursos(self):  # Ver cursos asignados
        return self.cursos_asignados if self.cursos_asignados else "No tiene cursos asignados."


#16/09/25
class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []    # registro de estudiantes
        self.evaluaciones  = []  # registro de evaluaciones

    def __str__(self):
        return self.nombre  # Ahora cuando se imprima solo muestra el nombre

    def inscribir_estudiante(self, alumno):
        if alumno not in self.estudiantes:  # Verifica si el alumno ya está inscrito
            self.estudiantes.append(alumno)
            alumno.inscribirse(self.nombre)
            print(f"Alumno {alumno.get_nombre()} inscrito en {self.nombre}.")
        else:
            print(f"El alumno {alumno.get_nombre()} ya está inscrito en {self.nombre}.")

    def crear_evaluacion(self, nombre_eval, tipo):
        evaluacion = Evaluacion(nombre_eval, tipo)
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación {nombre_eval} creada en el curso {self.nombre}.")
        return evaluacion
    
    def listar_estudiantes(self):
        return [alumno.get_nombre() for alumno in self.estudiantes]
    
    def listar_evaluaciones(self):
        return [eval.nombre for eval in self.evaluaciones]


class Evaluacion: 
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.calificaciones = {}  # diccionario {alumno: nota}

    def __str__(self):
        return self.nombre  # Igual, solo muestra el nombre al imprimir

    def registrar_notas(self, alumno, nota):
        self.calificaciones[alumno.get_nombre()] = nota
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
            estado = "Reprobado" if promedio < 60 else "Aprobado"
            print(f"{alumno.get_nombre()} -> Promedio {promedio:.2f} Estado -> {estado}")
        else:
            print(f"{alumno.get_nombre()} -> sin notas registradas")


# Guardar registros en un archivo txt
def guardar_registro(mensaje):
    try:
        with open("registros.txt", "a", encoding="utf-8") as f:
            f.write(mensaje + "\n")
    except Exception as e:
        print("Error al guardar registro:", e)


# Uso de *args y **kwargs
def mostrar_detalles(*args, **kwargs):
    print("Detalles adicionales:")
    for arg in args:
        print("-", arg)
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


# Función extra: buscar cursos por nombre
def buscar_curso(cursos, nombre):
    for curso in cursos:
        if curso.nombre.lower() == nombre.lower():
            return curso
    return None


# Función extra: Notas de estudiantes 
def ver_notas_estudiante(curso, alumno):
    print(f"\nNotas de {alumno.get_nombre()} en {curso.nombre}:")
    for eval in curso.evaluaciones:
        nota = eval.calificaciones.get(alumno.get_nombre(), "Sin nota")
        print(f"{eval.nombre} ({eval.tipo}): {nota}")


# Función auxiliar para elegir elementos
def seleccionar(lista, tipo):
    """Función auxiliar para seleccionar elementos de una lista"""
    if not lista:
        print(f"No hay {tipo} registrados.")
        return None
    print(f"\n--- {tipo.upper()} DISPONIBLES ---")
    for i, item in enumerate(lista):
        if hasattr(item, "get_nombre"):  # alumnos o profesores
            print(f"{i+1}. {item.get_nombre()}")
        elif isinstance(item, Curso):  # cursos
            print(f"{i+1}. {item}")  # gracias al __str__ solo muestra el nombre
        elif isinstance(item, Evaluacion):  # evaluaciones
            print(f"{i+1}. {item}")  # gracias al __str__ solo muestra el nombre
        elif isinstance(item, dict):  # en caso de diccionarios
            print(f"{i+1}. {item['nombre']}")
        else:
            print(f"{i+1}. {item}")
    try:
        indice = int(input(f"Selecciona un {tipo} (1-{len(lista)}): ")) - 1
        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            print("Selección inválida.")
            return None
    except ValueError:
        print("Debes ingresar un número.")
        return None


def menu():
    profesores = []
    alumnos = []
    cursos = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Alumno")
        print("2. Registrar Profesor")
        print("3. Crear Curso")
        print("4. Inscribir Alumno en Curso")
        print("5. Crear Evaluación en Curso")
        print("6. Registrar Nota")
        print("7. Generar Reporte")
        print("8. Ver Notas de Alumno")
        print("9. Salir")

        opcion = input("Elige una opción: ")
        try:
            if opcion == "1":
                id_a = input("ID Alumno: ")
                nombre_a = input("Nombre Alumno: ")
                alumno = Alumno(id_a, nombre_a)
                alumnos.append(alumno)
                guardar_registro(f"Alumno registrado: {nombre_a}")
            
            elif opcion == "2":
                id_p = input("ID Profesor: ")
                nombre_p = input("Nombre Profesor: ")
                profesor = Profesor(id_p, nombre_p)
                profesores.append(profesor)
                guardar_registro(f"Profesor registrado: {nombre_p}")

            elif opcion == "3":
                if not profesores:
                    print("No hay profesores registrados.")
                    continue
                profesor = seleccionar(profesores, "profesor")
                if not profesor:
                    continue
                nombre_curso = input("Nombre del curso: ")
                codigo = input("Código del curso: ")
                curso = Curso(nombre_curso, codigo, profesor)
                cursos.append(curso)
                guardar_registro(f"Curso creado: {nombre_curso}")
            
            elif opcion == "4":
                curso = seleccionar(cursos, "curso")
                alumno = seleccionar(alumnos, "alumno")
                if curso and alumno:
                    curso.inscribir_estudiante(alumno)
                    guardar_registro(f"Alumno {alumno.get_nombre()} inscrito en {curso.nombre}")
            
            elif opcion == "5":
                curso = seleccionar(cursos, "curso")
                if not curso:
                    continue
                nombre_eval = input("Nombre de la evaluación: ")
                tipo = input("Tipo (examen/tarea): ")
                curso.crear_evaluacion(nombre_eval, tipo)
                guardar_registro(f"Evaluación {nombre_eval} creada en {curso.nombre}")
            
            elif opcion == "6":
                curso = seleccionar(cursos, "curso")
                if not curso or not curso.evaluaciones or not curso.estudiantes:
                    print("Faltan evaluaciones o estudiantes.")
                    continue
                eval = seleccionar(curso.evaluaciones, "evaluación")
                alumno = seleccionar(curso.estudiantes, "alumno")
                if eval and alumno:
                    nota = float(input("Ingrese nota: "))
                    eval.registrar_notas(alumno, nota)
                    guardar_registro(f"Nota {nota} registrada para {alumno.get_nombre()} en {curso.nombre}")

            elif opcion == "7":
                curso = seleccionar(cursos, "curso")
                if curso:
                    generar_reporte(curso)
            
            elif opcion == "8":
                curso = seleccionar(cursos, "curso")
                if not curso or not curso.estudiantes:
                    print("No hay cursos o estudiantes en este curso.")
                    continue
                alumno = seleccionar(curso.estudiantes, "alumno")
                if alumno:
                    ver_notas_estudiante(curso, alumno)
            
            elif opcion == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
