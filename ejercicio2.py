# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores


#############################################################################################################
#############################################################################################################
#############################################################################################################

class Computadora:
    _conteo_computadoras=0
    def __init__ (self, marca:str='Lenovo', procesador:str='Intel I5', disco:int=256, OS:str='Windows 11', RAM:int=8): 
        self.identificador=Computadora._conteo_computadoras+1
        self.marca=marca
        self.procesador=self.validar_procesador(procesador)
        self.disco=disco
        self.OS=OS
        self.RAM=RAM
        Computadora._conteo_computadoras+=1

#El método __str__ no debe imprimir la información; su trabajo es devolver una cadena de texto. El método que se encarga de imprimir es print().
    def __str__ (self):
        return f'La computadora {self.identificador} marca {self.marca}, tiene un procesador {self.procesador}, tiene {self.disco}GB de memoria, su sistema operativo es {self.OS}, y tiene {self.RAM}GB de RAM. '

    def validar_procesador(self, procesador):
        procesadores_posibles=['Intel I3', 'Intel I5', 'Intel I7', 'Intel I9', 'AMD Ryzen 5000', 'AMD Ryzen 7000']
        if procesador not in procesadores_posibles:
            raise ValueError (f'El procesador {procesador} no es válido. Debe estar en la siguiente lista: Intel I3, Intel I5, Intel I7, Intel I9, AMD Ryzen 5000, AMD Ryzen 7000')

        return procesador


#############################################################################################################
#############################################################################################################
#############################################################################################################

def crear_computadora():
    try:
        marca=input('Ingrese la marca. ')
        procesador=input('Ingrese el procesador. Intel I3, Intel I5, Intel I7, Intel I9, AMD Ryzen 5000, AMD Ryzen 7000: ')
        disco=int(input('Ingrese el disco: '))
        OS=input('Ingrese el sistema operativo: ')
        RAM=int(input('Ingrese la RAM: '))
        nueva_computadora=Computadora(marca, procesador, disco, OS, RAM)

    except ValueError as e:
        print(f'Error al crear la computadora. {e}')

#############################################################################################################
#############################################################################################################
#############################################################################################################

if __name__ == "__main__":   
    opcion = None
    while opcion != 9:
        try:
            opcion = int(input('Ingrese la opción deseada: ' \
            '1: crear computadora' \
            '9: salir'))
            if opcion==1:
                crear_computadora()
            elif opcion==9:
                print('Saliendo...')
            else:
                print('Opción inválida. Seleccione 1 o 9: ')
        except ValueError:
            print ('Debe ingresar un número entero.')

