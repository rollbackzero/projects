from sys import argv

cheese = input(f"How many cheese: ")
crackers = input(f"How many crackers: ") 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's not enough for a party!")
    print("Get a blanket\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("We can even get user input:")
cheese_and_crackers(cheese, crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine two, variables and math:")
cheese_and_crackers(int(cheese) + 100, int(crackers) + 1000)
