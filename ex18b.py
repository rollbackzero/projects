from sys import argv

def print_two(*args):
    arg1, arg2 = args
    print(f"Hello {arg1}, {arg2}")

def print_two_again(arg1, arg2):
    print(f"Hello again Mr. {arg1}, {arg2}")

def print_one(arg1):
    print(f"{arg1}")

def print_none():
    print("I got nothin'.")

arg1 = input(f"Firstname? ")
arg2 = input(f"Lastname? ")

print_two(arg1,arg2)
print_two_again(arg1,arg2)
print_one(arg1)
print_none()
