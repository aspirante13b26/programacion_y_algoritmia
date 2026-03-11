import random

secreto = random.randint(1, 20)
adivinanza = 0

print("¡Adivina el número del 1 al 20!")

while adivinanza != secreto:
    adivinanza = int(input("Tu intento: "))

    if adivinanza < secreto:
        print("Más alto...")
    elif adivinanza > secreto:
        print("Más bajo...")
    else:
        print(f"¡Correcto! El número era {secreto}.")
