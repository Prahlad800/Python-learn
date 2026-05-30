### Q1 :- Print the given strings as per stated format.

# **Given strings**:
# ```
# "Data" "Science" "Mentorship" "Program"
# "By" "CampusX"
# ```
# **Output**:
# ```
# Data-Science-Mentorship-Program-started-By-CampusX
# ```

# Concept- [Seperator and End]
# q1
print( "Data", end="-")
print( "Science", end="-")
print("Mentorship","Program","By","CampusX",sep="-")

### Q2:- Write a program that will convert celsius value to fahrenheit.
c = 3
f = (c*1.8)+32
print("Fahrenheit =",f)

#Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

a=4
b=5
print("a =",a,"b =",b)
c=a
a=b
print("a =",a,"b =",c)

#Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

a=int(input("enter a "))
b=int(input("enter b "))
c=(a+b)/2
print("coordinates =",c)
