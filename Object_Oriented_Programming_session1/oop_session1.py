# AI_Javaher
# this is the first session of OOP tutorial
# check the video of this code in youtube :https://www.youtube.com/watch?v=TEuEGNREGrY&t=4s
# you can find the list of videos about OOP to tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xfQKkV3Q6R6NcPPD2LrZimo
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
###################### OOP ##########################
import numpy as np


class Work:
    def coordinate(self, xo, yo, xd, yd):
        self.xo = xo
        self.xd = xd
        self.yo = yo
        self.yd = yd

    def dis(self):
        d = np.abs(self.xo - self.xd) + (self.yo - self.yd)
        return d


a = Work()
a.coordinate(1, 2, 3, 4)
print(a.xo)
