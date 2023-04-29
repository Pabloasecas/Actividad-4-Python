print("¡Hola!, escriba un número")
primer_numero = int(input())
print("Escriba otro número")
segundo_numero = int(input())
if primer_numero > segundo_numero:
    print("El", primer_numero, "es mayor al", segundo_numero)
elif primer_numero == segundo_numero:
    print("El", primer_numero, "es igual al", segundo_numero)
else:
    print("El", primer_numero, "es menor al", segundo_numero)
if (segundo_numero % 2 == 0):
    print("El", segundo_numero, "es par")
else:
    print("El", segundo_numero, "es impar")
