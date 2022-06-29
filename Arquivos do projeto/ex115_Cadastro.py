def menu():
    from time import sleep
    sleep(3)
    print(f'{" Menu de Cadastro ":-^100}')
    print('''\n[1] - Ver pessoas cadastradas\n[2] - Cadastrar nova pessoa\n[3] - Finalizar o sistema''')

    while True:

        with open('Cadastro.txt', mode='a', encoding='utf-8') as cadastro:

            opcao = ''
            while not opcao.isnumeric():

                try:

                    opcao = int(input('\nInsira uma das opções acima: '))
                    while opcao < 1 or opcao > 3:
                        opcao = int(input('Insira um dos valores acima: '))

                    break

                except:
                    print('\nAtenção: insira uma das opções acima:  ')

            if opcao == 1:
                print(f'\nSua opçao foi: Ver pessoas cadastradas\n')

                nomes_cadastrados = open('Cadastro.txt', mode='r', encoding="utf-8")
                pessoas_cadastradas = nomes_cadastrados.readlines()

                if len(pessoas_cadastradas) == 0:
                    print('\033[1;33mAinda não foram cadastradas pessoas!\033[m\n')
                else:
                    print(f'\033[1;33m{"Nome ":-<60}{" Idade":->30}\n')
                    for pessoas in pessoas_cadastradas:
                        nomes_idades = pessoas.split(';')
                        print(f'{nomes_idades[0]:<30} {nomes_idades[1]:>58}')
                    print('-' * 90, '\033[m\n')

            elif opcao == 2:
                print(f'\nSua opçao foi: Cadastrar nova pessoa')

                pessoa = '123456'
                while pessoa in '123456789/?><()*&¨%$#@!{}/][/ºª':

                    pessoa = input('Insira aqui o nome da pessoa: ').strip().title()

                idade = ''
                while not idade.isnumeric():
                    idade = input('Insira sua idade:')

                cadastro.write(pessoa)
                cadastro.write(';')
                cadastro.write(idade)
                cadastro.write('\n')

            else:
                print(f'\nSua opçao foi:\033[1;31m Sair do sistema')
                break


menu()
