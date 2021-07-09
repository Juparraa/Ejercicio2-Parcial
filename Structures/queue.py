from .node import Node

class Queue:
    '''
    Implementación de cola (FIFO) haciendo uso de listas doblemente enlazadas
    
    Attributes
    ----------
    
    first : Node

        Referencia al primer nodo de la cola
    
    last: Node
        Referencia al último nodo de la cola
    
    '''

    def __init__(self,element=None):
        
        self.first = element
        self.last = element

    # Adición y eliminación de elementos a la cola

    def enqueue(self, element):

        x = Node(element)

        if self.first == None:
            self.first = x
            self.last = x
        else:
            x.setLeft(self.last)
            self.last.setRight(x)
        
        x.setRight(None)
        self.last = x

    def dequeue(self):
        ret = self.first
        if self.first.getRight() != None:
            self.first = self.first.getRight()
            self.first.setLeft(None)
        else:
            self.first = None
        
        return ret
    
    # Consulta de la cola

    def peek(self):
        return self.first