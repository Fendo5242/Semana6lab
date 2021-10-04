Operacion = input("Ingrese la inicial de la operacion que desea realizar (Suma-S; Resta-R; Multiplicacion-M; Division-D) ")
a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))

if Operacion == 'S' :
    print("La suma es ",a+b)
elif Operacion == 'R' :
    print("La resta es ",a-b)
elif Operacion == 'M' :
    print("La multiplicacion de los numeros es ",a*b)
elif Operacion == 'D':
    print("La division es ",a/b)
elif b == 0:
    print("No se puede realizar por un error")
