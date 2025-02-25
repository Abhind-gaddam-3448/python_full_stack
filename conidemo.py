
# find the maximamum  at three numbers
nu1=int(input("enter  a number "))
nu2=int(input("enter a number"))
nu3=int(input("enter  a number1"))
if(nu1>nu2 and nu1>nu3):
    print("maximu=",nu1)
elif(nu2>nu1 and nu2>nu3):
    print("maximum ",nu2)
else:
    print("maimum number",nu3)
 

#  swap two number


a=20
b=40
a= a ^ b
b=b ^ a
a= a ^ b
print(a)
print(b)

c=76
d=98
c=c+d 
d=c-d 
c=c-d
print(c)
print (d)



# swap 2 number with 3 variables
x=2
y=7
z=x+y
y=z-y
x=z-x
print(x)
print(y)


# 2varible swap
a=20
b=40
a= a ^ b
b=b ^ a
a= a ^ b
print(a)
print(b)

c=76
d=98
c=c+d 
d=c-d 
c=c-d
print(c)
print (d)


x=2
y=7
z=x+y
y=z-y
x=z-x
print(x)
print(y)

# 3variable swap

x=1
y=2
z=3
x,y,z,=y,z,x
print(x)
print(y)
print(z)
# method 2
p=1
q=2
r=3
u=p+q+r
q=u-(q+r)
r=u-(r+p)
p=u-(p+r)
print(p)
print(q)
print(r)
# leap year method 1
year=int(input("enter the year "))
month="february(29days) (year for 366 days) "
if(year%4==0):
    print("this is lipy  year ", month )
else:
    print("thise is not a lipy ")

# leaap year example but don't do thise prosses
nxyear=int(input("enter year start with 2000 to 3000 "))
lipy=(42002,2006,2010,2014,2018,2022,2026,2030,2034,2038,2042,2046)
if(nxyear in lipy):
    print("this is leap year february(29days) (year for 366days)")
elif(nxyear not in lipy ):
   print("thise is not a leap  year ")

# # reverse input 
userinput=input("enter a value ")
print(" before value ",userinput)
reverse=userinput[::-1]
print("after reverse a value ",reverse)


    # grading marks
marks=int(input("enter marks below 100"))
if(marks<=100 and marks>=90):
    print("this is A+")
elif(marks<=90 and marks>=80):
    print("yhis is A")
elif(marks<=80 and marks>=70):
    print("this is B+")
elif(marks<=70 and marks>=60):
   print("this is  c+")
elif(marks<=60 and marks>=50):
    print("this is  C")
elif(marks<=50 and marks>=35):
    print("thise is D")
elif(marks<=34):
    print("fail")
else:
  print("enter below 100")
 
# to find minimum among four numbers
number1=int(input("enter first number"))
number2=int(input("enter second number"))
number3=int(input("enter first number"))
number4=int(input("enter second number"))

if(number1<number2 and number1<number3):
    print("minimum",number1)
elif(number2<number3 and number2<number4):
    print("minimum",number2)
elif(number3<number4 and number3<number1):
    print("minimum",number3)
else:
    print("minimum",number4)