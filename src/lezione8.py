import numpy as np
a=np.array([[1,2],[2,2]])
print(a.shape)
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b.shape)



import numpy as np
a = np.array([1,2,3,4])
list1 = [1,2,3,4]
tupla = (5,6,7,8)
a = np.array(list) # from a list
print(a)
b = np.array(tupla) # from a tupla
print(b)
c = np.array([list1,tupla])
print(c)



b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))



a=np.arange(25)
a=a.reshape((5,5)) 
print(a)
print(a[::,1])
print(a[1])
print(a[1,:])
print(a[1,::])
print(a[1,::2])
print(a[1,10::-1])



v1=np.array([1,2,3])
v2=np.array([10,20,30])
print(v1*v2)
print(np.dot(v1,v2))



a = np.ones(4)
print(a)
b = np.arange(1,5)
print(b)
a+=b 
print(a)
print('a[0] ', a[0])
a[1:3]=a[1:3]*3 # Modify the elements from 1 to 3
print(a)



a=np.arange(5)
a: [0,1,2,3,4]
b=a
b[0]=100
print ("a:", a , "b:" , b)



a=np.arange(6) ; a
np.array([0, 1, 2, 3, 4, 5])
b=a[2:5] ; b
np.array([2, 3, 4])
b[0]=40 
b[1]=50
print ('a:', a , 'b:', b )
