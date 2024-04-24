# Read/Write Files Demo
#
# Files we want to open should be located
# in the same folder as our .py file
#


# First Step: Open the file
my_file = open("poem.txt", "r") #'r' → open for READING

# OPTION ONE: Read whole file into string
# full_text = my_file.read()  # loads the whole file into a single var
                            # usually would need to be split up

# OPTION TWO: Reach each line into a single list
lines = my_file.readlines()

# Use rstrip() to remove the '\n' characters
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")
    
print(f"""A poem:
{lines[0]}
{lines[1]}
{lines[2]}""")

# Last Step: Close the
my_file.close()