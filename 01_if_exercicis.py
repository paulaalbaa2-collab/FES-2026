###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num1=int(input("Introdueix un nombre: "))
num2=int(input("Introdueix un altre nombre: "))

if num1>num2:
    print("El primer nombre és més gran.")
elif num2>num1:
    print("El segon nombre és més gran.")
else:
    print("Els nombres són iguals.")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num1=float(input("Introdueix un nombre: "))
num2=float(input("Introdueix un altre nombre: "))
op=input("Introdueix una operació: '+', '-', '*', '/': ")

if op=='+':
    total=num1+num2
elif op=='-':
    total=num1-num2
elif op=='*':
    total=num1*num2
elif op=='/':
    if num2==0:
        print("No es pot dividir entre zero.")
    else:
        total=num1/num2
else:
    print("Operació no vàlida.")

print(f"El total de l'operació {op} entre el primer número {num1} i el segon {num2} és {total}.")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any=int(input("Introdueix un any de traspàs: "))

if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:

    print("És any de traspàs.")
    
else:
    print("No és any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat=int(input("Introdueix una edat: "))

if edat<0:
    print("Valor d'edat incorrecte.") 
elif edat>=0 and edat <=2:
    print("és un nadó.")
elif edat>=3 and edat<=12:
    print("És un infant")
elif edat >=13 and edat<=17:
    print("és un adolescent.")
elif 18<=edat<= 64:
    print("és un adult.")
else:
    print("és una persona gran.")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

senyal=float(input("Demana el nivell de senyal"))

if senyal>=-50:
    print("Excel.lent.")
elif -67>=senyal<-50:
    print("Bona.")
elif -75<=senyal<=-67:
    print("Feble.")
else:
    print("Molt feble.")

    
# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

pot=float(input("Introdueix la potència òptica rebuda: "))

if -27<=pot<=-8:
    print("Acceptable.")
elif pot<-27:
    print("Massa baix.")
else:
    print("Massa alt.")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum=float(input("Introdueix el consum de dades: "))

if 0<=consum<=20:
    print("Dins del límit.")
elif consum>20:
    exces=consum-20
    print(f"El consum ha sobrepassat el límit per {exces:.2f} gb.")
else:
    print("Valor no vàlid.")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los=int(input("L'indicador LOS del terminal òptic està encès (1) o apagat (0)?: "))
ro=int(input("L'indicador d'Internet està encès (1) o apagat (0)?: "))
 
if los:
    print("Cal revisar el cable de fibra.")
elif not ro:
    print("Cal comprovar el servei del proveïdor")
else:
    print("Sembla que funciona correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bat=int(input("Introdueix el percentatge de bateria disponible al SAI: "))

if 0>bat or bat>100:
    print("Valors fora del rang")
elif bat<20:
    print("Crític")
elif bat<50:
    print("Baix")
else:
    print("Suficient")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.



# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

ro=int(input("El router està encès? si(1), no(0): "))
los=int(input("L'indicador los del terminal òptic està encès? si(1), no(0): "))
int=int(input("l'indicador d'Internet del router està encès?: si(1), no(0): "))

if not ro:
    print("Cal encendre el router.")
else:
    if los:
        print("Cal revisar el cable de fibra.")
    elif int:
        print("Cal contactar amb el proveïdor.")
    else:
        print("Connexió funciona correctament.")


# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

inc=int(input("La incidència afecta a un sevrei crític? sí (1), no(0): "))
usu=int(input("Nombre d'usuaris afectats: "))
alt=int(input("Hi ha alguna alternativa de connexió dipsonible? sí (1), no(0): "))

if usu<0:
    print("Valor d'usuaris introduit no vàlid.")
    usu=int(input("Nombre d'usuaris afectats: "))

if (inc and not alt) or (usu>=50 and not alt) :
    print("Prioritat crítica.")
elif usu>=10 or inc:
    print("Prioritat alta.")
else:
    print("Prioritat baixa.")