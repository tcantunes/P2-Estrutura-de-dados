from pessoa import *
from animal import *
from cadastroAnimal import *
from cadastroPessoa import *


def menu_principal():
    cadastro_animais = CadastroAnimais()
    cadastro_pessoas = CadastroPessoas()
    animais_disponiveis = cadastro_animais.animais
    pessoas_disponiveis = cadastro_pessoas.pessoas

    print('\n\33[1;35mSistema de Cadastro e Adoção\33[m')
    while True:
        print('\nMenu Principal:\n1. Cadastrar novo animal\n2. Cadastrar nova pessoa interessada na adoção\n'
              '3. Pesquisar animais disponíveis\n4. Pesquisar pessoa interessada na adoção\n5. Sair\n')
        escolha_menu = int(input('Informe sua opção: \n'))

        if escolha_menu == 1:
            cadastro_animais.cadastrar_animal()

        elif escolha_menu == 2:
            cadastro_pessoas.cadastrar_pessoa()

        elif escolha_menu == 3:
            if len(animais_disponiveis) >= 1:
                print('\nOs animais disponíveis para adoção possuem as seguintes características:\n')

                for animal in animais_disponiveis:
                    print(f'Tipo: {animal.tipo}\nIdade: {animal.idade}\nCor: {animal.cor}\n'
                          f'Porte: {animal.porte}\nRaça: {animal.raca}\nParticularidade: {animal.particularidade}\n')
            else:
                print('\nNão há animais disponíveis para adoção.\n')

        elif escolha_menu == 4:
            if len(pessoas_disponiveis) >= 1:
                print('\nAs pessoas adotantes cadastradas são:\n')
                for pessoa in pessoas_disponiveis:
                    print(f'Nome: {pessoa.nome}\nContato: {pessoa.contato}\nInteresse pelo tipo do animal: {pessoa.interesse_tipo}\n'
                          f'Endereço: {pessoa.endereco}\nInteresse por particularidade do animal: {pessoa.interesse_particularidade}\n')
            else:
                print('\nNão há cadastros de pessoas interessadas na adoção.\n')
        
        elif escolha_menu == 5:
            print('Programa finalizado.\n')
            break

        else:
            print('\nInforme uma opção válida.')
    
    return animais_disponiveis, pessoas_disponiveis


def pesquisar_caracteristica(animais, item, begin=0, end=None):
    lista = []
    for posicao, animal in enumerate(animais):
        lista.append([posicao, animal])
    
    if end is None:
        end = len(lista)-1
    if begin <= end:
        m = (begin + end)//2
        if lista[m][1].tipo == item:
            return m
        if item < lista[m][1].tipo:
            return pesquisar_caracteristica(animais, item, begin, m-1)
        else:
            return pesquisar_caracteristica(animais, item, m+1, end)
    return None

animais, pessoas = menu_principal()

interesse_tipo = input('Informe o interesse do TIPO do animal: ')
tipo_encontrado = pesquisar_caracteristica(animais, interesse_tipo)
if tipo_encontrado is not None:
    animal_encontrado = animais[tipo_encontrado]
    print(f'\nAnimal com este TIPO encontrado:\nTipo: {animal_encontrado.tipo}\nIdade: {animal_encontrado.idade}\nCor: {animal_encontrado.cor}\n'
          f'Porte: {animal_encontrado.porte}\nRaça: {animal_encontrado.raca}\nParticularidade: {animal_encontrado.particularidade}\n')
else:
    print('Não há animais cadastrados com este TIPO específico.')

