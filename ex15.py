from sys import argv

script, filename = argv

txt = open(filename)  # open a file   

print(f"Here's your file {filename}:")  
print(txt.read())     # read and print open file

print("Type the filename again:")
file_again = input('> ')   # ask user to type filename 

txt_again = open(file_again)  # open typed filename

print(txt_again.read())    # read and print open file

