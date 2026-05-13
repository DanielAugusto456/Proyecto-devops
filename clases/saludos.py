class Saludos:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, {self.nombre}!"
    
    def saludo_formal(self):
        return f"Buenos días, {self.nombre}. Es un placer saludarle."