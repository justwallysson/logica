import random
print("JOGO DO PALPITE")
tentativa=0
cont=1
numero_aleatorio=random.randint(1,100)
while cont>0:
    numero_usuario=int(input("Palpite um número entre 1 e 100: "))
    if numero_usuario==0:
        cont=0
    elif numero_usuario>=1 and numero_usuario<=100:
        if numero_usuario < numero_aleatorio:
            tentativa+=1
            print("O número sorteado é maior")
        elif numero_usuario > numero_aleatorio:
            tentativa+=1
            print("O número sorteado é menor")
        elif numero_usuario == numero_aleatorio:
            tentativa+=1
            print(f"Parabens, você acertou o número com {tentativa} tentativas")
            cont=0
    elif numero_usuario>100:
        tentativa+=1
        print("ERROR: Digite um número menor ou igual a 100")
print("Fim do programa")