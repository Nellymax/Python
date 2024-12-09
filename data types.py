
num=2.5
print(type(num)) #brings it's data type as a float

num=5
print(type(num))

#j means a square root of -1
num=6+7j
print(type(num))  #it's data type is complex

#play with data types like 
#converting a 'float' to an "int" data type
# "a" will be assigned with a float data type value 
#"b" will be assigned as an "int" data type value of "a" as seen
a=8.7
b= int(a)
print(type(b)) # the output data type wiil be an "int"

#converting a 'int' to a "float" data type
#"b" was assigned with an int data type value 
#"k" will be assigned as a "float" data type value of "b" as seen
k=float(b)
print(k)  # the value will be a float number/value

#converting a 'int' to a "complex" data type
#"k" will be assigned with an int data type value 
#"c" will be assigned as a "complex" data type value of "k" as seen
k=6
c=complex(b,k)
print(c)   #the output is a complex data type value

#using the data type of 'BOOL'
#in BOOL, ture is taken as "1" and false is taken as "0"
print(int(True))  #output is "1"
print(int(False))  #output is "0"
#in this data type we set a condition to see if its 'true' or 'false' as seen below
print(b<k) # output is false since the value of b is 8 which is greater than 6 the value of k
bool=b > k
print(bool)  #output is true

#list,tuple,set,string,range are all grouped under "SEQUENCE"
lst=[25,36,90,12,34]
print(type(lst))   #this a list

m={58,93,0,24,13,23}
print(type(m))    #this a set

u=(48,93,2,80,34,1,2)
print(type(u))   #this a tuple

w='maxensia'
print(type(w))  #this a string(str)

r=(20)
print(list (range(20)))  #brings all values from 0 to 20

#in case we want only even numbers we say
print(list(range(2,20,2))) # only the even values are output
#we need to specify the range difference for the even values as 2

print(type(range(20)))  #this a range


p=5
h=4
print(p<8 and h<5)