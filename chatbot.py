from cart import *
from stock import *

print(f'\033[1;36m{"==-==" * 16}')
print('\033[1;32mOlá! Bem vindo(a) à loja de payloads!\nAqui você pode escolher o melhor foguete para o lançamento de sua carga!')
while True:
    print(f'\033[1;36m{"==-==" * 16}') 
    print('\033[1;32mO que você quer fazer agora?')
    print('[1] - Mostrar produtos disponíveis\n[2] - Comprar produto\n[3] - Ver carrinho\n[4] - Área do administrador\n[0] - Sair da loja')
    try:
        print(f'\033[1;36m{"==-==" * 16}\033[1;33m')
        choice = int(input('Sua escolha: '))
        if choice <= 4 and choice >= 0:
            if choice == 1:
                stock().show_products()

            elif choice == 2:
                print('==' * 21)
                print(f'{"Comprar produto":^40}')
                print('==' * 21)
                cart().add_to_cart()

            elif choice == 3:
                cart().show_cart()

            elif choice == 4:
                print(f'\033[1;34m{"==-==" * 16}')
                print(f'\033[1;35m{"ÁREA DO ADMINISTRADOR":^80}')
                while True:
                    print(f'\033[1;34m{"==-==" * 16}')
                    print('\033[1;35m[1] - Adicionar foguete ao estoque\n[2] - Aumentar quantidade de lançamentos para um foguete\n[3] - Remover quantidade de lançamentos de um foguete\n[0] - Sair da área do administrador')
                    print(f'\033[1;34m{"==-==" * 16}\033[1;33m')
                    try:
                        choice4 = int(input('Sua escolha: '))
                        if choice4 <= 3 and choice4 >= 0:
                            if choice4 == 1:
                                print('==' * 21)
                                print(f'{"Adicionar foguete":^40}')
                                print('==' * 21)
                                product = str(input('Digite o nome do novo foguete: ')).replace(' ', '').lower()
                                price = float(input('Digite o preço da payload: '))
                                quantity = int(input('Digite a quantidade que ficará disponível em estoque: '))
                                stock().add_product(product, price, abs(quantity))
                            elif choice4 == 2:
                                print('==' * 21)
                                print(f'{"Aumentar quantidade":^40}')
                                print('==' * 21)
                                product = str(input('Digite o nome do foguete: ')).replace(' ', '').lower()
                                quantity = int(input('Digite em quanto quer aumentar: '))
                                stock().increase_quantity(product, abs(quantity))
                            elif choice4 == 3:
                                print('==' * 21)
                                print(f'{"Diminuir quantidade":^40}')
                                print('==' * 21)
                                product = str(input('Digite o nome do foguete: ')).replace(' ', '').lower()
                                quantity = int(input('Digite em quanto quer reduzir: '))
                                stock().remove_product(product, abs(quantity))
                            elif choice4 == 0:
                                break
                        else:
                            print('\033[1;31mERRO: Você deve escolher um dos números listados!')
                    except (ValueError, TypeError):
                        print('\033[1;31mERRO: Houve um problema com os tipos de dados que você digitou!')
                    except (KeyboardInterrupt):
                        print('\033[1;31mERRO: O usuário não informou dados.')

            elif choice == 0:
                with open('cart.txt', 'w') as era:
                    era.write('')
                print(f'\033[1;36m{"==-==" * 16}')
                print('\033[1;32mVolte sempre!\033[m')
                break
            else:
                pass
        else:
            print('\033[1;31mERRO: Você deve escolher um dos números listados!')
    except (ValueError, TypeError):
        print('\033[1;31mERRO: Houve um problema com os tipos de dados que você digitou!')
    except KeyboardInterrupt:
        print('\033[1;31mERRO: O usuário não informou dados.')

