#Let's first re create a variable for two
my_integer = 10
my_str = "Hello world"
#you can always see the type of variable by using type()
type(my_integer)
type(my_str)

#what is stored inside these objects?
my_str.upper #upper is a METHOD that is attachted to all the objects of class string
#a method is like a function, so it needs to be called. How do we call a function again?
#we put () after it
my_str.upper() #returning the upper, capitalized version f the string
my_str.upper() #what does it mean to return a copy? it means that the original string is unchange:
my_str

#lets try another:
my_str.lower() 
#What else is in there?
my_str.endswith('!') #this asks if this ends with an exclamation mark. which is no
my_str.endswith('orld') #returned True
#Methods are a way of pairing functions to specific types of objects

#some objects have other things than methods. They have properties
#Properties are information about the object that was created
my_integer.denominator #white wrenchs (you will see it after putting .) are properties of an object
my_integer.numerator #do not put ()
#properties are only meant to be read. they do not do anything. they just exist. if does not do anything, it is probably a property. but be sure to look at the icon
