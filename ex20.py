from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())  # read contens of object and print out

def rewind(f):
    f.seek(0)    # call function seek to go back to start point         

def print_a_line(line_count, f):
    print(line_count, f.readline())  #  print the line number of each 


current_file = open(input_file)   # open the input file and assign to object 

print("First lets print the whole file.\n")

print_all(current_file)  # print contents of file

print("Now lets rewind, kind of like a tape:")   

rewind(current_file)    # call function rewind to go back to start point

print("Let's print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
