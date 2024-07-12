a = int(input("0 - sair 1 - repetir: "))
b= 5
c=1
while b ==5:
    if a ==0:
        b =0
    elif a ==1:
        c+=1
        print(f"Nova tentativa, vc ta na tentativa {c}")
        a =int(input("0-Sair e 1-Repetir: "))
    else:
        c+=1
        print("DIGITE 1 OU 0!!!")
        print(f"Nova tentativa, vc ta na tentativa {c}")
        a=int(input("0-Sair e 1-Repetir: "))
print(f"Fim de jogo com {c} tentativas.")