n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))

print(" 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. División\n 5. Cociente\n 6. Residuo")
print(" 7. Salir")
op = input("Selecciona una operación: ")

while True:
    if op == "1":
        print("{}+{} = {}".format(n1, n2, n1+n2))
    elif op == "2":
        print("{}-{} = {}".format(n1, n2, n1-n2))
    elif op == "3":
        print("{}*{} = {}".format(n1, n2, n1*n2))
    elif op == "4":
        print("{}/{} = {}".format(n1, n2, n1/n2))
    elif op == "5":
        print("{}/{} = {}".format(n1, n2, n1/n2))
    elif op == "6":
        print("{}%{} = {}".format(n1, n2, n1%n2))
    elif op == "7":
        break
    else: 
        print("La opción no es válida")
    print(" 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. División\n 5. Cociente\n 6. Residuo")
    print(" 7. Salir")
    op = input("Selecciona una operación: ")
