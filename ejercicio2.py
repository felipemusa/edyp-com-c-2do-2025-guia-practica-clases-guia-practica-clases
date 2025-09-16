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
        self.identificador=Computadora._conteo_computadoras + 1
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
    
    def updateOS(self, nuevo_OS):
        self.OS=nuevo_OS

    def getCapacity(self, componente):
        if componente.lower()=='disco':
            return self.disco
        elif componente.lower()=='ram':
            return self.RAM
        else:
            return None

#############################################################################################################
#############################################################################################################
#############################################################################################################
lista_computadoras=[]
def crear_computadora():
    try:
        marca=input('Ingrese la marca. ')
        procesador=input('Ingrese el procesador. Intel I3, Intel I5, Intel I7, Intel I9, AMD Ryzen 5000, AMD Ryzen 7000: ')
        disco=int(input('Ingrese el disco: '))
        OS=input('Ingrese el sistema operativo: ')
        RAM=int(input('Ingrese la RAM: '))
        nueva_computadora=Computadora(marca, procesador, disco, OS, RAM)
        lista_computadoras.append(nueva_computadora)
        print(f'La computadora #{nueva_computadora.identificador} fue creada con éxito')

    except ValueError as e:
        print(f'Error al crear la computadora. {e}')

def updateOS_menu():
    try:
        computadora_encontrada=None
        identificador_a_cambiar=int(input('Ingrese el identificador de la computadora que desea editar: '))
        for computadora in lista_computadoras:
            if computadora.identificador==identificador_a_cambiar:
                computadora_encontrada=computadora
        if computadora_encontrada:
            nuevo_OS=input('Ingrese el nuevo OS: ')
            computadora_encontrada.updateOS(nuevo_OS)
            print(f'El sistema operativo de la computadora {identificador_a_cambiar} fue cambiado con éxito a {nuevo_OS}. ')
        else:
            print('Computadora no encontrada. ')
    except ValueError as e:
        print(f'Debe ser un número entero. ')
    except Exception:
        print('Ocurrión un error inesperado. ')

def getCapacity_menu():
    try:
        computadora_encontrada=None
        identificador_a_cambiar=int(input('Ingrese el identificador de la computadora que desea editar: '))
        for computadora in lista_computadoras:
            if computadora.identificador==identificador_a_cambiar:
                computadora_encontrada=computadora
                break

        if computadora_encontrada:
            componente=input('Ingrese el componente a conocer. Seleccione entre disco y RAM: ')
            capacidad=computadora_encontrada.getCapacity(componente)
            if capacidad is not None:
                print(f'La capacidad es de {capacidad}GB. ')
            else:
                print('Componente inválido. ')

        else:
            print('Computadora no encontrada. ')


    except ValueError as e:
        print('El número del identificador debe ser entero. ')
    except Exception:
        print('Ocurrió un error inesperado. ')
    
    
    

#############################################################################################################
#############################################################################################################
#############################################################################################################

if __name__ == "__main__":   
    opcion = None
    while opcion != 9:
        try:
            opcion = int(input('Ingrese la opción deseada:  \n 1: crear computadora \n 2: actualizar OS \n 3: ver capacidad \n 9: salir \n >'))
            if opcion==1:
                crear_computadora()
            elif opcion==2:
                updateOS_menu()
            elif opcion==3:
                getCapacity_menu()
            elif opcion==9:
                print('Saliendo...')
            else:
                print('Opción inválida. Seleccione 1 o 9: ')
        except ValueError:
            print ('Debe ingresar un número entero.')