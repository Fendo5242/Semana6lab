monto = int(input("Ingrese monto "))
if monto<100:
    print("no hay comision")
else:
    if monto<300:
        print("La comision es ",monto*0.10)
    else:
        print("La comision es ",monto*0.20)