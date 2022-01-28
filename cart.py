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
                            totalCost += quantity*float(line.split('#')[1])
                            stock().remove_product(buy, 0, quantity)
                            with open('cart.txt', 'r') as dom:
                                if buy not in dom.read():
                                    with open('cart.txt', 'a') as dom:
                                        dom.write(f'{buy}#{quantity}\n')
                                else:
                                    counter = 0
                                    with open('cart.txt') as dom:
                                        for line in dom:
                                            if line.split('#')[0] == buy:
                                                add = str(quantity + int(line.split('#')[1]))
                                                with open('cart.txt', 'r') as bo:
                                                    listOfLines = bo.readlines()
                                                    listOfLines[counter] = f'{buy}#{add}\n'
                                                with open('cart.txt', 'w') as bo:
                                                    bo.writelines(listOfLines)         
                                            else:
                                                counter += 1
                                    pass
                                    
                            print(f'O custo dessa compra é de RS{totalCost:.2f}.')
                        else:
                            print('Não temos mais essa quantidade disponível em nosso estoque')
                    else:
                        pass     
        else:
            print('ERRO: Este item não está disponível!')
        return totalCost

    def show_cart(self):
        print('==' * 21)
        print('CARRINHO')
        print('==' * 21)
        with open('cart.txt', 'r') as car:
            for line in car:
                prod = line.split('#')[0]
                quant = line.split('#')[1]
                print(f'{prod: <15}{quant: <15}')
                print('--' * 21)
        #ADICIONAR CUSTO TOTAL DA COMPRA NO TXT E CHAMÁ-LO
            

cart().add_to_cart()
cart().show_cart()







