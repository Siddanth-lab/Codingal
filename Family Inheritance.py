class dad:
    def __init__(self,eyes,agressive):
        self.eyes=eyes
        self.agressive=agressive
    def display(self):
        print("Your eye color is", self.eyes)
        print("You are agressive", self.agressive)

class son(dad):
    def __init__(self,name,age,eyes,agressive):
        self.name=name
        self.age=age

        super().__init__(eyes,agressive)
obj=son("Penguin",8,"blue",True)
obj.display()