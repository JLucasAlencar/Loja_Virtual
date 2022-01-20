from dataclasses import dataclass

'''
    The products are payloads of various rockets in history.

    Example:
    name: Saturn V
    Payload price: R$2000000000,00
'''

@dataclass
class product:
    name: str
    payload_price: float
    quantity: int

saturn_V = product('Saturn V', 200000000, 10)
falcon_9 = product('Falcon 9', 1000000, 20)
ariane_5 = product('Ariane 5', 10000000, 8)


listOfProducts = [saturn_V, falcon_9]

print(listOfProducts)

class stock:
    name: str
    payloadPrice: float
    quantity: int
    def add_product(self, name, payloadPrice, quantity):
        self.name = name
        self.payloadPrice = payloadPrice
        self.quantity = quantity
    #def show_products(self):
        
    #def buy_item(self, quantity):
add_product()



