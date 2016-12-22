class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye color -"+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


miley_cyrus = Child("Cyrus", "blue",5)
miley_cyrus.show_info()
bily_cyrus = Parent("Cyrus", "blue")
print(bily_cyrus.last_name)