#!/usr/bin/python2

def modularExp(base, exponent, modulo):
    res = 1
    pot = base % modulo
    while exponent > 0:
        if exponent % 2 == 1:
            res = (res * pot) % modulo        
        pot = (pot * pot) % modulo
        exponent >>= 1
    return res
