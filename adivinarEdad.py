#El programa adivina la edad del usuario. Para ello genera un numero aleatorio en el rango entre 1 y 120
# le pregunta al usuario si esa es su edad.
# si elusuario dice que sí, termina el programa, e imprime la edad del usuario y la cantidad de intentos en los que adivinó 
# si dice que no hace un cilco en el cual pregunta al ausuario  si su edad es mayor que ese número,
# si dice que sí, lo guarda en la variable min, sino lo guarda en la variable max, para ir acotando poco a poco el rango de la edad hasta que la adivina
# una vez adivina la edad imprime la edad del usuario y la cantidad de intentos en los que adivinó 

import random

min=1
max=120
x=random.randint(min,max)
accion=input(f"Tu edad es {x} He adivinado? S/N")
contador=1
while accion.upper()=="N":
     aux= input(f"Tu edad es mayor que {x}?  S/N")
     if aux.upper()=="S":
        min=x+1
        x=random.randint(min,max)
     else:
        max=x-1
        x=random.randint(min,max)
     accion=input(f"Tu edad es {x} He adivinado? S/N")
     contador+=1
 
print(f"Tu edad es {x}")
print(f"He adivinado en  {contador} veces")