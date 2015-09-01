#coding=utf8
#Librería de funciones aritméticas

import itertools as itools
import math

Factoriales=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,\
  479001600, 6227020800, 87178291200, 1307674368000, 20922789888000,\
  355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]

Primos=[ 2,        3,        5,        7,       11,       13,       17,       19]
L=[23,       29,       31,       37,       41,       43,       47,       53,\
        59,       61,       67,       71,       73,       79,       83,       89,\
        97,      101,      103,      107,      109,      113,      127,      131,\
       137,      139,      149,      151,      157,      163,      167,      173,\
       179,      181,      191,      193,      197,      199,      211,      223,\
       227,      229,      233,      239,      241,      251,      257,      263,\
       269,      271,      277,      281,      283,      293,      307,      311,\
       313,      317,      331,      337,      347,      349,      353,      359,\
       367,      373,      379,      383,      389,      397,      401,      409,\
       419,      421,      431,      433,      439,      443,      449,      457,\
       461,      463,      467,      479,      487,      491,      499,      503,\
       509,      521,      523,      541,      547,      557,      563,      569,\
       571,      577,      587,      593,      599,      601,      607,      613,\
       617,      619,      631,      641,      643,      647,      653,      659,\
       661,      673,      677,      683,      691,      701,      709,      719,\
       727,      733,      739,      743,      751,      757,      761,      769,\
       773,      787,      797,      809,      811,      821,      823,      827,\
       829,      839,      853,      857,      859,      863,      877,      881,\
       883,      887,      907,      911,      919,      929,      937,      941,\
       947,      953,      967,      971,      977,      983,      991,      997]

ConjuntoPrimos=set(Primos)  # Para determinar pertenencia de manera más eficiente

def factorial(n):
    """Función para calcular factoriales,  usando tabla precalculada
    para valores pequeños"""
    if n<1: return 1
    r=len(Factoriales)
    if n<r:
        return Factoriales[n]
    else:
        p=Factoriales[-1]
        for k in xrange(r,n+1):
            p=p*k
            Factoriales.append(p)
        return p

# Inicializamos algunas factorizaciones comunes
Factorizaciones={ p:{p:1} for p in Primos}
for a in range(5):
    for b in range(5):
        for c in range(5):
            n=(2**a)*(3**b)*(5**c)
            Factorizaciones[n]={2:a,3:b,5:c}


def factoriza(n):
    """Factoriza un entero positivo, regresando un diccionario de
    primos y exponentes. Almacena en memoria factorizaciones conocidas para
    acelerar factorizaciones posteriores"""

    if n in Factorizaciones:
        # Si ya conocemos la factorización, no necesitamos recalcular
        return Factorizaciones[n]

    F=dict()
    if n in ConjuntoPrimos:
        # ¿Redundante? Las factorizaciones de primos las conocíamos
        F[n]=1   # Añadimos  {n:1} al diccionario.
        Factorizaciones[n]=F   #
        return F

    MaxPrimo=Primos[-1]

    for p in Primos:
        if n%p==0:  #  Si encontramos un divisor primo:
            m=n//p   # n = m*p
            F=factoriza(m)  # Factoriza el cociente
            if len(F)==0:
                return
            # Para evitar excepción por clave inválida
            if p in F:      # Si aparece otro factor p...
                F[p]=F[p]+1 # ...aumenta el exponente en 1
            else:
                F[p]=1      # Si no, crea la clave
            print("adding", n,F)
            Factorizaciones[n]=F
            return F
    if MaxPrimo*MaxPrimo < n:
        print("NO PUEDO FACTORIZAR")
        return dict()
    else:   # Enconramos un nuevo primo
        return {n:1}

print(factoriza(2**11+1))
print(factoriza(2049))
#print(Factorizaciones)
