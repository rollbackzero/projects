from sys import argv

script, filename = argv

print(f"Were going to erase {filename}")
print("If you don't want, hit CTRL-C (^C)")
print("If you do want that, hit RETURN")
input('?')

target = open(filename, 'w')  # open filename with write access
print("Opening the file...")
print("Truncating the file. Goodbye!")
target.truncate()            # delete contents of opened file 

print("Now I'm going to ask you for three lines")
line1 = input("line 1: ")    # ask user to type
line2 = input("line 2: ")    # ask user to type
line3 = input("line 3: ")    # ask user to type

print("I'm going to write to the file")
target.write(f'''
{line1}
{line2}
{line3}
''')

print("And finally, we close it.")
target.close()               # saved and close file  
