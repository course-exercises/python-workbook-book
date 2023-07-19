# exercise 1

print("my name is Mohammad", "my Email address is : " , "sites.me56@gmail.com")
# -----------------------------------------------------------------------------------------

# exercise 2
name = input("please enter your name : ")
print("hello", name)
# -----------------------------------------------------------------------------------------

# exercise 3
width = float(input("please enter width of your room : "))
length = float(input("please enter length of your room : "))
print("Area of your room is : ",width*length)
# -----------------------------------------------------------------------------------------

# exercise 4
CONST = 43560
width = float(input("please enter width of your room in feet : "))
length = float(input("please enter length of your room in feet : "))
print("Area of your room is : ",width*length/CONST)
# -----------------------------------------------------------------------------------------

# exercise 5


# -----------------------------------------------------------------------------------------

# exercise 6


# -----------------------------------------------------------------------------------------

# exercise 7
n = int(input("please enter a positive number : "))
print("sum of numbers from 1 to %i is %i"%(n,(n*(n+1)/2)))
# -----------------------------------------------------------------------------------------

# exercise 8
number_of_widgets = int(input("enter number of widgets"))
number_of_Gizmos = int(input("enter number of Gizmos"))
print("total weight of order is : ", number_of_Gizmos*112 + number_of_widgets * 75)
# -----------------------------------------------------------------------------------------

# exercise 9


# -----------------------------------------------------------------------------------------

# exercise 10
a = int(input("enter first number"))
b = int(input("enter second number"))
print("sum of a and b is : ",a+b)
print("product of a and b is : ",a*b)
print("difference of a and b is : ",a-b)
print("division of a and b is : ",a/b)
print("reminder of a / b is : ",a%b)
print("result of a^b is : ",a**b)
# -----------------------------------------------------------------------------------------

# exercise 11


# -----------------------------------------------------------------------------------------


# exercise 12


# -----------------------------------------------------------------------------------------

# exercise 13


# -----------------------------------------------------------------------------------------

# exercise 14
height1 = float(input("please enter height in feet"))
height2 = float(input("please enter height in inch"))
print("height is : ",((height1 * 12)+height2)*2.54)


# -----------------------------------------------------------------------------------------

# exercise 15
measurement_in_feet = float(input("enter the measurement in feet"))
measurement_in_inches = measurement_in_feet * 12
measurement_in_yards  = measurement_in_feet * 0.33
measurement_in_miles  = measurement_in_feet * 0.000189
print("the equivalent distance in inches is %f and in yards is %f and in miles is %f"%(measurement_in_inches,measurement_in_yards,measurement_in_miles))


# ----------------------------------------------------------------------------------------

# exercise 16
PI = 3.14
radius = float(input("enter the radius"))
print("area is : ",PI * (radius**2))
print("volume of sphere is ",4*PI*(radius**3)/3)

# ----------------------------------------------------------------------------------------

# exercise 17


# ----------------------------------------------------------------------------------------

# exercise 18

# ----------------------------------------------------------------------------------------

# exercise 19

# ----------------------------------------------------------------------------------------

# exercise 20

# ----------------------------------------------------------------------------------------

# exercise 21

# ----------------------------------------------------------------------------------------

# exercise 22

# ----------------------------------------------------------------------------------------

# exercise 23

# ----------------------------------------------------------------------------------------

# exercise 24

# ----------------------------------------------------------------------------------------

# exercise 25

# ----------------------------------------------------------------------------------------

# exercise 26

# ----------------------------------------------------------------------------------------

# exercise 27

# ----------------------------------------------------------------------------------------

# exercise 28



# ----------------------------------------------------------------------------------------

# exercise 29

celsius = int(input("enter the degrees in celsius : "))
# kelvin =
# fahrenheit =
# print("degree in celsius is : ",celsius,"degree in kelvin is : ",kelvin,"degree in fahrenheit is : ",fahrenheit)





# ----------------------------------------------------------------------------------------

# exercise 30

pressure = int(input("enter pressure in kilo pascal : "))




# ----------------------------------------------------------------------------------------

# exercise 31

n = int(input("please enter a four degits number : "))
sum = 0

sum += n%10
n = n//10

sum += n%10
n = n//10

sum += n%10
n = n//10

sum += n%10
# n = n//10

print(sum)


# ----------------------------------------------------------------------------------------

# exercise 32

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

sum = a+b+c

minimum = min(a,b,c)
maximum = max(a,b,c)
middle  = sum - minimum - maximum
print(minimum+"\t"+middle+"\t"+maximum)

# ----------------------------------------------------------------------------------------

# exercise 33

number_of_loaves = int(input("enter the loaves of old day : "))
regular_price = number_of_loaves * 3.49
discount = regular_price * 60 / 100
final = regular_price - discount
print("the regular price is : ",regular_price, "discount is : " ,discount, "finaly : ", )

