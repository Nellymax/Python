# every value has an address 
#the command for finding the address is "print(id(the value we want to find the address for))"
num=5
print(id(num))

# finding the address of strings
name= 'maxensia'
print(id(name))

#wen finding the address of the same value
a=10
b=a
print(a)  

print(b) #will bring an output has 10 since a & b are equal to each other(have the same value/number)

#both will output the same address as seen below
print(id(a))
print(id(b))
print(id(10))
# even if we change a and make it any other letter like m 
#the address will be the same since in the database 10 has address already 
#m refers to 10 has its value
m=10
print(id(m))

#in case we change the address of a
a=7
print(id(a))   #this address changes since a has be assigned a different value thus the address changing
#the new address of 'a' doesn't effect the address of 'b' since 'b' is still assigned to the value of 10 as seen
print(id(b)) #the address remains the same as before

#in cases in future we change the value of 'm' being equal to 'a', the new address of'a' will be the address of 'm' as seen
m=a
print(id(m))

#using constants in python
#in constants we use capital letters
#constants don't change
PI =3.14
print(PI)

#in case we want to know the type of variable(data type) we do the following command
#the command is "print(type(the value whose data type we want to find))"
print(type(PI))
print(type(m))

