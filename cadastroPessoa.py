from pessoa import *


class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self):
        nome = input('Informe o nome do adotante: \n')
        contato = input('Informe o contato do adotante: \n')
        interesse_tipo = input('Informe o interesse pelo tipo do animal: \n')
        endereco = input('Informe o endereço do adotante: \n')
        interesse_particularidade = input('Informe o interesse da particularidade: \n(Caso não tenha, informe que não possui (NP).)\n')
        pessoa = Pessoa(nome, contato, interesse_tipo, endereco, interesse_particularidade)
        self.pessoas.append(pessoa)
