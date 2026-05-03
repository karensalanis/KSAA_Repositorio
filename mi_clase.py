Class Mi_Clase:

    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def get_num3(self):
        return self.__num3

    def set_num1(self, num1):
        self.__num1 = num1

    def set_num2(self, num2):
        self.__num2 = num2

    def set_num3(self, num3):
        self.__num3 = num3

    def info(self):
        print("Num1:", self.__num1)
        print("Num2:", self.__num2)
        print("Num3:", self.__num3)

    def sumar(self):
        resultado = self.__num1 + self.__num2 + self.__num3
        print("Suma:", resultado)

    def mayor(self):
        mayor = max(self.__num1, self.__num2, self.__num3)
        print("Mayor:", mayor)

    def menor(self):
        menor = min(self.__num1, self.__num2, self.__num3)
        print("Menor:", menor)

    def iguales(self):
        if self.__num1 == self.__num2 == self.__num3:
            print("Son iguales")
        else:
            print("No son iguales")

    def concatenar(self):
        texto = str(self.__num1) + str(self.__num2) + str(self.__num3)
        print("Concatenación:", texto)

