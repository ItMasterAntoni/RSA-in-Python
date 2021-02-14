#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#RSA in Python by Antoni Szymanski 2021
#License: Freeware
#**************************************

import random

def ned(p,q):
    'calculating keys'
    z = (p-1) * (q-1) #calculation of auxiliary variable 'z'
    e = ue(z) #calling a function that calculates the public key
    d = ud(z,e) #calling a function that calculates the private key
    return [p*q,e,d]

def ue(z):
    'computing the public key'
    for x in range(2,z):
        if NWD(x,z) == 1 and x % 2 != 0:
            return x

def ud(z,e):
    'computing the private key'
    return mmi(z,e)

def NWD(a,b):
    'greatest common divisor'
    if b > 0:
        return NWD(b, a%b)
    else:
        return a

def mmi(z,e):
    'modular multiplicative inverse'
    if NWD(e,z) == 1:
        for x in range(0,z):
            if ((e * x) % z) == 1:
                return x
    else:
        return 'ERROR'

def miller_rabin(n,k):
    'miller-rabin prime test'
    if n == 1 or n == 2 or n == 3 or n % 2 == 0:
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        if n == 1:
            return False
    else:
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = spm(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = spm(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

def spm(a,b,n):
    '(a ** b) mod n'
    bits = bin(b)[2:]
    m = len(bits)
    out = 1
    x = int(a % n)
    for i in range(m-1,-1,-1):
        if bits[i] == '1':
            out = out * int(x % n)
        x **= 2
        x = int(x % n)
    return int(out % n)

def main():
    print('RSA in Python by Antoni Szymanski 2021')
    print('License: Freeware')
    print('**************************************')
    prime1 = int(input('Enter a prime number other than 2 (11,13,17,23...) '))
    while miller_rabin(prime1,20) == False:
        prime1 = int(input('Enter a prime number other than 2 (11,13,17,23...) '))
    prime2 = int(input('Enter a other prime number '))
    while miller_rabin(prime2,20) == False:
        prime2 = int(input('Enter a other prime number '))
    keys = ned(prime1,prime2)
    print('Your public keys are:',[keys[0],keys[1]])
    print('Your private keys are:',[keys[0],keys[2]])
    mode = input('Do you want to encrypt or decrypt (0/1)? ')
    if mode == '0':
        what = int(input('What you want to encrypt? '))
        print('Your encrypted number is',spm(what,keys[1],keys[0]))
    if mode == '1':
        what = int(input('What you want to decrypt? '))
        print('Your decrypted number is',spm(what,keys[2],keys[0]))
    print('\n**************************************')
    print('Thanks for using my script')
    print('The next ones are coming soon')
    
main()
