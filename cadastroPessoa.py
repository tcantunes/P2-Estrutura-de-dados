from pessoa import *


class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self):
        nome = input('Informe o nome do adotante: \n')
        while not all(char.isalpha() or char.isspace() for char in nome):
            print("O nome deve conter apenas letras.")
            nome = input('Informe o nome do adotante: \n')
        contato = input('Informe o contato do adotante (E-mail ou Telefone): \n')
        interesse_tipo = input('Informe o interesse pelo tipo do animal: \n')
        while not all(char.isalpha() or char.isspace() for char in interesse_tipo):
            print("O interesse pelo tipo do animal deve conter apenas letras.")
            interesse_tipo = input('Informe o interesse pelo tipo do animal: \n')
        endereco = input('Informe o endereço do adotante: \n')
        interesse_particularidade = input('Informe o interesse da particularidade: \n(Caso não tenha, informe que não possui (NP).)\n')
        pessoa = Pessoa(nome, contato, interesse_tipo, endereco, interesse_particularidade)
        self.pessoas.append(pessoa)
