from dataclasses import dataclass

@dataclass
class chatbot:
    def print_data(self):
        return print()

while True:
    chatbot()
    print('#' * 100, '\n Olá! Bem vindo(a) à loja de payloads! \n Aqui você pode escolher o melhor foguete para o lançamento de sua carga!', '\nO que você quer fazer agora?')
    print('[1] - Ver carrinho', '[2] - Mostrar produtos', '[3] - Remover produto do carrinho', '[4] - Área do administrador', '[0] - Sair da loja')
    choice = int(input('Sua escolha:'))
    if choice == 0:
        print('#' * 100, '\nVolte sempre!')
        break

