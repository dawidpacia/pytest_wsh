class Animal:

    def __init__(self, animal_type):
        self.animal_type = animal_type

    def make_a_sound(self):
        if self.animal_type == "cat":
            print("meow")
        elif self.animal_type == "fox":
            print("timpirimpimpim")
        else:
            print("no sound")

cat = Animal("cat")
cat.make_a_sound()
