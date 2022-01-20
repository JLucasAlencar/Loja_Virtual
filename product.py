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
    
saturn_V = product('Saturn V', 200000000)
print(saturn_V.name, saturn_V.payload_price)


    
