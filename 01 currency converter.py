# Ask the user for their name and store it in a variable called name.
# Ask the user for an amount (in CAD) to convert to Yen, and store this amount in a variable called amount_cad.
# Create a third variable called amount_yenand calculate what the Canadian amount would equal if exchanged into Japanese Yen.You may either look up a current rate, or use:1 CAD : 110 YEN 
# Print out the following: “Hello, [name]. If you exchange [amountCad] CAD, you would receive [amountYen] YEN.”


# Data Types:   int (6)   float (6.11)   str ("blah")   bool (True/False)
# input() → always gives us a string     int() float() str() bool()

# Ask user for name, store in var
name = input("Enter your name: ")  

# Ask for an amount in CAD
amount_cad = input("Enter an amount in CAD: ")  #STR

# Compute corresponding amount in YEN  1:110  (*110)
amount_yen = float(amount_cad) * 110
  # FLOAT             FLOAT      * INT
  
print("Hello, " + name + ".")
print("Exchanging " + amount_cad + " CAD gives " + str(amount_yen)+ " YEN.")