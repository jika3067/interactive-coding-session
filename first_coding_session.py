print("hello world") #in our python file (also called a python script)
print("hello friend") #Final way of running Pythin code: Run a script in full

#What are the big variable types in python?
this_string = "jill" #this is a string. I assigned the value "jill" to the variable this string

this_float = 3.14 #float 
this_int = 12 #integer
this_bool = False #note the case sensitive 

#What can you do with variables?
#only after the line is executed do the variables exist in Python's memory
print(this_string) #tab to autocomplete code
print(this_float)

#what else can you print?
print(this_string) #you can print a variable
print(12) # you are not storing it into a variable, you are directly printing an input
print(12+5) #printing an expression
#SKILL: being able to 'trace the code'. meaning reconstruct the steps of the code
#another ex. of expression
print(this_float + 5) #here, we can trace the steps

#what is print()? it is a function. a function is a way of doing something in python
#functionos are called using()
#functions take a number of arguments (what goes in ())

#how many arguments does print() take?
#it can take one
print(this_float)
# but can it can take more
print(this_float, this_int, this_string)
# printing is printing all of its arguments on the same line

#calculations
print(2+3*5)


print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3) #floating point error. Operations with decimal numbers are, by default, not mathematically 'exact'

# How can we avoid this?
#one way is to round:
my_rounded_sum = round(0.1 + 0.2, 1)
print(my_rounded_sum)
print(my_rounded_sum == 0.3) #this is now true

#More logical comparisons:
print(1 < 2)
print(1>2)
print(1 >= 2)
print(1 <= 2)

print(1 != 2) #testing if things are different

# you can print more complex comparisons
print((1 < 2 and (3 > 2)))
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #both true, so true
print(condition_1 and condition_3), #False, so True 
#AND requires ALL conditions to be True
#What about OR
print(condition_1 or condition_2)
print(condition_1 or condition_3) #True, why? bc at least one of them is true
#OR requires AT LEAST ONE conition to be True

print(False + False) #its 0
print(False + True) #= 1
print(True + True) 
print(True == 1)
print(False == 0) 

print(False * 5) 
print(True *3+1) #simple stand in for 0 and 1

#lets continue the weirdness
greeting = "Hello" + "world!" #plus signs work differently when working with strings
print(greeting)
#+, when applied to strings, means CONCATENATION : bringing them into a single string

laugh = "ha" * 3
print(laugh) #Here, multiplication means repeat it when applied to a string
weird_laugh = "ha" * 3.14 #this does not work. can't multiply by an integer and a string 

my_age = 24
my_intro = "I'm Jill and I'm " + my_age #my_age is technically an integer so this command won't work
#when you want types to work nicely with each other, you will need to convert them first

#type conversions: 
my_age_string = "24" #this makes it a string
my_intro = "I'm Jill and I'm " + my_age_string
print(my_intro)

#a better way to do this is to convert one type to the other using 4 different function: str(), int(), bool()

#how we use them
print(str(39))
#is this really a string?:
type(str(39))
#trying others:
str(3.14)
str(False) #in terminal if it's a string you will get ' ' around it
str(0.1 + 0.2) #this is another error
#can convert almost anything to a string: int, bool, float

#Let's try float:
float('Hello') #doesnt work
float('32') #will have .0 at the end to show it's a float
float (False) #remember False is another term for 0
float(40)
#for float, it's sometimes going to work and sometimes not

#Int?
int('Hello') #can't do this
int(True)
int('32')
int(3.14) #is it rounding or cutting off the decimal?
int(3.9) #this is different than rounding. it just cuts off the decimal
round(3.9) #here we get 4

#ANOTHER GREAT SKILL: running experiments on your code
