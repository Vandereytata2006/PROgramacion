class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def presentarse(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad} años'
    def cumplirAños(self):
        self.edad+=1
        return f'{self.nombre} ahora tiene {self.edad} años.'

yo=persona('Vanderlei', 18)

nombreEl=input('Introduce tu nombre: ')
edadEl=int(input('Introduce tu edad: '))
El=persona(nombreEl, edadEl)

personas=[yo,El]
for persona in personas:
    print(persona.presentarse())
    print(persona.cumplirAños())