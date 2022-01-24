from dataclasses import dataclass

@dataclass
class chatbot:
    def print_data(self):
        return print()

while True:
    print('==-==' * 16)
    print('Olá! Bem vindo(a) à loja de payloads!\nAqui você pode escolher o melhor foguete para o lançamento de sua carga!')
    print('==-==' * 16)
    print('O que você quer fazer agora?')
    print('[1] - Mostrar produtos disponíveis\n[2] - Comprar produto\n[3] - Ver carrinho\n[4] - Área do administrador\n[0] - Sair da loja')
    try:
        print('==-==' * 16)
        choice = int(input('Sua escolha: '))
        if choice < 4 and choice >= 0:
            if choice == 0:
                print('==-==' * 16)
                print('Volte sempre!')
                break
        else:
            print('ERRO: Você deve escolher um dos números listados!')
    except:
        print('ERRO')
    

