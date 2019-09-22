from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt_again = input("Type the filename again: ")
file_again = open(txt_again)
print(file_again.read())

