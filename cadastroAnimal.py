from animal import *


class CadastroAnimais:
    def _init_(self):
        self.animais = []

    def cadastrar_animal(self, tipo, idade, cor, porte, raca, particularidade):
        animal = Animal(self, tipo, idade, cor, porte, raca, particularidade)
        self.animais.append(animal)