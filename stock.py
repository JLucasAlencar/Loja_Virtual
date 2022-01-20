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
    name: str 
    payloadPrice: float 
    quantity: int 
    def add_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self. quantity = quantity
        add = open('stock.txt', 'a')
        add.write(f'{self.name}#{self.payloadPrice}#{self.quantity}' + '\n')
        add.close()
    def remove_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self. quantity = quantity
        with open('stock.txt') as fo:
            for line in fo:
                if line.split('#')[0] == self.name:
                    a = int(line.split('#')[2])
                    newQuantity = a - removeRocketQuantity
                    line.split('#')[2] = str(newQuantity)
                


            
        
    #def show_products(self):
        
    #def buy_item(self, quantity):

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
removeRocketQuantity = int(input('Quantidade a ser comprada: '))

removeProduct = stock(removeRocketName, removeRocketQuantity)


'''
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




