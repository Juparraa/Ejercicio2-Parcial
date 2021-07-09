class Node:
    '''
    Nodos para lista doblement enlazada

    Attributes
    ----------
    
    data : object
        
        Objeto con dato

    next : Node
        
        Referencia al nodo siguiente, o el que se encuentra a la derecha

    last : Node

        Referencia al nodo anterior, o el que se encuentra a la izquierda
    '''
    def __init__(self, data=None, rightNode=None, leftNode=None):
        self.data = data
        self.rightNode = rightNode
        self.leftNode = leftNode

    # Consulta de datos del nodo

    def __str__(self):
        return self.data

    def getData(self):
        return self.data

    # Consultas de nodos adyacentes

    def getLeft(self):
        return self.leftNode

    def getRight(self):
        return self.rightNode


    # Modificaciones del nodo
    
    def setData(self,data):
        self.Data = data
    
    def setRight(self,rightNode):
        self.rightNode = rightNode

    def setLeft(self,leftNode):
        self.leftNode = leftNode