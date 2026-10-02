###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.


# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets=input("Quants paquets ha rebut el encamiador?\n")
print(f"L'encaminador ha rebut {1200+int(paquets)} paquets.")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat=input(("Quina es la velocitat de la connexió en Mbps?"))
print(f"La velocitat en MB/s és {float(velocitat)/8}.")