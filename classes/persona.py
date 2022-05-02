from cgi import print_arguments


class Persona:

    def __init__(self,edad,nombre,telefono):
        self.nombre=None
        self.edad=None
        self.telefono=None
        
    def saludarr(self):
        print(f'hola me llamo {self.nombre}')
        print("jajajaj")

