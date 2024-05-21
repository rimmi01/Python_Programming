class Students:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
student1 = Students()
student1.set_name("Shehnaaz")
print(student1.name)
print(student1.get_name())

student2 = Students()
student2.set_name("Parag")
print(student2.get_name())
