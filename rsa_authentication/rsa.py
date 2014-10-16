#!/usr/bin/python2
"""
RSA Algorithm
Creates public and private keys
"""
from random import randint
from random import SystemRandom
from math import sqrt

def getPrime(bits):
   i = 2
   rand = SystemRandom()
   prime = rand.getrandbits(bits)
   primesqrt = sqrt(prime)
   while i <= primesqrt:
      if prime % i == 0:
         i = 1
         prime = rand.getrandbits(bits)
         primesqrt = sqrt(prime)
      i += 1
   return prime

def egcd(a, b):
   a, b = (max(a, b), min(a, b))
   if a % b == 0:
      return (b, 0, 1)
   c, x, y = egcd(b, a % b)
   return (c, y, x - (a//b)*y)

def rsa():
   try:
      p = getPrime(int(argv[1]))
      q = getPrime(int(argv[1]))
   except:
      p = getPrime(10)
      q = getPrime(10)
   n = p * q
   phin = (p - 1) * (q - 1)
   c = 2
   while c != 1:
      e = randint(2, n-1)
      if phin > e:
         c, x, d = egcd(phin, e)
         h = x * phin + d * e
      else:
         c, d, x = egcd(phin, e)
         h = x * e + d * phin
   if d < 0:
      d %= phin
   print "h=", h, c

   publicKey = (e, n)
   privateKey = (d, n)

   print "Public Key:", publicKey
   print "Private Key:", privateKey
   print "In the public key the first value is e and the second is n."
   print "Don't share your private key. The first value is d. The second is n."
      
   f = open("rsa.keys", 'w')
   f.write("Public:" + str(publicKey) + ' ')
   f.write("Private: " + str(privateKey) + '\n')
   f.close()

rsa()
