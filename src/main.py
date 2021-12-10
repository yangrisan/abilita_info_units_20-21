a=300
print (a)

import math
b=math.pi
print(b)
c=math.e
print(c)

var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])


a = "Hello"
c= a+a+a # Concatenation
print(c)

a = "He"+"l"*2+"o World" # Multiple concatenation
print(a)

a = "What’s your name?" # Ok if I create the string with double quotes
b = "What\’s your name?"  # Ok if you escape the single quote character
print (a)
print(b)

a = r"Hello \t World"
#Raw string
print(a)
 
name = "yan"
my_string = "ciao %s" % name # Append and Insert
my_string = "ciao %s, come stai? %s" % (name, 'bene') # Insert multiple values
print(my_string)

person = {"name": "yan", "age": 21}
print(f"{person['name']} is {person['age']} years old.")

s="Ciao Mondo"
d=s.replace('o','i',1)
print(d)

s = "Hello"
d=s.center(10,'.')
print(d)

d=s.upper()
print(d)