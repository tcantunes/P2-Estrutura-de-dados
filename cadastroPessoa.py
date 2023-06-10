from pessoa import *


class CadastroPessoas():
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, nome, contato, interesse_tipo, endereco, interesse_particularidade=None):
        pessoa = Pessoa(nome, contato, interesse_tipo, endereco, interesse_particularidade)
        self.pessoas.append(pessoa)

        # Cadastro de pessoa por entrada de dados:

        pessoa_nome = input('Informe o nome do adotante: \n')
        pessoa_contato = input('Informe o contato do adotante: \n')
        pessoa_interesse_tipo = input('Informe o interesse pelo tipo do animal: \n')
        pessoa_endereco = input('Informe o endereço do adotante: \n')
        pessoa_interesse_particularidade = input('Informe o interesse da particularidade: \n')
        self.cadastrar_pessoa(pessoa_nome, pessoa_contato, pessoa_interesse_tipo, pessoa_endereco, pessoa_interesse_particularidade)
