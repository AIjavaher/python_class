# AI_Javaher
# this is the second session of OOP tutorial
# check the video of this code in youtube :https://www.youtube.com/watch?v=GTQUkcPYO_w&t=271s
# you can find the list of videos about OOP to tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xfQKkV3Q6R6NcPPD2LrZimo
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
########################## OOP Advance ##########################
class Project:
    boss = 'jack'

    def __init__(self, name, date, workers=5):
        self.name = name
        self.date = date
        self.workers = workers

    @classmethod
    def budget(cls, money):
        print(f'the budget of this project is {money}$')

    @staticmethod
    def salary():
        print('the salary is 1200$')


pro1 = Project('road1', '1.1.2021', 14)
print(pro1.date)
print(Project.boss)
# Project.budget(120000)
