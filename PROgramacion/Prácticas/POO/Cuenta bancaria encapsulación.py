import random

class CuentaBancaria:
    def __init__(self,nºcuenta=None,saldo=0):
        self.__nºcuenta=nºcuenta if nºcuenta else self.generateAccount() #atributo privado
        self.__saldo=saldo #atributo privado

    def generateAccount(self):
        return str(random.randint(1000000000,9999999999))

    def get_saldo(self): #consultar el saldo
        return self.__saldo

    def get_nºcuenta(self): #consultar la cuenta
        return self.__nºcuenta 

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Has ingresado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirar(self, cantidad):
        while True:
            if cantidad > 0:
                if self.__saldo >= cantidad:
                    self.__saldo -= cantidad
                    print(f"Has retirado {cantidad}. Saldo actual: {self.__saldo}")
                    break
                else:
                    print("Fondos insuficientes para retirar esa cantidad.")
                
            else:
                print("La cantidad a retirar debe ser positiva.")

def main():
    cuenta=CuentaBancaria(saldo=1000)
    print(f'Tu cuenta de banco es {cuenta.get_nºcuenta()}.')
    while True:
        print('\n---Bienvenid@ a tu cuenta de banco---')
        print('1. Ingresar.')
        print('2. Retirar.')
        print('3. Consultar saldo.')
        print('4. Salir.' )

        try:
            operacion=int(input('Elige la operación a realizar (1-4): '))
            if operacion == 1:
                cantidad = float(input("¿Cuánto quieres ingresar?: "))
                cuenta.ingresar(cantidad)

            elif operacion == 2:
                cantidad = float(input("¿Cuánto quieres retirar?: "))
                cuenta.retirar(cantidad)

            elif operacion == 3:
                print(f"Tu saldo actual es: {cuenta.get_saldo()}")

            elif operacion == 4:
                print("Gracias por usar nuestro banco.")
                break


            else:
                print('La elección debe ser un número entre 1 y 4. Intenta de nuevo.')
                continue

            


        except ValueError:
            print('Debes escribir un número válido.')

if __name__=='__main__':
    main()