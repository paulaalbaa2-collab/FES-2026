###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###


# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_t=input("Quin es el nom del tecnic?")
nom_x=input("Quin es el nom de la xarxa?")
print(f"El nom del tecnic es {nom_t} i el de la xarxa es {nom_x}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
long=float(input("Quina es la longitud d'un enllaç de fibra en quilometres?"))
vel=float(input("Quina es la velocitat de transissio en Gbps?"))
temps=(8/vel) 
print(f"Caldrien {temps: .2f} segons per transmetre 1 GB de dades a l'enllaç de {long} km.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores=float(input("Quantes hores de feina has fet?"))
preu_h=float(input("Quin es el preu per hora de la instal.lacio de xarxa?"))
preu_m=float(input("Quin es el preu del material?"))
cost_t=hores*preu_h+preu_m
print(f"El cost total de la instal.lacio es: {cost_t}")