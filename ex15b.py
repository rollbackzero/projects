from sys import argv  # import argument variable function from sys module

script, filename = argv

txt = open(filename)  # open file and put into file object

print(f"Here's your file {filename}:")
print(txt.read())  # read contents of file object

txt_again = input("Type the filename again: ")
file_again = open(txt_again)
print(file_again.read())
txt.close()
file_again.close()
