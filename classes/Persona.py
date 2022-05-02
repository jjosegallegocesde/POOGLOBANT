class Persona:
    def __init__(self):
        self.nombre=None
        self.edad=None
        self.telefono=None
    def saludar(self):
        print(f'Hola me llamo {self.nombre}')
        print(f'Mi edad es {self.edad}')
        print(f'Mi telefono es {self.telefono}')