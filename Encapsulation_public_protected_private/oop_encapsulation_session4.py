# AI_Javaher
# this is the forth session of OOP tutorial about encapsulation
# check the video of this code in youtube :https://www.youtube.com/watch?v=TEuEGNREGrY&t=4s
# you can find the list of videos about OOP to tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xfQKkV3Q6R6NcPPD2LrZimo
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
class Car:
    def __init__(self):
        self.__country = 'Germany'
        self.__color = 'red'
        self.__sits = 4

    def gas(self):
        print(f'{self.__sits * 10} liters per 1000 km')


class BMW(Car):
    def __init__(self):
        self.type = 'A'
        super().__init__()

    def private(self):
        print(f'In Car class I use public attribute: {self.__color}')


c = Car()
c.gas()
# print(c.__color)
b = BMW()
# print(b.__color)
