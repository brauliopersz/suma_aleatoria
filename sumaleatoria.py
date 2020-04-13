# Este programa se encarga de generar dos numeros de manera aleatoria
# y el usuario tendra que adivinar cual es el resultado de la suma.
# de estos dos numeros.

import random

num1 = random.randint(1,10)
num2 = random.randint(2,4)

print(f"Cuanto es {num1} + {num2} ?")
respuesta = input()

if int (respuesta) == num1 + num2:
    print("Correcto")
else:
    print("Incorrecto")

