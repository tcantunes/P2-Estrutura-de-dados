class Pessoa:
    def __init__(self, nome, contato, interesse_tipo,endereco,interesse_particularidade=None):
        self.nome = nome
        self.contato = contato
        self.interesse_tipo = interesse_tipo
        self.interesse_particularidade = interesse_particularidade
        self.endereco = endereco