class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()   # call super with arguments Child and self then call altered function 
        print("CHILD, AFTER PARENT alterered()")
    
dad = Parent()  # create an object from class Parent
son = Child()   # create an object from class Child

dad.altered()   
son.altered()
