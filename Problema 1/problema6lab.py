temperatura = int(input("Ingrese el valor de la temperuta: "))
if temperatura<10:
    print("El clima es frio")
elif temperatura > 11 and temperatura < 16:
    print("El clima es templado")
elif temperatura > 17 and temperatura < 24:
    print("El clima es calido")
elif temperatura > 24:
    print("El clima es tropical")
