from clases import saludos as s

if __name__ == "__main__":
    saludo = s.Saludos(nombre=input("Ingrese su nombre: "))
    print(saludo.hola_mundo())