a = int(input("Escribe el costo total de la compra: "))
if a > 1000:
    descuento = a * 0.20
    compratotal = a - descuento
    print("El total a pagar es ",compratotal)
else:
    print("El total a pagar es ",a)
