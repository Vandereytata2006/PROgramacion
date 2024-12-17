class animal:

    def __init__(self, especie, edad):
        self.especie=especie
        self.edad=edad

    def hacer_sonido(self):
        print('Este animal hace un sonido.')

    def info(self):
        print(f'Especie: {self.especie}')
        print(f'Edad: {self.edad}')

class perro(animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
      

    def hacer_sonido(self):
        print('Guau guau') 
        
class gato(animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
        

    def hacer_sonido(self):
        print('Miaaaauu')

Perro=perro('Perro', 3)
Gato=gato('Gato', 2)
animales=[Perro, Gato]
for animal in animales:
    print(animal.hacer_sonido(),'  ', animal.info())

#este es mejor:
"""class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace un sonido.")

    def info(self):
        print(f"Especie: {self.especie}, Edad: {self.edad} años.")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miaaaauu!")


# Instancias de los animales
perro = Perro("Perro", 3)
gato = Gato("Gato", 2)

# Lista de animales
animales = [perro, gato]

# Mostrar información y sonido de cada animal
for animal in animales:
    animal.hacer_sonido()  # Llama al método sobrescrito
    animal.info()          # Muestra la información
    print()  # Espacio para separar cada animal
"""