from dataclasses import dataclass

'''
    The products are payloads of various rockets in history.

    Example:
    name: Saturn V
    Payload price: R$2000000000,00
    Quantity: 10
'''

@dataclass
class stock:
    name: str = ''
    payloadPrice: float = 0
    quantity: int = 0
    #Add a new product to stock
    def add_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self.quantity = quantity
        add = open('stock.txt', 'a')
        add.write(f'{self.name}#{self.payloadPrice}#{self.quantity}' + '\n')
        add.close()
    #Remove a product
    def remove_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self.quantity = quantity
        with open('stock.txt') as fo:
            counter = 0
            for line in fo:
                if line.split('#')[0] == self.name:
                    self.payloadPrice = line.split('#')[1]
                    a = int(line.split('#')[2]) - quantity
                    with open('stock.txt', 'r') as bo:
                        listOfLines = bo.readlines()
                        listOfLines[counter] = f'{self.name}#{self.payloadPrice}#{a}\n'
                    with open('stock.txt', 'w') as bo:
                        bo.writelines(listOfLines)
                else:
                    counter += 1
    def show_products(self):
        with open('stock.txt') as co:
            print('==' * 21)
            print('Produtos', ' '*5, 'Preço', ' '*10, 'Quantidade')
            print('==' * 21)
            for line in co:
                products = line.split('#')[0]
                price = line.split('#')[1]
                quantity = line.split('#')[2]
                print(f'{products: <15}R${price: <15}{quantity}')
                print('--' * 21)

    
'''
#On Chatbot(To add new products to stock):
rocketName = str(input('Nome do foguete: '))
rocketPayloadPrice = float(input('Preço da Payload: R$'))
rocketQuantity = int(input('Quantidade disponível: '))

newProduct = stock(rocketName, rocketPayloadPrice, rocketQuantity)
newProduct.add_product(rocketName, rocketPayloadPrice, rocketQuantity)
openDocument = open('stock.txt', 'r')
with open ('stock.txt') as fo:
    for line in fo:
        print(line.split('#')[0])

#On chatbot(To remove a product)
removeRocketName = str(input('Digite o nome do produto que deseja comprar: '))
removeRocketName = removeRocketName.replace(" ", "").lower()
removeRocketQuantity = int(input('Quantidade a ser comprada: '))
print(removeRocketName)
removeProduct = stock(removeRocketName, 0, removeRocketQuantity)
removeProduct.remove_product(removeRocketName, 0, removeRocketQuantity)

new_product = stock()
new_product.name = str(input('Digite o nome do foguete: '))
new_product.payloadPrice = float(input('Digite o preço da payload: '))
new_product.quantity = int(input('Quantidade disponível do produto: '))


with open('stock.txt') as fo:
    for line in fo:
        print(line.split('#')[2])
a = int(line.split('#')[2])
print(a+1)
'''

show = stock()
show.show_products()




