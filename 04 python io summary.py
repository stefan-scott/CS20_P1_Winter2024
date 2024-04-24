# Python I/O Review

# OUTPUT lvl 1 - printing to shell (1 piece of data)
print(34)       #number
print("hello")  #string literal
text = "cs20"
print(text)     #string data from a variable

#OUTPUT lvl 2 - multiple things at once       → [alt] 26 
print("Hello" + text) #STR + STR → join/concatenation
print("Hello", text) #printing with , adds space ch

#OUTPUT lvl 3 - printing mixed types
num = 45
#         STR          INT
print("Best number:", num) 
print("Best number: " + str(num))
 
#INPUT - reading in values and storing in variables
number_one = input("enter a number: ") #input → STR

#DO MATH? Convert to a number
number_one = float(number_one)

result = number_one ** 3 #raise to the power of 3
print("cube of",number_one,"is",result)
