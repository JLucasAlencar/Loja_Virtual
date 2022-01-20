from dataclasses import dataclass

'''
    The products are payloads of various rockets in history.

    Example:
    name: Saturn V
    Payload price: R$2000000000,00
    Quantity: 10
'''

@dataclass
class product:
    name: str
    payload_price: float
    quantity: int

class stock:
    name: str
    payloadPrice: float
    quantity: int
    def add_product(self, name=0, payloadPrice=0, quantity=0):
        self.name = name
        self.payloadPrice = payloadPrice
        self.quantity = quantity
        
    #def show_products(self):
        
    #def buy_item(self, quantity):
new_product = stock()
new_product.name = str(input('Digite o nome do foguete: '))
new_product.payloadPrice = float(input('Digite o preço da payload'))
new_product.quantity = int(input('Qunatidade disponível do produto'))


with open('stock.txt') as fo:
    for line in fo:
        print(line.split('#')[2])
a = int(line.split('#')[2])
print(a+1)




