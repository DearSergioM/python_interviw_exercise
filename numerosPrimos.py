print('--------------------------------')
numero = int(input("Ingesa un número: "))

def primo(numero):
    if numero == 1:
        return "No es primo"
    elif numero == 2:
        return "Es primo"
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return "No es primo"
        return "Es primo"
    
for i in range(1,numero + 1):
    print(i,primo(i))

print('--------------------------------')