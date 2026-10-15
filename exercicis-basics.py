###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
nom="Paula"
ubi="Rubí"
print(f"El meu nom és {nom}.")
print(f"La meva ciutat és {ubi}.")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

print(int("12345"))
print(float("12345"))
print(int(3.99))#Si convertim un float en int el que passa és que eliminem els seus decimals, sense arrodonir ni res

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí

name='Paula'
age=19
print(f"Hola em dic {name} i tinc {age} anys.")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")


resultat=int(round(3.1416)/2)
print(resultat)

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temp_cel=float(input("Introdueix una temperatura en graus Celsius: "))

temp_f=(temp_cel * 9/5) + 32
print(f"La temperatura introduïda en celsius és {temp_cel}, i la seva conversió a fahrenheit és {temp_f}.")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total=float(input("Quin és el total de la compra?: "))
propina_perc=float(input("Quin és el percentatge de propina?: "))
propina=total*(propina_perc/100)
final=total+propina
print(f"El total sense la propina és {total:.2f}, i la propina sent del {propina_perc:.2f}% deixa al preu final a {final:.2f}.")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí