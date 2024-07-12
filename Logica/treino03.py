import random
cont=1
a=int(input("Digite 1 para rodar um dado, pressione 0 para sair: "))
while cont==1:
    if a==1:
        numero_aleatorio=random.randint(1,6)
        print("O número que saiu no dado foi",numero_aleatorio)
        a=int(input("Digite 1 para rodar um dado, pressione 0 para sair: "))
    elif a==0:
        cont=0
    else:
        print("Digite 1 ou 0")
        a=int(input("Digite 1 para rodar um dado, pressione 0 para sair: "))
print("FIM DO JOGO")