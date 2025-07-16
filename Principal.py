from time import process_time_ns

estudiantes = {} #Diccionario que almacernara los estudiantes


class estudiante: #nombre del objeto estudiante

    def __init__(self, nombre, edad, carrera):
      self.Nombre = nombre
      self.Edad = edad
      self.Carrera = carrera


    def mostrar_datos(self):
        print(f'Nombre: {self.Nombre} Edad: {self.Edad} Carrera: {self.Carrera}')

class curso


def registro_estudiante():
    print('Bienvenido a registro de estudiantes: ')
    print('Ingrese los datos correspondientes al estudiante: ')
    carnet = input('Ingrese el numero de carnet: ')
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese la edad: ')
    carrera = input('Ingrese la carrera del estudiante: ')






fin_menu = True

while fin_menu:
    print('\t\t===Menu Principal ===')
    print('1.Registrar estudiantes\r\n2.Mostrar estudiantes y los cursos\r\n3.Buscar estudiante por carnet\r\n4.Salir')
    op = int(input('Ingrese a una opcion: '))

    match   op:
        case 1:
            registro_estudiante()

        case 2:

        case 3:

        case 4:
            print('Gracias por usar el sistema :) ')
            fin_menu =False

        case _:
            print('Opcion incorrecta vuelva a intentarlo... \n\n')


