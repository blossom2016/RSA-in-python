# -*- coding: utf-8 -*-
"""Lastone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wlQy674K0MWngmVPyKTmJ6_4zLNzL6mn
"""

import random

'''
Euclid's algorithm for determining the greatest common divisor

'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))
  '''
  This function is to encrypt a message
  '''

def encrypt(pk, m):
    
    key, n = pk
    cipher = (int(m) ** int(key)) % n 
    return cipher
'''
 This function is to  decrypt a message
 '''
def decrypt(pk, c):
    key, n = pk
    plain = c ** key % n
    return plain

print ("RSA Encrypter/ Decrypter")
p = int(input("Enter a prime number (17, 19, 23, etc): "))
q = int(input("Enter another prime number (Not one you entered above): "))
print ("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print ("Your public key is ", public ," and your private key is ", private)
message = input("Enter a message to encrypt with your private key: ")
encrypted_msg = encrypt(private, message)
print ("Your encrypted message is: ")
print (encrypted_msg)
print ("Decrypting message with public key ", public ," . . .")
print ("Your message is:")
print (decrypt(public, encrypted_msg))

'''1993	2161	2371	2579
1997	2179	2377	2591
1999	2203	2381	2593
2003	2207	2383	2609
2011	2213	2389	2617
2017	2221	2393	2621
2749	2957	3187	3373
2753	2963	3191	3389
2767	2969	3203	3391
2777	2971	3209	3407
2789	2999	3217	3413
2791	3001	3221	3433
2797	3011	3229	3449
2801	3019	3251	3457
2803	3023	3253	3461
2819	3037	3257	3463
2833	3041	3259	3467
2837	3049	3271	3469
2843	3061	3299	3491
2851	3067	3301	3499
2857	3079	3307	3511
2861	3083	3313	3517
2879	3089	3319	3527
2887	3109	3323	3529
2897	3119	3329	3533
2903	3121	3331	3539
2909	3137	3343	3541
2917	3163	3347	3547
2927	3167	3359	3557
2939	3169	3361	3559
2953	3181	3371	3571


'''