import math
import time
from manim import *
from manim_slides import Slide

SLIDES = True;
SECTION_DIV = False;
SKIP_ANIM = True;


def pointstr(array3d):
    return f"({array3d[0]},{array3d[1]},{array3d[2]})"


class TotalVelocity(Slide):
    def div(self, ovr=False):
        if not SLIDES:
            if SECTION_DIV:
                if ovr:
                    self.next_section()                
                elif SKIP_ANIM:
                    self.next_section(skip_animations=True)
            else:
                self.wait(1)
        else:
            self.next_slide()

        
            
    def construct(self):
        self.div()

        ptext = Text("a").scale(0.6)
        tlawtext = Text("Kepler's Third Law").scale(1.3).next_to(ptext, UP *1.2)
        self.play(Write(ptext), Write(tlawtext))





                            







        

        




        








