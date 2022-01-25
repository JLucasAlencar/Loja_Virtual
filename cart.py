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
                            print(f'{buy} foi adicionado ao carrinho!')
                            print(f'O custo total é de RS{totalCost:.2f}.')
                        else:
                            print('Não temos mais essa quantidade disponível em nosso estoque')
                    else:
                        pass     
        else:
            print('ERRO: Este item não está disponível!')
        #CRIAR FUNÇÃO DE MOSTRAR CARRINHO
          
cart().add_to_cart()






