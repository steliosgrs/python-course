# Παράδειγμα 1 - if
x = 2
if x > 0:
    print("Θετικός")


# Παράδειγμα 2 - if-else
y = -4
x = y
if x > 0:
    print("Θετικός")
else:
    print("Αρνητικός")

# Λύση προβλήματος
students = int(input("Πόσοι μαθητές υπάρχουν;"))
size = int (input("Σε πόσα group θες να τους χωρίσεις;"))
if students%size == 0:
    print(f"Δημιουργήθηκαν {students//size} group")
else:
    print(f"Δημιουργήθηκαν {students//size+1} group")

# Παράδειγμα 3 - if-elif-else
z = 0
x = z
if x > 0:
    print("Θετικός")
elif x < 0:
    print("Αρνητικός")
else:
    print("Το {x} είναι 0")


#  Παράδειγμα - Τελεστές (==, !=, >,>=,<,<=)
day = "Κυριακή"
if day == "Κυριακή":
    print("Έχεις μάθημα")

time = 13
if day == "Κυριακή":
    if time >= 12.30:
        print("Έχεις μάθημα")
    else:
        print("Πιες καφέ")


# Παράδειγμα - Strings
string = "Python"
sub_str = int(input("Δώσε κάποιους χαρακτήρες: "))
if string == sub_str:
    print(f"Έδωσες την ίδια φράση ({string})")
else:
    if sub_str in string:
        print("Η φράση {sub_str} υπάρχει μέσα στην {string}")
