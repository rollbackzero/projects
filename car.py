class Car(object):
    def __init__(self, make, model, color, max_speed):
        self.make = make
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def start(self):
        print("start engine")

    def stop(self):
        print("stop engine")

    def accelerate(self):
        print("accelerate")

    def breaking(self):
        print("breaking")


Volvo = Car('Volvo', 'S40', 'Silver', 200)
Nissan = Car("Nissan", "Xtrail", "Red", 180)

