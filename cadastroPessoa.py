from pessoa import *


class CadastroPessoas():
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, nome, contato, interesse_tipo, endereco, interesse_particularidade=None):
        pessoa = Pessoa(nome, contato, interesse_tipo, endereco, interesse_particularidade)
        self.pessoas.append(pessoa)

