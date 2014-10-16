#!/usr/bin/python2
"""
Login
"""
print "Content-type: text/html\n\n"
import cgi
from random import randint
from modularExp import modularExp

def fs(xc, ns):
    return (xc**2 + 1) % ns

def generax(username):
    f = open("registered.txt", 'r')
    for line in f:
       user = line.split()
       uname = user[0]
       e = int(user[1])
       n = int(user[2])
       if uname == username:
           x = randint(2, n-1)
           f.close()
           return x, e, n
    f.close()
    return 0, 0, 0

fields = cgi.FieldStorage()
if fields.has_key("username") and fields.has_key("xc"):
   username = fields["username"].value
   xc = int(fields["xc"].value)
   x, e, n = generax(username)
   f = open("rsa.private", 'r')
   privatekey = f.readline().split(",")
   f.close()
   ds = int(privatekey[0])
   ns = int(privatekey[1])
   s = modularExp(fs(xc, ns), ds, ns)
   if n != 0:
      print """
      <h2>Insert s : signed f(x)</h2>
      <form name="login" id="login" action="prove.py">
      Enter this value as s while running challenge.py
      <br>fs:   <input type="text" size="10" name="fs" value="%s" readonly>
      <br><br>Enter f(x), i.e. run the script using this number as x.
      <br>x:    <input type="text" size="10" name="x" id="x" value="%s" readonly>
      <br>user: <input type="text" size="10" name="username" value="%s" readonly>
      <br>e:    <input type="text" size="10" name="e" id="e" value="%s" readonly>
      <br>n:    <input type="text" size="10" name="n" id="n" value="%s" readonly>
      <br>S:    <input type="text" size="10" name="s" id="s" required="True">
      <br><input type="submit">
      </form>
      <br><a href="../fx.py">Download the script that generates the signed f(x).</a>
      """ %(s, x, username, e, n)
   else:
      print """
      <br>User doesn't exist or xc has not been introduced.
      <br><a href="../index.html">Registro</a>
      """
else:
    print """
    <h1>Login</h1>
    <form name="user" id="user" action = "login.py">
    <br>User: <input type="text" size="10" name="username" id="username" required="True">
    <br>Use this python script <a href = "../challenge.py">Challenge the server</a>
    <br>Challenge the server, enter a number xc, then compute xc**2+1. Finally, verify the answer of the server using its public key.
    <br>Enter xc: <input type="text" size="20" name="xc" required="True">
    <input type="submit">
    </form>
    """

