class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_toys = number_toys

#billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)
    
miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_toys)
