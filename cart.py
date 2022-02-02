from dataclasses import dataclass
from stock import *

@dataclass
class cart:
    def add_to_cart(self): #Add an item to cart and removes it from "stock.txt"
        totalCost = 0
        rockets = []
        with open('stock.txt') as fo:
            for line in fo:
                rockets.append(line.split('#')[0])
    
        while True:
            buy = str(input('Foguete em que se deseja lançar: ')).replace(" ", "").lower()
            if buy in rockets:
                while True:
                    try: 
                        quantity = int(input('Quantidade de lançamentos desejada nesse foguete: '))
                        if quantity > 0:
                            break
                        else:
                            print('\033[1;31mERRO: A quantidade deve ser MAIOR que 0!\033[m')
                    except:
                        print('\033[1;31mDigite um número inteiro!\033[m')
                        pass
                break
            elif buy == '0':
                break
            else: 
                print('\033[1;31mERRO: Este item não está disponível!(Digite 0 para voltar ao menu)\033[1;33m')
        
        with open('stock.txt') as doc:
            for line in doc:
                if line.split('#')[0] == buy:
                    if int(line.split('#')[2]) - quantity >= 0:
                        totalCost = float(line.split('#')[1])
                        stock().remove_product(buy, quantity)
                        with open('cart.txt', 'r') as dom:
                            if buy not in dom.read():#
                                with open('cart.txt', 'a') as dom:
                                    dom.write(f'{buy}#{quantity}#{totalCost}\n')
                                print(f'\033[1;33mLançamento no \033[4m{buy}\033[m \033[1;33mfoi \033[1;32madicionado com sucesso!\033[1;33m')
                            else:
                                counter = 0
                                with open('cart.txt') as dom:
                                    for line in dom:
                                        if line.split('#')[0] == buy:
                                            add = str(quantity + int(line.split('#')[1]))
                                            with open('cart.txt', 'r') as bo:
                                                listOfLines = bo.readlines()
                                                listOfLines[counter] = f'{buy}#{add}#{totalCost}\n'
                                            with open('cart.txt', 'w') as bo:
                                                bo.writelines(listOfLines)         
                                        else:
                                            counter += 1
                    else:
                        print('\033[1;31mInfelizmente não temos mais essa quantidade disponível em nosso estoque.\033[1;33m')
                else:
                    pass     
        
            

    def show_cart(self):
        print('==' * 21)
        print(f'{"CARRINHO":^40}')
        print('==' * 21)
        print('Produtos', ' '*5, 'No carrinho', ' '*2, 'Custo de um')
        print('==' * 21)
        with open('cart.txt', 'r') as car:
            tCost = 0
            for line in car:
                prod = line.split('#')[0]
                quant = line.split('#')[1]
                price = line.split('#')[2]
                tCost += float(line.split('#')[2]) * int(quant)
                print(f'{prod: <15}{quant: <15}{price}')
                print('--' * 21)
            print(f'Preço total: {tCost}')
            







