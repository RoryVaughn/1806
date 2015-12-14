import math
from math import *
class Vector2():
		def __init__(self,ax,ay):
				self.x = ax
				self.y = ay
				
		#This is the print fuction for Vector 2		
		def printer(self):
				print(self.x,self.y)
		#This is the Addition fuction for Vector 2
		def __add__(self, thing):
				result = Vector2(0,0)
				result.x = self.x + thing.x
				result.y = self.y + thing.y
				return result
		#This is the Subtraction fuction for Vector 2	
		def __sub__(self, thing):
				result = Vector2(0,0)
				result.x = self.x - thing.x
				result.y = self.y - thing.y
				return result
		#This is the Multipication fuction for Vector 2
		def __mul__(self, thing):
				result = Vector2(0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				return result
		#This is the Magnitude fuction for Vector 2	    
		def Mag(self):
				result = Vector2(0,0)
				newresult = sqrt((self.x * self.x) + (self.y * self.y))
				return newresult
		#This is the Normilization fuction for Vector 2
		def Norm(self):
				result = Vector2(0,0)
				magresult = sqrt((self.x * self.x) + (self.y * self.y))
				result.x = self.x/magresult
				result.y = self.y/magresult
				return result
		#This is the Dot Product fuction for Vector 2
		def DProd(self,thing):
				result = Vector2(0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				newresult = (self.x * thing.x) + (self.y * thing.y)
				return newresult
		def lerp(self, thing):
				result = Vector2(0,0)
				result.x = self.x + 0.5 * (thing.x - self.x)
				result.y = self.y + 0.5 * (thing.y - self.y)
				return result

			    

				
				



class Vector3():
		def __init__(self,ax,ay,az):
				self.x = ax
				self.y = ay
				self.z = az
		#This is the print fuction for Vector 3		
		def printer(self):
				print(self.x, self.y, self.z)
		#This is the Addition fuction for Vector 3	
		def __add__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x + thing.x
				result.y = self.y + thing.y
				result.z = self.z + thing.z
				return result
		#This is the Subraction fuction for Vector 3		
		def __sub__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x - thing.x
				result.y = self.y - thing.y
				result.z = self.z - thing.z
				return result
		#This is the Multiplication fuction for Vector 3	
		def __mul__(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				result.z = self.z * thing.z
				return result
		#This is the Magnitute fuction for Vector 3		    
		def Mag(self):
				result = Vector3(0,0,0)
				result.x = self.x * self.x
				result.y = self.y * self.y
				result.z = self.z * self.z
				newresult = sqrt(result.x + result.y + result.z)
				return newresult
		#This is the Normalization fuction for Vector 3	
		def Norm(self):
				result = Vector3(0,0,0)
				magresult = sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
				result.x = self.x/magresult
				result.y = self.y/magresult
				result.z = self.z/magresult
				return result
		#This is the Dot product fuction for Vector 3	
		def DProd(self,thing):
				result = Vector3(0,0,0)
				result.x = self.x * thing.x
				result.y = self.y * thing.y
				result.z = self.z * thing.z
				newresult = (self.x * thing.x) + (self.y * thing.y) + (self.z * thing.z)
				return newresult
		def lerp(self, thing):
				result = Vector3(0,0,0)
				result.x = self.x + 0.5 * (thing.x - self.x)
				result.y = self.y + 0.5 * (thing.y - self.y)
				result.z = self.z + 0.5 * (thing.z - self.z)
				return result
class Vector4():
		def __init__(self,ax,ay,az,ar):
				self.x = ax
				self.y = ay
				self.z = az	
				self.r = ar
		#This is the print fuction for Vector 4		
		def printer(self):
				print(self.x, self.y, self.z, self.r)
		#This is the Normalization fuction for Vector 4	
		def Norm(self):
				result = Vector4(0,0,0,0)
				magresult = sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.r * self.r))
				result.x = self.x/magresult
				result.y = self.y/magresult
				result.z = self.z/magresult
				result.r = self.r/magresult
				return result
				

