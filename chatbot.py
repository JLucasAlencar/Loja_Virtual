from cart import *
from stock import *

print('==-==' * 16)
print('Olá! Bem vindo(a) à loja de payloads!\nAqui você pode escolher o melhor foguete para o lançamento de sua carga!')
while True:
    print('==-==' * 16)
    print('O que você quer fazer agora?')
    print('[1] - Mostrar produtos disponíveis\n[2] - Comprar produto\n[3] - Ver carrinho\n[4] - Área do administrador\n[0] - Sair da loja')
    try:
        print('==-==' * 16)
        choice = int(input('Sua escolha: '))
        if choice <= 4 and choice >= 0:
            if choice == 1:
                stock().show_products()

            elif choice == 2:
                cart().add_to_cart()

            elif choice == 3:
                cart().show_cart()

            elif choice == 4:
                print('==-==' * 16)
                print(f'{"ÁREA DO ADMINISTRADOR":^80}')
                while True:
                    print('==-==' * 16)
                    print('[1] - Adicionar foguete ao estoque\n[2] - Aumentar quantidade de lançamentos para um foguete\n[3] - Remover quantidade de lançamentos de um foguete\n[0] - Sair da área do administrador')
                    print('==-==' * 16)
                    choice4 = int(input('Sua escolha: '))
                    if choice4 <= 3 and choice4 >= 0:
                        if choice4 == 1:
                            print(f'{"Adicionar foguete":^40}')
                            print('==' * 21)
                            product = str(input('Digite o nome do novo foguete: '))
                            price = float(input('Digite o preço da payload: '))
                            quantity = int(input('Digite a quantidade que ficará disponível em estoque: '))
                            stock().add_product(product, price, abs(quantity))
                        elif choice4 == 2:
                            print(f'{"Aumentar quantidade":^40}')
                            print('==' * 21)
                            product = str(input('Digite o nome do foguete: '))
                            quantity = int(input('Digite em quanto quer aumentar: '))
                            stock().increase_quantity(product, abs(quantity))
                        elif choice4 == 3:
                            print(f'{"Diminuir quantidade":^40}')
                            print('==' * 21)
                            product = str(input('Digite o nome do foguete: '))
                            quantity = int(input('Digite em quanto quer reduzir: '))
                            stock().remove_product(product, abs(quantity))
                        elif choice4 == 0:
                            break

                    else:
                        print('ERRO: Você deve escolher um dos números listados!')
            elif choice == 0:
                with open('cart.txt', 'w') as era:
                    era.write('')
                print('==-==' * 16)
                print('Volte sempre!')
                break
            else:
                pass
        else:
            print('ERRO: Você deve escolher um dos números listados!')
    except:
        print('ERRO')

        #1 - CORRIGIR BUGS!
        #2 - COLOCAR CORES NO TERMINAL!

