x=0 # Αρχικοποίηση

# Απλό while
while x < 10: # Συνθήκη (όπως και στο if)
    x=x+1     # Update μεταβλητής που ΕΛΕΓΧΕΤΑΙ στην συνθήκη
    print(x)

# Δεν εκτελείται καμία επανάληψη
while x > 10:
    x=x-1
    print(x)

# Άπειρες επαναλήψεις - Infinity Loop
while x < 10:
    x=x-1
    print(x)


# For σε range (εύρος) 10,
# Αρχική τιμή i = 0 (default τιμή)
# Βήμα 1 (default βήμα)
for i in range(10):
    print(i)


# For σε range (εύρος) 10,
# Αρχική τιμή i = 3
# Βήμα 1 (default βήμα)
for i in range(3, 10):
    print(i)


# For σε range (εύρος) 10,
# Αρχική τιμή i = 3
# Βήμα 2
for i in range(2, 10, 2 ):
    print(i)


# For για string
for x in "banana":
  print(x)

char = "#"
for x in range(1,10):
    message = x * char
print(message)
