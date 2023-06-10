from pessoa import *
from animal import *
from cadastroAnimal import *
from cadastroPessoa import *


def menu_principal():
    cadastro_animais = CadastroAnimais()
    cadastro_pessoas = CadastroPessoas()

    print("Sistema de Cadastro e Adoção")
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar novo animal")
        print("2. Cadastrar nova pessoa interessada na adoção")
        print("3. Pesquisar animais disponíveis")
        print("4. Pesquisar pessoa interessada na adoção")
        print("5. Sair")
        escolha_menu = int(input('Informe sua opção: \n'))

        if escolha_menu == 1:
            cadastro_animais.cadastrar_animal()

        elif escolha_menu == 2:
            cadastro_pessoas.cadastrar_pessoa

        elif escolha_menu == 3:
            
            animais_disponiveis = cadastro_animais.animais
            if len(animais_disponiveis) >= 1:
                print('\nOs animais disponíveis para adoção possuem as seguintes características:\n')

                for animal in animais_disponiveis:
                    print(f'Tipo: {animal.tipo}\n Idade: {animal.idade}\n Cor: {animal.cor}\n '
                        f'Porte: {animal.porte}\n Raça: {animal.raca}\n Particularidade: {animal.particularidade}\n')
            
            else:
                print('\nNão existem animais disponíveis para adoção.\n')

        elif escolha_menu == 4:
            return cadastro_pessoas.pessoas
        
        elif escolha_menu == 5:
            print('Programa finalizado.')
            break

        else:
            print('\nInforme uma opção válida.')


menu_principal()
