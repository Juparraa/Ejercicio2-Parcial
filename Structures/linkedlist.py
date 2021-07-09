from .node import Node

class LinkedList:
    '''
    Implementación de lista simplemente enlazada
    
    Attributes
    ----------
    
    head : Node

        Referencia al primer nodo de la lista
    
    '''

    def __init__(self,element=None):
        self.head = element
    
    #Adición de elementos al inicio de la lista
    def pushfront(self, data):
        temp = Node(data)
        temp.setRight(self.head)
        self.head = temp

    #Adición de elementos al final de la lista
    def pushback(self, data):
        if self.head == None:
            self.pushfront(data)
        else:
            temp = Node(data)
            current = self.head
            while current.getRight() != None:
                current = current.getRight()
            current.setNext(temp) 
    
    #Adición de elementos despues de otro elemento en especifico:
    def insert(self, key, data):
        temp = Node(data)
        current = self.head
        while current != None:
            if current.getData() == key:
                break
            else:
                current = current.getRight()
        if current == None:
            raise ValueError("La llave no se encuentra en la lista")
        else:
            temp.setRight(current.getRight())
            current.setRight(temp)

    #Metodo para obtener el tamaño de la lista
    def size(self):
        current = self.head
        tamaño = 0
        while current != None:
            tamaño += 1
            current = current.getRight()
        return tamaño

    #Metodo de find (confirmación que el objeto este en la lista)
    def find(self, key):
        current = self.head
        while current != None:
            if current.getData() == key:
                return True
            else:
                current = current.getRight()
        return False  

    #Metodo de busqueda de nodos
    def search(self, key):
        current = self.head
        while current != None:
            if current.getData() == key:
                break
            else:
                current = current.getRight()
        if current == None:
            raise ValueError("La llave no se encuentra en la lista")
        else :
            return current

    #Metodo de actualización de datos de un nodo
    def update(self, key, data):
        current = self.head
        while current != None:
            if current.getData() == key:
                current.setData(data)
                break
            else:
                current = current.getRight()
        if current == None:
            raise ValueError("La llave no se encuentra en la lista")


    #Metodo de eliminación de nodos
    def delete(self, key):
        previous = None
        current = self.head
        while current != None:
            if current.getData() == key:
                break
            else:
                previous = current
                current = current.getRight()
        if current == None:
            raise ValueError("La llave no se encuentra en la lista")
        elif previous == None:
            self.head = current.getRight()
        else:
            previous.setRight(current.getRight)

    def popFront(self):
        temp = self.head
        self.head = self.head.getRight()
        temp.setRight(None)
        return temp.getData()
