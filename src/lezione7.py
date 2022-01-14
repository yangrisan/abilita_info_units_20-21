# the script takes from the user two input parameters
import sys
while(True):
    print('PLEASE INSERT AN INTEGER NUMBER IN THE RANGE 0-10')
    param1 = input()
    if int(param1) in range(11): 
        while(True):
            print( 'PLEASE INSERT A CHAR PARAMETER IN [A,B,C]')
            param2 = input()
            if param2 in ['A','B','C']:
                print('uso I due parametri passati dall utente: ',param1,param2)
                sys.exit()
            else: print('TRY AGAIN PLEASE')
    else: print('TRY AGAIN PLEASE')



import math 

def f(y):
    if y >= 0.0:
        return y**5*(math.exp(-y))
    else:
        return 0.0

infile='src/mydata.dat'
outfile='src/myout.dat'

indata = open( infile, 'r')
linee=indata.readlines()
indata.close()
processati=[ ]
x=[ ]
for el in linee:
    valori = el.split()
    x.append(float(valori[0])); y = float(valori[1])
    processati.append(f(y))

outdata = open(outfile, 'w')
i=0
for el in processati:
    outdata.write('%g %12.5e\n' % (x[i],el))
    i+=1
outdata.close()



l = []
with open('src/input1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append(map(int, line.split(',')))
print(l)



fin = open('src/input1.txt','r')
a=[]
for line in fin.readlines():
    a.append( [ int (x) for x in line.split(',') ] )



with open('src/input2.txt', 'r') as f:
    data = f.readlines() # read raw lines into an array

cleaned_matrix = [] 
for raw_line in data:
    split_line = raw_line.strip().split(",") # ["1", "0" ... ]
    nums_ls = [int(x.replace('"', '')) for x in split_line] # get rid of the quotation marks and convert to int
    cleaned_matrix.append(nums_ls)

print(cleaned_matrix)



# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)



# Program to multiply two matrices using list comprehension
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
for r in result:
    print(r) 



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()



class MyClass:
    def __init__(self, name, age):
        self.attribute1 = value1
        self.attribute2 = value2
    def myfunc(self):
        print('Hello my attribute1 is '+ self.attribute1)



x = range(3, 6)
for n in x:
 print(n)



x = range(3, 20, 2)
for n in x:
 print(n) 



a = ("Marco", "Luca", "Claudio")
b = ("Giovanna", "Maria", "Anna", "Francesca")
x = zip(a, b) 
print(tuple(x))



coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list)
c, v = zip(*result_list)
print('c =', c)
print('v =', v)



string='Hello World!''
print(lambda string : print(string))