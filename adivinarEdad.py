import random

min=1
max=99
x=random.randint(min,max)
accion=input(f"Tu edad es {x} He adivinado? S/N")
lista=[]
contador=0
while accion.upper()=="N":
     aux= input(f"Tu edad es mayor que {x}?  S/N")
     if aux.upper()=="S":
        min=x
        x=random.randint(min,max)
     else:
        max=x
        x=random.randint(min,max)
     if(x not in lista):
        accion=input(f"Tu edad es {x} He adivinado? S/N")
        lista.append(x)
     contador+=1
     
   

print(f"Tu edad es {x}")
print(f"He adivinado en  {contador} veces")