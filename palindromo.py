print("---------------------------")
print("Ingresa una palabra o frase: ")
palabra = input()
print("---------------------------")
# No reconoce los upercase o lowercase
print(palabra)
if(palabra) == (palabra)[::-1]:
    print("Palindromo")
else:
    print("No Palindromo")
print("---------------------------")
#Arreglando los lowercase:
print(palabra)
palabra = palabra.lower()
if(palabra) == (palabra)[::-1]:
    print("Palindromo")
else:
    print("No Palindromo")
print("---------------------------")
#Arreglando los espacios si son frases:
print(palabra)
palabra = palabra.lower()
palabra = palabra.replace(' ', '')
if(palabra) == (palabra)[::-1]:
    print("Palindromo")
else:
    print("No Palindromo")
print("---------------------------")

