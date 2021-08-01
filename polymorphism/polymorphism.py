# AI_Javaher
# this is the polymorphism tutorial in python
# check the video of this code in youtube :https://www.youtube.com/watch?v=eTM3qpRaiPI&t=2s
# you can find the list of videos about OOP to tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xfQKkV3Q6R6NcPPD2LrZimo
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
import numpy as np

class Euclidean:
    def __init__(self):
        pass

    def distance(self, x1, x2, y1, y2):
        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Manhattan:
    def __init__(self):
        pass

    def distance(self, x1, x2, y1, y2):
        return np.abs(x1 - x2) + np.abs(y1 - y2)

e = Euclidean()
m = Manhattan()
print(e.distance(1,2,3,4))
print(m.distance(1,2,3,4))
for obj in (e,m):
    obj.distance(1,2,3,4)

def Dis(obj):
    obj.distance(1,2,3,4)




