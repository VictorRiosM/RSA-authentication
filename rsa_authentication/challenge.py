#!/usr/bin/python2

def f(xc, n):
    return (xc**2 + 1) % n

def modularExp(base, exponent, modulo):
    res = 1
    pot = base % modulo
    while exponent > 0:
        if exponent % 2 == 1:
            res = (res * pot) % modulo
        exponent >>= 1
        pot = (pot * pot) % modulo
    return res

def challenge():
    xc = input("Enter xc: ")
    s = input("Enter s: ")
    e = 141257
    n = 407921
    fxc = f(xc, n)
    fs = modularExp(s, e, n)
    print "fxc:", fxc
    print "fs: ", fs
    if fxc == fs:
        print "The server is valid"
    else:
        print "It is not the server"
    
challenge()
