from sqlalchemy import false
palavra_secreta = ["M", "U"]
letras_descoberta = []

print('Jogo da Forca')

for i in range(0, len(palavra_secreta)):
    letras_descoberta.append("-", )
    
acertou = False

while acertou == False:
    letra = str(input("Digite a letra: "))
    
    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descoberta[i] = letra
            
        print(letras_descoberta[i])
        
    acertou = True
    
    for x in range(0, len(letras_descoberta)):
        if letras_descoberta[x] == "-":
            acertou = False