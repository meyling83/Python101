#Programa para calcular el precio sin IVA o con IVA dado el porcentaje de IVA

print(f"Bienvenido a Calculadora IVA")
accion=str(input("Introducir S si desea Sumar IVA o Q si desea Quitar IVA"))
if(accion.upper()=="S"):
    precioSinIva=float(input("Introduzca el precio sin IVA"))
    porcentajeIva=float(input("Introduzca el porcentaje de IVA"))
    iva=porcentajeIva*precioSinIva/100
    precioConIva=precioSinIva+iva
    print(f"Resultado")
    print(f"Precio sin IVA: {precioSinIva:.2f} €")
    print(f"IVA: {iva:.2f} €")
    print(f"Precio con IVA: {precioConIva:.2f} €")
elif (accion.upper()=="Q"):
    precioConIva=float(input("Introduzca el precio con IVA"))
    porcentajeIva=float(input("Introduzca el porcentaje de IVA"))
    precioSinIva=precioConIva*100/(100+porcentajeIva)
    iva=precioConIva-precioSinIva
    #precioSinIva=precioConIva-iva
    print(f"Resultado")
    print(f"Precio sin IVA: {precioSinIva:.2f} €")
    print(f"IVA: {iva:.2f} €")
    print(f"Precio con IVA: {precioConIva:.2f} €")
else: 
      print(f"La acción no es válida")
