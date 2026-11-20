###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

num = 10
while num>=1:
    print(num)
    num=num-1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

num=2
compt=0

while num <=20:
    if num % 2 ==0:
        compt+=num
        num+=num
    else:
        num+=num

print(f"La suma de números parells és: {compt}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

num=int(input("Introdueix un número enter positiu: "))
compt=1
acum=1

while compt<=num:
    acum=acum*compt
    compt=compt+1
    
print(f"El factorial del número {num} és {acum}.")
    

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contr= input("Introdueix una contrasenya: ")

while len(contr) < 8:
    print("Constrasenya de mida incorrecte, mínim 8 caràcters.")
    contr=input("Introdueix una contrasenya: ")
    
print("Constrasenya correcta.")
    


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num=int(input("Introdueix un número: "))
compt=1

while compt<=10:
    taula=compt*num
    print(taula)
    compt=compt+1
    


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

num=int(input("Introdueix un número enter positiu: "))
a=2
while a<=num:
        b=2
        primer=True
        while b<a:
            if b%a==0:
                primer=False
                break
            else:
                b += 1
        print(a)
        a += 1
                
     

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

num=int(input("Introdueix números enters: "))
sum=0

while num != 0:
    sum+=sum

print(f"La suma és: {sum}.")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

num=input("Introdueix un numero enter positiu:")
i=1
xifres=0

while i<=len(num):
    xifres+=xifres
    i+=i

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

cops=int(input("Quants termes de la seqüència de fibonacci vols saber?: "))
compt=0
anterior=0
actual=1


while compt<cops:
    print(anterior)
    seguent=anterior+actual
    anterior=actual
    actual=seguent
    compt+=compt

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

num=7
supo=int(input("Introdueix el número que tu estimes que és el secret: "))
if supo==num:
    print("S'ha encertat.")
    
else:
    if supo<num:
        print("No s'ha encertat i el número introduït és més petit que el secret, torna a intentar-ho.")
    else:
        print("No s'ha encertat i el número introduït és més gran que el secret, torna a intentar-ho.")
     
    