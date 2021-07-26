# AI_Javaher
# this is the third session of OOP tutorial about single and multi inheritance
# check the video of this code in youtube :https://www.youtube.com/watch?v=ayjqdUE_WTI&t=109s
# you can find the list of videos about OOP to tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xfQKkV3Q6R6NcPPD2LrZimo
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
class Creation:
    def __init__(self, nleg, eye, ear, weight):  # number of legs, seeing or blind, hearing or deaf, kg
        self.nleg = nleg
        self.eye = eye
        self.ear = ear
        self.weight = weight

    def calories(self, cal):
        total_calory = cal * self.weight
        return total_calory

    def description(self, number):
        print(f' the {number} of {self.species} is living in {self.habitat}  ')

class Animal:
    def __init__(self, species, food, habitat):
        self.species = species
        self.food = food
        self.habitat = habitat
        self.vertebrate = False

    def description(self, number):
        print(f' the {number} of {self.species} is living in {self.habitat} and eats {self.food} ')

class Cat(Creation, Animal):
    def __init__(self, name, species, food, habitat,nleg,eye,ear,weight):
        self.name = name
        Animal.__init__(self,species, food, habitat)
        Creation.__init__(self,nleg,eye,ear,weight)

        self.vertebrate = True

    # def description(self, number):
    #     if self.vertebrate:
    #         super().description(number)


c = Cat('kitty', 'SB', 'meat', 'forest',4,'seeing','hearing',5)
c.description(5)
print(Cat.__mro__)
# print(c.calories(200))
# a = Animal('hg', 'meat', 'forest')
# print(a.vertebrate, 'animal class')
# print(c.vertebrate, 'cat class')
# c.description(5)
