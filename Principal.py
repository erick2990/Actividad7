from time import process_time_ns

from gtweak.utils import execute_subprocess

estudiantes = {} #Diccionario que almacernara los estudiantes


class estudiante: #nombre del objeto estudiante

    def __init__(self, nombre, edad, carrera):
      self.Nombre = nombre
      self.Edad = edad
      self.Carrera = carrera


    def mostrar_estudiante(self):
        print(f'Nombre: {self.Nombre} Edad: {self.Edad} Carrera: {self.Carrera}')

class curso:

    def __init__(self,nombre, nota_tarea, nota_parcial, nota_proyecto):
        self.nombre = nombre
        self.tarea = nota_tarea
        self.parcial = nota_parcial
        self.proyecto = nota_proyecto

    def mostrar_datoscurso(self):
        print(f'Notas {self.nombre}:\nTareas:{self.tarea} Parcial:{self.parcial} Proyecto:{self.proyecto}')


def registro_estudiante():
    print('Bienvenido a registro de estudiantes \n\n')
    print('Ingrese los datos correspondientes al estudiante \n')
    carnet = input('Ingrese el numero de carnet: ')
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    carrera = input('Ingrese la carrera del estudiante: ')
    estudiante_ingreso = estudiante(nombre, edad, carrera) #Instanciamos un objeto temporal
    cantidad_cursos = int(input('Ingrese la cantidad de cursos que se asignara: '))
    cursos = {} #se crea un diccionario vacio para este objeto y posterior se llenan

    for i in range(cantidad_cursos):
        id_curso = input(f'Ingrese el CODIGO del {i+1} curso: ')
        nombre_curso = input(f'Ingrese el NOMBRE del {i+1} curso: ')
        nota_tarea = float(input('Ingrese la NOTA de tareas: '))
        nota_parcial = float(input('Ingrese la NOTA de parcial: '))
        nota_proyecto = float(input('Ingrese la NOTA del proyecto: '))
        curso_tmp = curso(nombre_curso, nota_tarea, nota_parcial, nota_proyecto)
        print('\n')
        cursos[id_curso] = {
            "Notas" : curso_tmp #Se añade un nuevo curso cada que se ingresan nuevos datos su llave sera siempre su ID
        }

    estudiantes[carnet] = {
        "Estudiante": estudiante_ingreso,
        "Cursos": cursos
    }
    print('Estudiante registrado con exito')


def mostrar_info():
    print('\t\t\tInformacion de los estudiantes:')
    for  llave, campo1 in estudiantes.items():
        campo1["Estudiante"].mostrar_estudiante()
        for id, datos_curso in campo1["Cursos"].items():
            print(f'Codigo Curso: {id}')
            datos_curso["Notas"].mostrar_datoscurso()

def buscar_estudiante():





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
            mostrar_info()

        case 3:
            print('Buscar estudiantes')

        case 4:
            print('Gracias por usar el sistema :) ')
            fin_menu =False

        case _:
            print('Opcion incorrecta vuelva a intentarlo... \n\n')


