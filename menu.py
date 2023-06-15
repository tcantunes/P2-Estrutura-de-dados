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


animais, pessoas = menu_principal()

lista_animais, lista_pessoas = animais, pessoas

def pesquisa_tipo_animais(animais, item):
    lista_animais = []
    for posicao, animal in enumerate(animais):
        if animal.tipo == item:
            lista_animais.append(animal)
    return lista_animais

def pesquisa_tipo_pessoa(pessoas, item):
    lista_pessoas = []
    for posicao, pessoa in enumerate(pessoas):
        if pessoa.interesse_tipo == item:
            lista_pessoas.append(pessoa)
    return lista_pessoas

buscar_interesse = input('Deseja fazer uma busca pelo TIPO de animal de preferência? [SIM | NÃO]\n')
if not (buscar_interesse.lower() == 'sim' or buscar_interesse.isspace()):
    print('Busca finalizada.\n')
else:
    buscar_tipo = input('Informe o interesse pelo TIPO de animal: ')

    animais_encontrados = pesquisa_tipo_animais(animais, buscar_tipo)
    animais_relatorio = []
    if animais_encontrados:
        print(f'\nAnimais com o tipo {buscar_tipo.upper()} encontrados:')
        for animal in animais_encontrados:
            animais_relatorio.append(animal)
            print(f'Tipo: {animal.tipo}\nIdade: {animal.idade}\nRaça: {animal.raca}\n')
    else:
        print(f'\nAnimal com o tipo {buscar_tipo.upper()} não cadastrado.\n')

    pessoas_encontradas = pesquisa_tipo_pessoa(pessoas, buscar_tipo)
    pessoas_relatorio = []  
    if pessoas_encontradas:
        print(f'\nPessoas interessadas no tipo {buscar_tipo.upper()} encontradas:')
        for pessoa in pessoas_encontradas:
            pessoas_relatorio.append(pessoa)
            print(f'Nome: {pessoa.nome}\nContato: {pessoa.contato}\nInteresse pelo tipo: {pessoa.interesse_tipo}\n')
    else:
        print(f'Pessoa interessada no tipo de animal {buscar_tipo.upper()} não cadastrada.\n')

    if animais_encontrados and pessoas_encontradas:
        emitir_relatorio = input('Deseja emitir RELATÓRIO de informações entre animais disponíveis x possíveis candidatos? [SIM | NÃO]\n')
        if not (emitir_relatorio.lower() == 'sim' or emitir_relatorio.isspace()):
            print('Emissão de relatório recusada.')
        else:
            print('\n--- RELATÓRIO ---\n')
            print('\nANIMAIS DISPONÍVEIS PARA ADOÇÃO:')
            for animal in animais_relatorio:
                print('-'*30)
                print(f'Tipo: {animal.tipo}\nIdade: {animal.idade}\nCor: {animal.cor}\n'
                    f'Porte: {animal.porte}\nRaça: {animal.raca}\nParticularidade: {animal.particularidade}\n')

            print('\nPOSSÍVEIS CANDIDATOS PARA REALIZAREM A ADOÇÃO:')
            for pessoa in pessoas_relatorio:
                print('-'*30)
                print(f'Nome: {pessoa.nome}\nContato: {pessoa.contato}\nInteresse pelo tipo do animal: {pessoa.interesse_tipo}\n'
                    f'Endereço: {pessoa.endereco}\nInteresse por particularidade do animal: {pessoa.interesse_particularidade}\n')
                
