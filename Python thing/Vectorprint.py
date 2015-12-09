import Vectors
from Vectors import *


a = Vector2(6,12)
b = Vector2(6,9)


print("------------------------------------------------------------")
print("THIS IS THE VECTOR 2 CALCULATOR")
print("The first Vector consists of (6,12)")
print("The second Vector consists of (6,9)")
print(" ")
c = a + b
print("Vector 1 + Vector 2 = ")
c.printer()

c = a - b
print("Vector 1 - Vector 2 = ")
c.printer()

c = a * b
print("Vector 1 * Vector 2 = ")
c.printer()

print("Vector 1's magnitude is ",a.Mag())
print("Vector 2's magnitude is ",b.Mag())

print("Vector 1 Normalized is ")
a.Norm().printer()
print("Vector 2 Normalized is ")
b.Norm().printer()

print("Vector 1's Dot Product is ",a.DProd(b))


print("Lerp is ")
a.lerp(b).printer()

print("------------------------------------------------------------")
a = Vector3(6,12,4)
b = Vector3(4,2,0)
print("THIS IS THE VECTOR 3 CALCULATOR")
print("The first Vector consists of (6,12,4)")
print("The second Vector consists of (4,2,0)")
print(" ")
c = a + b
print("Vector 1 + Vector 2 = ")
c.printer()

c = a - b
print("Vector 1 - Vector 2 = ")
c.printer()

c = a * b
print("Vector 1 * Vector 2 = ")
c.printer()
print(" ")
print("Vector 1's magnitude is ",a.Mag())
print("Vector 2's magnitude is ",b.Mag())
print(" ")


print("Vector 1 Normalized is ")
a.Norm().printer()
print("Vector 2 Normalized is ")
b.Norm().printer()
print(" ")
print("Vector 1's Dot Product is ",a.DProd(b))
print("Vector 2's Dot Product is ",b.DProd(b))
print(" ")
print("Lerp is ")
a.lerp(b).printer()
print(" ")




print("------------------------------------------------------------")
a = Vector4(1,7,3,8)
b = Vector4(1,8,0,6)
print("THIS IS THE VECTOR 4 CALCULATOR")
print("The first Vector consists of (1,7,3,8)")
print("The second Vector consists of (1,8,0,6)")
print(" ")
print("Vector 1 Normalized is ")
a.Norm().printer()
print("Vector 2 Normalized is ")
b.Norm().printer()
#def HexColor(object):
                                #red = int(object[:2], 16)
                                #green = int(object[2:4], 16)
                                #blue = int(object[4:6], 16)
                                #alpha = int(object[6:], 16)
                                #print(red,green,blue,alpha)

rory = Vector2(1,1)
print("rory is ", rory)

print("rory really is ")
rory.printer()