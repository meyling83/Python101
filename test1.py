#a=10
#if a>10:
 #   print(f"la varialble a con valor {a} es mas que 10.")
#else:
 #   print(f"la varaiable a con valor {a} es menor o igual que 10")

#b=-1
#if b<100:
 #   print(f"la varialble b con valor {b} es menor que 100.")
#else:
  #  print(f"la varaiable b con valor {b} es mayor o igual que 100")

#b=int(input("introducir un valor"))
#if b<100:
 #   print(f"la varialble b con valor {b} es menor que 100.")
#else :
 #   print(f"la varaiable b con valor {b} es menor o igual que 100")
#else:
     #print(f"la varaiable b con valor {b} es  igual que 100")

#multiplicar por 10 el salario introducido y mostrar mensaje de cuanto puede ganar si fuera experto
#salario=float(input("introducir salario"))
#salario=salario*10
#print(f"puede ganar {salario} si fueras experto en python")

#sumar dos números introducidos por el usuario
#num1=int(input("introducir un número"))
#num2=int(input("introducir otro número"))
#suma=num1+num2
#print(f"La suma de los numeros es {suma}")

#calcular precio a pagar por cada persona dado el precio total y la cantidad de personas
#cntPersonas=int(input("introducir cantidad de personas"))
#precioTotal=float(input("introducir precio total de la compra"))
#precioPorPersona=precioTotal/cntPersonas
#print(f"Cada uno tiene que pagar {precioPorPersona:.2f}")

#convertir peso en Kilos o Libras

#accion=str(input("Introducir K si quiere convertir kilos en libras o L si quiere convertir libras en kilos"))

#if accion.upper()=="K":
    #kilos=float(input("Introducir peso en kilos"))
    #libras=kilos*2.2205
    ##print(f"{kilos} kilos son {libras} libras")
#elif accion.upper()=="L":
    #libras=float(input("Introducir peso en libras"))
    #kilos=libras/2.2205
    #print(f"{libras} libras son {kilos} kilos")
#else:
   # print(f"El valor introducido no es correcto")

#tipo de datos
#def numbers():
   # return 10,20,30
#a=numbers()
#type(a)
#print(f"El tipo de a es {type(a)}")
#a, b, c = numbers()
#print(f"El tipo de a es {type(a)}")
#print(f"El tipo de b es {type(b)}")
#print(f"El tipo de c es {type(c)}")

#convierte un decimal en entero
#accion=float(input("introducir un número"))
#resultado=int(accion)
#print(f"El mainframe espera {resultado}")

#convierte un decimal en entero otra via utilizando listas
#acciones=[3.234,4.655,7.333]
#for accion in acciones:
    #resultado=int(accion)
    #print(f"El mainframe espera {resultado}")

#Imprimir nombre introducido por el usuario 50 veces
""" nombre=str(input("¿Cúal es tu nombre?"))
for i in range(50):
    print(f"{nombre}") """

#imprimir cuenta ascendente o descendente
""" accion=str(input("¿Teclear 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?"))
if accion.upper()=="UP":
   numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
   for i in range(numeros_de_veces):
       print(f"{i}")
elif accion.upper()=="DOWN":
   numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
   for i in range(numeros_de_veces-1,-1,-1):
       print(f"{i}")
else:
   print(f"La acción introducida no es correcta") """

#Programa para gestionar los Invitados a la fiesta
""" gente=int(input("Cuanta gente acudira a la fiesta"))
max_invitados=5
if gente>max_invitados:
    print(f"Lo siento, solo {max_invitados} personas pueden acudir a la fiesta.")
else:
    for i in range(gente):
        nombre=str(input("Nombre del invitado"))
        print(f"Hola {nombre}.  Ha sido invitado a nuestra fiesta.") """

gente=int(input("Cuanta gente acudira a la fiesta"))
max_invitados=5
if gente>max_invitados:
    print(f"Lo siento, solo {max_invitados} personas pueden acudir a la fiesta.")
else:
    lista_nombres=[]
    for i in range(gente):
        nombre=str(input("Nombre del invitado"))
        lista_nombres.append(nombre)
    print(f"Hola {lista_nombres}.  Han sido invitados a nuestra fiesta.")
