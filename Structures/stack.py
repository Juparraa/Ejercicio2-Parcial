from .node import Node

class Stack:
    '''
    Implementación de pila (LIFO) haciendo uso de listas enlazadas
    
    Attributes
    ----------
    
    last: Node
        Referencia al último nodo de la cola
    
    '''
    def __init__(self, element=None):

        self.last = element

        # Adición y eliminación de elementos a la pila

    def push(self, element):

        x = Node(element)

        if self.last == None:
            self.last = x
        else:
            x.setLeft(self.last)
            self.last = x

    def pop(self):
        x = self.last
        try:
            self.last = self.last.getLeft()
        except:
            self.last = None

        return x

    # Consulta del elemento superior

    def top(self): 
        return self.last