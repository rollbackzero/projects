#mystuff = {'apple': "I AM APPLES"}
#print(mystuff['apple'])

#import mystuff
#mystuff.apple()
#print(mystuff.tangerine)


class MyStuff(object):

    def __init__(self):
        self.tangerine = "and now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")


thing = MyStuff()
thing.apple()
print(thing.tangerine)
