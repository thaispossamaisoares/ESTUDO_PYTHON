import string, random
from time import sleep

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    

titulo('BEM VINDO AO JOGO DO STOP SOLITARIO')
qtd_campo = int(input('quantos campos vai ter?'))

informacao = []
for quantidade in range(0,qtd_campo): 
    informacao.append(input("informe os campos: "))


if __name__ == '__main__':
    letra = random.choice(string.ascii_letters)
    print('A letra sorteada e: ' + letra)

    
valor = [] 
for quantidade in range(0,qtd_campo): 
    print(informacao )
    valor.append(input("informe valor: ")) 


print('-'*30)
 
print(informacao )
print(valor )
titulo('Fim da partida')


