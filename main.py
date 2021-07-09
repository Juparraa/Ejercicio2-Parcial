from Structures.node import Node
from Structures.queue import Queue
from Structures.stack import Stack
from Structures.linkedlist import LinkedList

class Vacuna:

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = int(cantidad)

    def setCantidad(self, cantidad):
        self.cantidad = int(cantidad)
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCantidad(self):
        return self.cantidad
    
    def getNombre(self):
        return self.nombre

    def usarVacunas(self, cantidad):
        restantes = self.getCantidad() - cantidad
        self.setCantidad(restantes)


class Region:

    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = int(poblacion)
    
    def setPoblacion(self, poblacion):
        self.poblacion = int(poblacion)
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getPoblacion(self):
        return self.poblacion
    
    def getNombre(self):
        return self.nombre


def read_vacunas():
    
    listaVacunas = LinkedList()

    n = int(input())        # número de tipos de vacunas
    nx = input().split(" ") # lista de vacunas y cantidades

    for x in range(n):
        x=x*2
        vacuna = Vacuna(nx[x], nx[x+1])
        listaVacunas.pushfront(vacuna)

    return listaVacunas
    
def read_regiones():
    listaRegiones = LinkedList()
    m = int(input())        # número de regiones
    mx = input().split(" ") # lista de regiones y poblaciones
    
    for y in range(m):
        y=y*2
        region = Region(mx[y], mx[y+1])
        listaRegiones.pushfront(region)

    return listaRegiones

#TODO : arreglar esto, no sirve, se supone que las ordene en orden ascendente
def sortVacunas(listaVacunas):
    current = listaVacunas.head
    index = None
    while current != None:
        index = current.getRight()
        while index != None:
            if(current.getData().getCantidad() < index.getData().getCantidad()):
                temp = current.getData()
                current.setData(index.getData())
                index.setData(temp)
            index = index.getRight()
        current = current.getRight()
    
#TODO : arreglar esto, no sirve, se supone que las ordene en orden ascendente
def sortRegiones(listaRegiones):
    current = listaRegiones.head
    index = None
    while current != None:
        index = current.getRight()
        while index != None:
            if(current.getData().getPoblacion() > index.getData().getPoblacion()):
                current.setRight(index.getRight())
                index.setRight(current)
            index = index.getRight()
        current = current.getRight()

#TODO : no estoy seguro que esto sirva, pero esoty intentando arreglar primero el sort
def enviarVacunas(queueVacunas, StackRegiones):
    output = Queue()
    Region = StackRegiones.pop().getData()
    output.enqueue(Region.getNombre())

    while Region.getPoblacion() != 0:

        Vacuna = queueVacunas.peek().getData()

        if Vacuna.getCantidad() > Region.getPoblacion():
            output.enqueue(Vacuna.getNombre())
            output.enqueue(Region.getPoblacion())
            Vacuna.setCantidad(Vacuna.getCantidad()- Region.getPoblacion())
            Region.setPoblacion(0)

        else:
            output.enqueue(Vacuna.getNombre())
            output.enqueue(Vacuna.getCantidad())
            Region.setPoblacion(Region.getPoblacion() - Vacuna.getCantidad())
            Vacuna.setCantidad(0)
            queueVacunas.dequeue()

    while output.peek() != None:
        print(output.dequeue().getData(), end =" ")
    print("")

def main():
    listaVacunas = read_vacunas()
    listaRegiones = read_regiones()
    sortVacunas(listaVacunas)       #Vacunas organizadas según su cantidad en orden ascendiente
    sortRegiones(listaRegiones)     #Regiones organizadas según su población en orden ascendiente
    Vacunas = Queue()
    Regiones = Stack()
    while listaVacunas.size() > 0:
        Vacunas.enqueue(listaVacunas.popFront())
    while listaRegiones.size() > 0:
        Regiones.push(listaRegiones.popFront())
    while Regiones.top() != None:
        enviarVacunas(Vacunas, Regiones)
         
if __name__ == '__main__':
    main()