# Guía Práctica

## Tema: Clases

### Ejercicio 1

Dada la siguiente clase:

```python
class Camion:
    def __init__(self, marca, modelo):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
```

a. Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y luego ejecutá las instrucciones en la máquina para comprobar tu respuesta.

```python


furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2)
print(furgon1 is furgon2)
print(furgon3 == furgon4)
print(furgon3 is furgon4)
print(furgon1 == furgon4) 
```

b. Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva True cuando todos sus atributos sean iguales.

c. ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y modificá el código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.

d. Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones.

f. Creá un pequeño menú que te permita:

1. Registrar un nuevo camión.
2. Modificar la carga de un camión.
3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
4. Mostrar por terminal la marca que más veces fue registrada.

### Ejercicio 2

En este ejercicio vamos a modelar una computadora, creando la clase `Computadora` para ello.

A done
Primero, pensá un rato en todas las características que mirarías al momento de comprar una. ¿Cómo llamamos a esas características en el paradigma de la programación orientada a objetos?
ATRIBUTOS

Luego de pensarlo, continuá con la consigna.

B done
- El objeto computadora debe ser instanciado con todos sus atributos pasados como parámetros al método constructor. Al momento de crear el equipo, asignales a los atributos valores por defecto. ¿Qué criterio tuviste en cuenta para elegir esos valores?

C done
- El método `__str__` nos ayuda a conocer la información esencial de nuestros objetos. ¡Implementalo! Recordá que siempre debería estar presente en las clases que creás.

D
- Instanciá 3 computadoras y asignales distintos valores a sus atributos.

E done
- ¿Cómo podrías llevar la cuenta de la cantidad de computadoras creadas? ¿Qué tipo de variable resuelve lo pedido?

F
- Implementá al menos 2 de los siguientes métodos en la clase Computadora:

  f.1- `updateOS`: Actualiza el sistema operativo.
  f.2- `PM`: Brinda un mantenimiento programado al hardware del equipo.
  f.3- `addRAM`: Instala un nuevo módulo de RAM en la computadora.
  f.4- `getCapacity`: Muestra la capacidad del componente de hardware que se desee conocer.

G
> Nota: Pedile ayuda a tu monitor para pensar cómo implementar los métodos solicitados. Pensá en aquellos atributos creados u otros adicionales que les den funcionalidad y practicidad a dichos métodos. Si es necesario, podés investigar el uso de `datetime` u otra librería que requieras. Recordá informar siempre al usuario sobre las acciones realizadas en el sistema. Probá todos los métodos creados para testear su funcionamiento.

H
- Elegí algún componente de hardware o software de la máquina (atributo) y dale identidad. Para ello, creá otra clase, definí el constructor, el `__str__` y pensá en al menos una función que sea aplicable al componente elegido. Codificá el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? ¿Una lectura (read)? ¿Una escritura (write)? ¿Una ejecución (exec)?