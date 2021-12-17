a=[0,1,2,3,4,5,6,7]
print(a[0:6])
b=[0,1,2,3,4,5,6,7]
print(b[1:6:2])
# no ‘stop’ means until the end of list
c=[0,1,2,3,4,5,6,7]
print (c[1::2])
 # no ‘start’ means from the first item of the list
d=[0,1,2,3,4,5,6,7]
print(d[::2])
#Slicing can be also negative
e=[0,1,2,3,4,5,6,7]
# starts fom index 6, ends to index 0 going back with step 2
print(e[6:0:-2])


g=[0,1,2,3,4,5,6,7]
g=list(range(3))
print(g)
c=type(a)
print(c)
d=list(range(1,10))
print(d)
e=list(range(1,10,2))
print(e)


import time
l=list(range(1000000))
v=list(range(10000))
T1=time.perf_counter()
l.extend(v)
T2=time.perf_counter()
print(T2-T1)

T1=time.perf_counter()
l+v
T2=time.perf_counter()
print(T2-T1)

T1=time.perf_counter()
l.extend(v)
T2=time.perf_counter()
print("extend execution time:", T2-T1 , "s")


stack=[1, 2, 3, 4]
print("Initial Stack : ", stack)
for i in range(5,7):
 stack.append(i)
print ("Append: ", stack)
stack.pop()
print ("Pop: " , stack)
queue=[ "a","b","c","d" ]
print("Initial Queue : ", queue)
queue.append("e")
queue.append("f")
print("Append : ", queue)
queue.pop(0)
print("Pop : ", queue)


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0]) # access to single element
print("tup2[1:5]: ", tup2[1:5]) # access to slice

my_dict = {"name":"Jack", "age": 26}
print(my_dict["name"]) # Output: Jack
print(my_dict.get("age")) # Output: 26
# Trying to access keys which doesn't exist throws error (try)
# my_dict.get('address')
# my_dict['address']

my_dict = {"name":"Jack", "age": 26}
# update value
my_dict["age"] = 27
#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)
# add item
my_dict["address"] = "Downtown"
print(my_dict)


#s=list(range(1,9,1))
#print(s[2],s[6],s[1])
#t=[el*2 for el in s]
#print(s)
#print(t)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#l=[1,2]
#l2=["a","b"]
#l3=[4,5,6]
#f=[]

#for e1 in l:
 #for e2 in l2:
  #for e3 in l3:
  #f.append ((e1,e2,e3))
  #print(f)



# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# remove a particular item
print(squares.pop(4)) # Output: 16
print(squares) # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item
print(squares.popitem()) # Output: (1, 1)
print(squares) # Output: {2: 4, 3: 9, 5: 25}
# delete a particular item


number = 23
guess = int(input('Enter an integer : '))
if guess == number:
 # New block starts here
 print("Congratulations, you guessed it.")
 print("(but you do not win any prizes!)")
 # New block ends here
elif guess < number:
 # Another block
 print("No, it is a little higher than that")
 # You can do whatever you want in a block ...
else:
 print("No, it is a little lower than that")
 # you must have guessed > number to reach here
print("Done")
# This last statement is always executed,
# after the if statement is executed.


number = 23
running = True
while running:
    guess = int(input("Enter an integer : "))
    if guess == number:
        print("Congratulations, you guessed it.")
 # this causes the while loop to stop
        running = False
    elif guess < number:
        print("No, it is a little higher than that.")
    else:
        print("No, it is a little lower than that.")
else:
    print("The while loop is over.")
 # Do anything else you want to do here
print("Done")


while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')




