#mi primer repositorio
num1=float(input("ingrese numero"))
num2=float(input("ingrese numero"))
op=True
while op:
    print("ingrese una opcion" \
    "1) sumar" \
    "2) restas" \
    "3) multiplicar" \
    "4) dividir" \
    "5) salir")
    opcion=input("ingrese una opcion")
    if opcion=="1":
        valor=num1+num2
        print(valor)
    elif opcion=="2":
        valor=num1-num2
        print(valor)
    elif opcion=="3":
        valor=num1*num2
        print(valor)
    elif opcion=="4":
        valor=num1/num2
        print(valor)
    elif opcion=="5":
        op=False
print("adios")