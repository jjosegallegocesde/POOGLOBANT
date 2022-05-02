class Persona:
    def __init__(self):
        self.name = None
        self.edad = None
        self.telefono = None
    
    def saludar(self):
        print(f'Hola me llamo {self.name}')
        print(f'tengo {self.edad} años de edad')