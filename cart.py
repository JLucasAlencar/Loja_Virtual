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
            quantity = int(input('Quantidade de lançamentos desejada nesse foguete: '))
            if quantity > 0:
                break
            else:
                print('ERRO: A quantidade deve ser MAIOR que 0!')
        if buy in rockets:
            print(f'{buy} foi adicionado ao carrinho!')
            with open('stock.txt') as doc:
                for line in doc:
                    if line.split('#')[0] == buy:
                        totalCost += quantity*float(line.split('#')[1])
        else:
            print('ERRO: Este item não está disponível!')
        print(totalCost)
        #AGORA FALTA REMOVER O ITEM DE STOCK.TXT!   



cart().add_to_cart()






