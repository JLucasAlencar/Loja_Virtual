from dataclasses import dataclass

'''
    The products are payloads of various rockets in history.

    Example
    name: Saturn V
    Payload price: R$2000000000,00
    Quantity: 10
'''

@dataclass
class stock:
    #Add a new product to stock
    def add_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self.quantity = quantity
        with open('stock.txt', 'r') as add:
            listOfRockets = []
            for line in add:
                listOfRockets.append(line.split('#')[0])
            if self.name not in listOfRockets and self.name != '': 
                with open('stock.txt', 'a') as add:
                    add.write(f'\n{self.name}#{self.payloadPrice:.2f}#{self.quantity}')
                    print('Operação realizada com \033[1;32msucesso!\033[m')
            else:
                print('\033[1;31mEsse item já está no estoque!\033[m')

    def increase_quantity(self, name=0, quantity=0):
        self.name = name
        self.quantity = quantity
        with open('stock.txt') as inc:
            counterInc = 0
            for line in inc:
                if line.split('#')[0] == self.name:
                    increase = int(line.split('#')[2]) + self.quantity
                    with open('stock.txt', 'r') as bo:
                        sp = line.split('#')[1]
                        listOfLines = bo.readlines()
                        listOfLines[counterInc] = f'{self.name}#{sp}#{increase}\n'
                    with open('stock.txt', 'w') as bo:
                        bo.writelines(listOfLines)
                        print('Operação realizada com \033[1;32msucesso!\033[m')
                else:
                    counterInc += 1

    #Remove a product
    def remove_product(self, name=0, quantity=0):
        self.name = name
        self.quantity = quantity
        with open('stock.txt') as fo:
            counterRem = 0
            listNames = []
            for line in fo:
                listNames.append(line.split('#')[0])
            if self.name not in listNames:
                print('\033[1;31mEste item não se encontra no estoque.\033[m')
            else: 
                with open('stock.txt') as fo:
                    for line in fo:
                        if line.split('#')[0] == self.name:
                            a = int(line.split('#')[2]) - quantity
                            plP = line.split('#')[1]
                            if a >= 0:
                                with open('stock.txt', 'r') as bo:
                                    listOfLines = bo.readlines()
                                    listOfLines[counterRem] = f'{self.name}#{plP}#{a}\n'
                                with open('stock.txt', 'w') as bo:
                                    bo.writelines(listOfLines)
                                    print('Operação realizada com \033[1;32msucesso!\033[m')
                            else:
                                print('ERRO: Não há quantidade suficiente do produto no estoque!')

                        else:
                            counterRem += 1
    def show_products(self):
        with open('stock.txt') as co:
            print('==' * 21)
            print(f'{"ESTOQUE":^40}')
            print('==' * 21)
            print('Produtos', ' '*5, 'Preço', ' '*10, 'Quantidade')
            print('==' * 21)
            for line in co:
                products = line.split('#')[0]
                price = line.split('#')[1]
                quantity = line.split('#')[2]
                print(f'{products: <15}R${price: <15}{quantity}')
                print('--' * 21)





