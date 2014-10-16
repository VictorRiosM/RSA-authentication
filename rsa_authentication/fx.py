#!/usr/bin/python2

from sys import argv

def f(x, n):
   return (x**2 + 3*x + 5) % n

def modularExp(base, exponent, modulo):
   res = 1
   pot = base % modulo
   while exponent > 0:
      if exponent % 2 == 1:
         res = (res * pot) % modulo
      exponent = exponent >> 1
      pot = (pot * pot) % modulo
   return res

def sfx():
   try:
      x = int(argv[1])
      d = int(argv[2])
      n = int(argv[3])
   except:
      x = input("Introduce x: ")
      d = input("Introduce d: ")
      n = input("Introduce n: ")
   y = f(x, n)
   s = modularExp(y, d, n)
   print "f(x): ", y
   print "Signed f(x): ", s, "\n Write this value in the login form"
   return s

s = sfx()
      
