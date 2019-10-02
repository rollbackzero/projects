people = 40
cars = 30
trucks = 45

if cars > people:
    print("We should take cars")
elif cars < people:
    print("We should not take cars")
else:
    print("We can't decide")

if trucks > cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else: 
    print("We still cant decide")

if people > trucks:
    print("Alright, lets just take the trucks")
else:
    print("Fine, lets stay home then")
    


