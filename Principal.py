from time import process_time_ns

estudiantes = {} #Diccionario que almacernara los estudiantes


class estudiante: #nombre del objeto estudiante

    def __init__(self, nombre, edad, carrera):
      self.Nombre = nombre
      self.Edad = edad
      self.Carrera = carrera


    def mostrar_datos(self):
        print(f'Nombre: {self.Nombre} Edad: {self.Edad} Carrera: {self.Carrera}')

class curso:

    def __init__(self, nota_tarea, nota_parcial, nota_proyecto):
        self.tarea = nota_tarea
        self.parcial = nota_parcial
        self.proyecto = nota_proyecto

    def mostrar_datoscurso(self):
        print(f'Notas:\nTareas:{self.tarea} Parcial:{self.parcial} Proyecto:{self.proyecto}')


def registro_estudiante():
    print('Bienvenido a registro de estudiantes: ')
    print('Ingrese los datos correspondientes al estudiante: ')
    carnet = input('Ingrese el numero de carnet: ')
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    carrera = input('Ingrese la carrera del estudiante: ')
    estudiante_ingreso = estudiante(nombre, edad, carrera) #Instanciamos un objeto temporal
    cantidad_cursos = int(input('Ingrese la cantidad de cursos que se asignara: '))
    cursos = {} #se crea un diccionario vacio para este objeto y posterior se llenan

    for i in range(cantidad_cursos):
        nombre_curso = input('Ingrese el nombre del curso: ')
        nota_tarea = float(input('Ingrese la nota de tareas: '))
        nota_parcial = float(input('Ingrese la nota de parcial: '))
        nota_proyecto = float(input('Ingrese la nota del proyecto: '))
        curso_tmp = curso(nota_tarea, nota_parcial, nota_proyecto)

        cursos[nombre_curso] = {
            "Notas" : curso_tmp
        }

    estudiantes[carnet] = {
        "Estudiante": estudiante_ingreso,
        "Cursos": cursos

    }




fin_menu = True

while fin_menu:
    print('\t\t===Menu Principal ===')
    print('1.Registrar estudiantes\r\n2.Mostrar estudiantes y los cursos\r\n3.Buscar estudiante por carnet\r\n4.Salir')
    op = int(input('Ingrese a una opcion: '))

    match   op:
        case 1:
            registro_estudiante()

        case 2:
            print('Mostrar estudiantes')

        case 3:
            print('Buscar estudiantes')

        case 4:
            print('Gracias por usar el sistema :) ')
            fin_menu =False

        case _:
            print('Opcion incorrecta vuelva a intentarlo... \n\n')


