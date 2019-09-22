from sys import argv

script, username = argv


print(f"Hi {username}, I'm the {script} script")
print("I'd like to ask you a few questions")
likes = input(f"Do you like me {username}? ")
lives = input(f"Where do you live {username}? ")
computer = input("What kind of computer do you have? ")

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')

