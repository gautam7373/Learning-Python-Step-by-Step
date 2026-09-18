#operator in Python
#Arithmatic Ops = +, -, /, *, **
#Comparison Operators --> ==, /=, <, >, <=, >=
#Logical --> and, or, not

#Lets start-------------

x= 10
y= 2
print("so here we are taking 2 numbers, x=10, & y=2, let's run all the possible arithmatic operators")
print("sum (x+y) is = ", x+y)
print("product (x*y) is = ", x*y)
print("divsion (x/y) is = ", x/y)
print("reminder (x%y) of the above division is is = ", x%y)
print("x to the power of y (x**y) is = ", x**y)
print("I hope you liked it.. <3 ")

#Comparision--
print("------------", "\n", "lets do some comparisons")
print(x==y)
print(x>=y)
print(x<=y)
print(x<y)

#logical Operations

print("Now some Logical Operations", "\n", "mmmmmmmmmmmmmmm", "\n", "#1 is And, #2 is OR")
print(x<y and y<x) #False
print(x<y or y<x) #true
print("hahahaha ha ha ha")
print("time for NOT Operator")
print("Not Operator result is ", not(x<y))

#assignment Operator

x3=10
y3 = 3
print("here x is ", x3)

x3=x3+3
print("here x is ", x3)

x3+=3
print("here x is ", x3)

#if we say a=a+3, or any number we add to variable it does the same as a+=3, so it does for other arithmatic operations like
#a=a*3 & a*=3
#or a=a-3 & a-=3