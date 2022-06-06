print('------------------------------------------------------')
numero = int(input("Ingresa un número para imprimir la serie Fibonacci: "))
print('------------------------------------------------------')
#Forma Iterativa
def fibonacci(numero):
    a = 0
    b = 1    
    for k in range(numero):
        c = a + b
        a = b
        b = c
    return b

for x in range(numero):
    print(fibonacci(x))
print('------------------------------------------------------')
#Forma Recursiva    
def fibonacciRecursiva(numero):
    if numero<2:
        return numero
    return fibonacciRecursiva(numero-1)+fibonacciRecursiva(numero-2)


for x in range(numero):
    print(fibonacciRecursiva(x))
print('------------------------------------------------------')