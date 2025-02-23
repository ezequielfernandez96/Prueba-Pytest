#2 importa la clase Operaciones, agrega otra que herede Operaciones,utiliza super y agrega dos funciones mas, multiplicar y dividir
from operaciones import Operaciones

class FuncionesExtra(Operaciones):
    def __init__(self):
        super().__init__()
        print("inicia la clase funciones extra")
    
    def multiplicar(self,a, b):
        return a * b
    
    def dividir(self,a, b):
        if b == 0:
            return "error, no se puede dividir por 0"
        return a / b 
