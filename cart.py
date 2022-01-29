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
    
        buy = str(input('Foguete em que se deseja lançar: '))
        while True:
            try: 
                quantity = int(input('Quantidade de lançamentos desejada nesse foguete: '))
                if quantity > 0:
                    break
                else:
                    print('ERRO: A quantidade deve ser MAIOR que 0!')
            except:
                print('Digite um número inteiro!')
                pass
        if buy in rockets:
            with open('stock.txt') as doc:
                for line in doc:
                    if line.split('#')[0] == buy:
                        if int(line.split('#')[2]) - quantity >= 0:
                            totalCost = float(line.split('#')[1])
                            stock().remove_product(buy, 0, quantity)
                            with open('cart.txt', 'r') as dom:
                                if buy not in dom.read():#
                                    with open('cart.txt', 'a') as dom:
                                        dom.write(f'{buy}#{quantity}#{totalCost}\n')
                                    print(f'Lançamento no {buy} foi adicionado com sucesso!')
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
                            print('Não temos mais essa quantidade disponível em nosso estoque')
                    else:
                        pass     
        else:
            print('ERRO: Este item não está disponível!')
        return totalCost

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
            
'''
cart().add_to_cart()
cart().show_cart()
'''






