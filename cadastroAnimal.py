from animal import *


class CadastroAnimais:
    def _init_(self):
        self.animais = []

    def cadastrar_animal(self, tipo, idade, cor, porte, raca, particularidade):
        animal = Animal(self, tipo, idade, cor, porte, raca, particularidade)
        self.animais.append(animal)

        # Cadastro por entrada de dados:

        animal_tipo = input('Informe o tipo do animal: \n')
        animal_idade = input('Informe a idade do animal: \n')
        animal_cor = input('Informe a cor do animal: \n')
        animal_porte = input('Informe o porte do animal: \n')
        animal_raca = input('Informe a raça do animal: \n')
        animal_particularidade = input('Informe a particularidade do animal: \nCaso não tenha, informe que não possui.')
        self.cadastrar_animal(animal_tipo, animal_idade, animal_cor, animal_porte, animal_raca, animal_particularidade)
        