import math
from math import *
class Vector2():
		def __init__(self,ax,ay):
				self.x = ax
				self.y = ay
				
				
		def printer(self):
				print(self.x,",",self.y)
		def __add__(self, thing):
				result = Vector2(0,0)
				result.x = self.x + thing.x
				result.y = self.y + thing.y
				return result
			
		def __sub__(self, thing):
				result = Vector2(0,0)
				result.x = self.x - thing.x
				result.y = self.y - thing.y
				return result
		
		def __mul__(self, thing):
				result = Vector2(0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				return result
			    
		def Mag(self):
				result = Vector2(0,0)
				result.x = self.x ^ 2
				result.y = self.y ^ 2
				newresult = sqrt(result.x + result.y)
				return newresult

		def DProd(self,thing):
				result = Vector2(0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				newresult = (self.x * thing.x) + (self.y * thing.y)
				return newresult
			    

				
				
a = Vector2(2,4)
b = Vector2(6,9)
c = Vector2(0,0)


print("Vector 1 consists of (2,4)")
print("Vector 2 consists of (6,9)")
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

print("Vector 1's Dot Product is ",a.DProd(b))
print("Vector 2's Dot Product is ",b.DProd(b))


class Vector3():
		def __init__(self,ax,ay,az):
				self.x = ax
				self.y = ay
				self.z = az
				
		def printer(self):
				print(self.x,",",self.y,",",self.z)
		def __add__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x + thing.x
				result.y = self.y + thing.y
				result.z = self.z + thing.z
				return result
			
		def __sub__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x - thing.x
				result.y = self.y - thing.y
				result.z = self.z - thing.z
				return result
		
		def __mul__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				result.z = self.z * thing.z
				return result
			    
		def Mag(self):
				result = Vector3(0,0,0)
				result.x = self.x ^ 2
				result.y = self.y ^ 2
				result.z = self.z ^ 2
				newresult = sqrt(result.x + result.y + result.z)
				return newresult

		def DProd(self,thing):
				result = Vector3(0,0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				result.z = self.z * thing.z
				newresult = (self.x * thing.x) + (self.y * thing.y) + (self.z * thing.z)
				return newresult
				
		#def lerp(self,other,per):
                #result = Vector(0,0,0)
                #result.x = self.x + (per * (other.x - self.x))
                #result.y = self.y + (per * (other.y - self.y))
                #result.z = self.z + (per * (other.z - self.z))
                #return result
			    

				
				
a = Vector3(2,2,5)
b = Vector3(4,2,0)
c = Vector3(0,0,0)


print("Vector 1 consists of (2,2,5)")
print("Vector 2 consists of (4,2,0)")
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

print("Vector 1's Dot Product is ",a.DProd(b))
print("Vector 2's Dot Product is ",b.DProd(b))

#print("Lerp: ")
#result = a.lerp(b,.5)
#result.printer()
#print(" ")


#def HexColor(object):
                                #red = int(object[:2], 16)
                                #green = int(object[2:4], 16)
                                #blue = int(object[4:6], 16)
                                #alpha = int(object[6:], 16)
                                #print(red,green,blue,alpha)