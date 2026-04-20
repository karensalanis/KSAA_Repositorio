class Perro:
    def __init__(self, nombre, raza, edad, peso, embarazada):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__embarazada = embarazada

    def get_nombre (self) :
        return self.__nombre
    def set_nombre (self, nombre) :
        self.__nombre = nombre
    def get_raza (self) :
        return self.__raza 
    def set_raza (self, raza) :
        self.__raza = raza
    def get_edad (self) :
        return self.__edad
    def set_edad (self, edad) :
        self.__edad = edad
    def get_peso (self) :
        return self.__peso
    def set_peso (self, peso) :
        self.__peso = peso
    def get_embarazada (self) :
        return self.__embarazada
    def set_embarazada (self, embarazada) :
        self.__embarazada = embarazada
    def info(self) :
        print (self.__nombre)
        print (self.__raza)
        print (self.__edad)
        print (self.__peso)
        print (self.__embarazada)
    
    def es_adulto(self):
        if self.__edad >= 2:
            print("es adulto")
        else:
            print("es cachorro")
print ("Perro 1")
nombre = input("ingresa nombre: ")
raza = input("ingresa raza: ")
edad = int(input("ingresa edad: "))
peso = float(input("ingresa peso: "))
embarazada = input("esta embarazada (si/no): ")

perro1 = Perro(nombre, raza, edad, peso, embarazada)

print("perro 1 creado")
perro1.info()
perro1.es_adulto()
perro1.subir_pesdo()

print("-----------------------------")

perro2 = Perro("Max", "pomerania", 4, 12, "no")
print("Perro 2")
perro2.info()
perro2.es_adulto()
perro2.subir_peso()

print("-----------------------------")