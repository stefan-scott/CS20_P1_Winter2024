# Try-Except Demo
# To prevent our programs from crashing so much...

#          0    1       2
my_list = [88, 44, "Twenty Two"]

while True:
    try:
        index = int(input("Enter an index: ")) #int() with non-num: ValueError
        chosen_num = my_list[index]  #if index is > 2, IndexError (out of range)
        print("Number: " + chosen_num) #if chosen_num is an int: TypeError
        break  #if we get this far, we know we had no problems...
    except TypeError:
        #what happens if we encountered an Error
        print("Type Error")
    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    except:
        print("Other Error")


