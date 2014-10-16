#!/usr/bin/python2
"""
Register
Save the name and the public key.
"""
print "Content-type: text/html\n\n"

import cgi
import os

def register(name, e, n):
   f = open("registered.txt", 'r')
   for line in f:
      userdata = line.split()
      if name == userdata[0]:
         f.close()
         print """The username is not available. <a href="../index.html">Return</a>"""
         return False
   f = open("registered.txt", 'a')
   f.write(name + ' ' + e + ' ' + n + '\n')
   f.close()
   print "The user has been added."
   return True

args = cgi.FieldStorage()
if args.has_key("username") and args.has_key("e") and args.has_key("n"):
   username = args["username"].value
   e = args["e"].value
   n = args["n"].value
   result = register(username, e, n)
   if result == True:
      os.mkdir("users/"+username)
      print """
      <br>Username: %s
      <br>       e: %s
      <br>       n: %s
      <br><a href="login.py">Login with RSA</a>
      """%(username, e, n)

