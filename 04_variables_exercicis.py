###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom=input("Quin es el nom de l'encaminador?")
ubi=input("Quina es la seva ubicacio?")
ports=input("Quin es el nombre de ports?")
estat=input("Esta ON o OFF?")

print(f"L'encaminador es diu {nom}, esta a {ubi}, te {ports} ports i esta {estat}. ")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
pla_dades=input("Quins son els GB inclosos al pla?")
consumits=input("Quins son els GB consumits?")
totals=int(pla_dades)-int(consumits)

consumits=input("Quins son els GB consumits ara?")
totals=int(pla_dades)-int(consumits)
