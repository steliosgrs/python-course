# Break
while True:
    x=x+1
    print(x)
    if x ==10:
        break

# Continue
while True:
    x=x+1
    if x ==5:
        continue
    print(x)
    if x ==10:
        break

# Boolean Μεταβλητές
x=2
print(x > 2) # ==> False
print(x == 2) # ==> True

char = '#'
flag = True # False

for x in range(1,10):
    message = x * char
    print(message)
    if x == 5 and flag == True:
        break
print("Telos")

# Flag
flag = True
while flag:
    x=x+1
    print(x)
    if x ==10:
        flag=False

# Keywords and, or
x = 2
y = 3 
if x >= 2 and y >=3:
    print("Είναι μεγαλύτερα από..")


x = 10
print("Countdown!")
while x > 0:
    print(x)
    x = x - 1 
    if x == 0:
        break

# Modules 1
import random

for i in range(10):
    print(random.randint(1,10))

# Modules 2
# Πρόγραμμα που εμφανίζει τις λύσεις ενός τριωνύμου
from math import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
# ax^2 + bx + c = 0 Τύπος για τριώνυμο

# Υπολογισμός διακρίνουσας
D = b**2 - 4*a*c
x1 = -b + sqrt(D)/2*a
x2 = -b - sqrt(D)/2*a
print(f"The roots are {x1} and {x2}")