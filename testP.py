import math
class exClass:
	man="Sukhdeep"
	height=6
	def yomethod(self):
		return 'hey man'
	def roti(self):
		return 'lolz'
	
exObject=exClass()
print exObject.man
print exObject.height
print exObject.yomethod()
print exObject.roti()
###################################################################
class nameit:
	def createName(self,name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print "hello %s" % self.name
		
firstName=nameit()
firstName.createName('Sukhdeep')
print firstName.displayName()
print firstName.saying()
########################################################################

# Self is a temporary place holder for the object name.
# Subclasses(Child Class) and Superclasses(Parent Class) : Inheriting all traits from one class to another


class parentClass:
	a="I am good"
	b="I am very good"
class childClass(parentClass):
	pass
aObject=parentClass()
bObject=childClass()
print aObject.b
print bObject.a
########################################################################
# Inheriting some traits from the parentClass to the childClass

class parentClass1:
	a='man'
	b='woman'
class childClass1:
	b='god'
pObject=parentClass1()
cObject=childClass1()
print pObject.b
print cObject.b

########################################################################
# Multiple parent classes
class mom:
	a='I am mother'
class dad:
	b= 'I am Father'
class child(mom,dad):
	c= 'I am creator'
childObject=child()
print childObject.a+childObject.b+childObject.c

########################################################################
# Constructor when called it automatically access the atrributes declared in a class unlike the methods where they need to be called
# When the new object is made calling the constructor class, it access all the attributes and prints out the values
class explainingConstructors:
	def __init__(self):
		print "This is good"
cObject=explainingConstructors()

########################################################################
# Modules store the variables that when imported can be accessed for later use

def testModu():
	print 'this is nice inne!!'

########################################################################
# Reloading Modules : Once a module is loaded in a file and some value is changed back there in back module, new value is not displayed as the module is already loaded and reload is used to get out of this.
#reload (testP) # This is should be done in the file calling it

########################################################################
# Getting module info, first import it and then get the info

dir(math)	 # Functions present in the module
help(math)	 # Detailed look into the module
math.__doc__ # Short info about the module
