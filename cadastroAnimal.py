from animal import *


class CadastroAnimais:
    def __init__(self):
        self.animais = []

    def cadastrar_animal(self):
        tipo = input('Informe o tipo do animal: \n')
        while not all(char.isalpha() or char.isspace() for char in tipo):
            print("O tipo deve conter apenas letras.")
            tipo = input('Informe o tipo do animal: \n')
        idade = input('Informe a idade do animal: \n')
        while not idade.isdigit():
            print("A idade deve conter apenas números.")
            idade = input('Informe a idade do animal: \n')
        cor = input('Informe a cor do animal: \n')
        while not all(char.isalpha() or char.isspace() for char in cor):
            print("A cor deve conter apenas letras.")
            cor = input('Informe a cor do animal: \n')
        porte = input('Informe o porte do animal: \n')
        while not all(char.isalpha() or char.isspace() for char in porte):
            print("O porte deve conter apenas letras.")
            porte = input('Informe o porte do animal: \n')
        raca = input('Informe a raça do animal: \n')
        while not all(char.isalpha() or char.isspace() for char in raca):
            print("A raça deve conter apenas letras.")
            raca = input('Informe a raça do animal: \n')
        particularidade = input('Informe a particularidade do animal: \n(Caso não tenha, informe que não possui (NP).)\n')


        animal = Animal(tipo, idade, cor, porte, raca, particularidade)
        self.animais.append(animal)