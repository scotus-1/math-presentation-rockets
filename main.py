import math
import time
from manim import *
from manim_slides import Slide

SLIDES = True;
SECTION_DIV = True;
SKIP_ANIM = False;


def pointstr(array3d):
    return f"({array3d[0]},{array3d[1]},{array3d[2]})"


class TotalVelocityPart1(Slide):
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
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}")

        start = MathTex(
    r"\Delta V", r"=", r"-", r"c", r"\ln", r"\bigg(", 
    r"1", r"-", r"{", r"(1", r"-", r"S)", r"M_r", r"\over", r"P", r"+", r"M_r", r"}", 
    r"\bigg)"
).scale(1.1)
        self.play(Write(start))
        self.div()

        delV1 = MathTex(r"\Delta V = \Delta V_1 + \Delta V_2 + \Delta V_3").next_to(start, UP)
        self.play(Write(delV1))
        self.div()

        groupHEAD = VGroup(start, delV1)
        self.play(groupHEAD.animate.to_corner(UP+RIGHT*4))
        rect_width = 1
        rect_height = 1.5  # 1.5 × width

        rectangles = VGroup(
            *[
                Rectangle(width=rect_width, height=rect_height)
                for _ in range(4)
            ]
        )

        rectangles.arrange(DOWN, buff=0.2)
        rectangles.to_edge(LEFT)

        for r in rectangles:
            r.set_fill(BLUE, opacity=0.6)

        labels = VGroup(
            MathTex("A").scale(0.8).move_to(rectangles[0]),
            MathTex("M_3").scale(0.8).move_to(rectangles[1]),
            MathTex("M_2").scale(0.8).move_to(rectangles[2]),
            MathTex("M_1").scale(0.8).move_to(rectangles[3]))

        self.play(*[DrawBorderThenFill(r) for r in rectangles], *[Create(label) for label in labels])
        self.div()

        V1_1 = MathTex(
    r"\Delta V_1", r"=", r"-", r"c", r"\ln", r"\bigg(", 
    r"1", r"-", r"{", r"(1", r"-", r"S)", r"M_r", r"\over", r"P", r"+", r"M_r", r"}", 
    r"\bigg)"
).scale(1.2).move_to(start.get_center() + DOWN*2.7)
        
        self.div()

        self.play(TransformMatchingTex(start.copy(), V1_1))
        # --- Bracket 1: top two shapes ---
        brace1 = Brace(
            VGroup(rectangles[0], rectangles[2]),
            direction=RIGHT
        )
        label1 = brace1.get_text(r"$P$")

        # --- Bracket 2: bottom two rectangles ---
        brace2 = Brace(
            VGroup(rectangles[3], rectangles[3]),
            direction=RIGHT
        )
        label2 = brace2.get_text(r"$M_r$")

        self.div()

        self.play(
            Create(brace1), FadeIn(label1),
            Create(brace2), FadeIn(label2),
        )
        self.div()

        V1_2 = MathTex(
    r"\Delta V_1", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_1", r"\over", 
    r"M_2", r"+", r"M_3", r"+", r"A", r"+", r"M_1", 
    r"}", 
    r"\big)"
).scale(1.2).move_to(V1_1.get_center())
        self.play(TransformMatchingTex(V1_1, V1_2))
        self.div()

        self.play(Unwrite(V1_2))
        self.div()

        V2_1 = MathTex(
    r"\Delta V_2", r"=", r"-", r"c", r"\ln", r"\bigg(", 
    r"1", r"-", r"{", r"(1", r"-", r"S)", r"M_r", r"\over", r"P", r"+", r"M_r", r"}", 
    r"\bigg)"
).scale(1.2).move_to(start.get_center() + DOWN*2.7)
        
        self.div()

        self.play(TransformMatchingTex(start.copy(), V2_1))
        # --- Bracket 1: top two shapes ---
        brace1_2 = Brace(
            VGroup(rectangles[0], rectangles[1]),
            direction=RIGHT
        )
        label1_2 = brace1_2.get_text(r"$P$")

        # --- Bracket 2: bottom two rectangles ---
        brace2_2 = Brace(
            VGroup(rectangles[2], rectangles[2]),
            direction=RIGHT
        )
        label2_2 = brace2_2.get_text(r"$M_r$")

        self.div()

        self.play(
            ReplacementTransform(brace1, brace1_2), ReplacementTransform(label1, label1_2),
            ReplacementTransform(label2, label2_2), ReplacementTransform(brace2, brace2_2),
            Uncreate(rectangles[3]), Uncreate(labels[3])
        )
        self.div()

        V2_2 = MathTex(
    r"\Delta V_2", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_2", r"\over", 
    r"M_3", r"+", r"A", r"+", r"M_2", 
    r"}", 
    r"\big)"
).scale(1.2).move_to(V2_1.get_center())
        self.play(TransformMatchingTex(V2_1, V2_2))
        self.div()

        self.play(Unwrite(V2_2))
        self.div()

        V3_1 = MathTex(
    r"\Delta V_3", r"=", r"-", r"c", r"\ln", r"\bigg(", 
    r"1", r"-", r"{", r"(1", r"-", r"S)", r"M_r", r"\over", r"P", r"+", r"M_r", r"}", 
    r"\bigg)"
).scale(1.2).move_to(start.get_center() + DOWN*2.7)
        
        self.div()

        self.play(TransformMatchingTex(start.copy(), V3_1))
        # --- Bracket 1: top two shapes ---
        brace1_3 = Brace(
            VGroup(rectangles[0], rectangles[0]),
            direction=RIGHT
        )
        label1_3 = brace1_3.get_text(r"$P$")

        # --- Bracket 2: bottom two rectangles ---
        brace2_3 = Brace(
            VGroup(rectangles[1], rectangles[1]),
            direction=RIGHT
        )
        label2_3 = brace2_3.get_text(r"$M_r$")

        self.div()

        self.play(
            ReplacementTransform(brace1_2, brace1_3), ReplacementTransform(label1_2, label1_3),
            ReplacementTransform(label2_2, label2_3), ReplacementTransform(brace2_2, brace2_3),
            Uncreate(rectangles[2]), Uncreate(labels[2])
        )
        self.div()

        V3_2 = MathTex(
    r"\Delta V_3", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_3", r"\over", 
    r"M_3", r"+", r"A", 
    r"}", 
    r"\big)"
).scale(1.2).move_to(V3_1.get_center())
        self.play(TransformMatchingTex(V3_1, V3_2))
        self.div()

        self.play(Unwrite(V3_2))
        self.div()
        self.play(FadeOut(*self.mobjects), run_time=1.5)
        self.div()

class TotalVelocityPart2(Slide):
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
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}")

        V1 = MathTex(
    r"\Delta V_1", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_1", r"\over", 
    r"M_2", r"+", r"M_3", r"+", r"A", r"+", r"M_1", 
    r"}", 
    r"\big)"
)       

        V2 = MathTex(
    r"\Delta V_2", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_2", r"\over", 
    r"M_3", r"+", r"A", r"+", r"M_2", 
    r"}", 
    r"\big)"
)

        V3 = MathTex(
    r"\Delta V_3", r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_3", r"\over", 
    r"M_3", r"+", r"A", 
    r"}", 
    r"\big)"
)
        
        # Group them
        equations = VGroup(V1, V2, V3).scale(1)
        # Arrange horizontally with spacing
        equations.arrange(DOWN, buff=0.5)



        # Add to scene
        self.play(*[Create(eq) for eq in equations])
        self.div()

        vf = MathTex(r"v_f=  \Delta V_1 + \Delta V_2 + \Delta V_3 + 0").next_to(equations, UP, buff=0.6)
        self.play(Write(vf))
        self.div()

        V1_1 = MathTex(
            r"-c \ln\Big( 1 - {(1-S) M_1 \over M_2 + M_3 + A + M_1} \Big)"
        ).move_to(V1.get_center())  

        V2_1 = MathTex(
    r"-c \ln\Big( 1 - {(1-S) M_2 \over M_3 + A + M_2} \Big)"
).move_to(V2.get_center())

        V3_1 = MathTex(
            r"-c \ln\Big( 1 - {(1-S) M_3 \over M_3 + A} \Big)"
        ).move_to(V3.get_center())
        self.play(TransformMatchingTex(V1, V1_1), TransformMatchingTex(V2, V2_1), TransformMatchingTex(V3, V3_1))
        self.div()

        addition = MathTex(V1_1.get_tex_string(), V2_1.get_tex_string(), V3_1.get_tex_string()).scale(0.7).next_to(vf, DOWN)

        self.play(TransformMatchingTex(VGroup(V1_1, V2_1, V3_1), addition))
        self.remove(addition)
        addition = MathTex(
    # First term
    r"=", r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_1", r"\over", r"M_2", r"+", r"M_3", r"+", r"A", r"+", r"M_1",
    r"}", r"\big)",
    
    # Plus sign
    r"+",
    
    # Second term
    r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_2", r"\over", r"M_3", r"+", r"A", r"+", r"M_2",
    r"}", r"\big)",
    
    # Plus sign
    r"+",
    
    # Third term
    r"-", r"c", r"\ln", r"\big(", 
    r"1", r"-", r"{", 
    r"(1", r"-", r"S)", r"M_3", r"\over", r"A", r"+", r"M_3",
    r"}", r"\big)"
).scale(0.7).next_to(vf, DOWN)
        self.add(addition)
        self.div()

        addition2 = MathTex(
    # -c[
    r"=", r"-", r"c", r"\big[",
    
    # First log
    r"\ln", r"\big(",
    r"{", r"M_1", r"+", r"M_2", r"+", r"M_3", r"+", r"A", r"-", r"(1", r"-", r"S)", r"M_1", r"\over", 
    r"M_1", r"+", r"M_2", r"+", r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Plus sign
    r"+",
    
    # Second log
    r"\ln", r"\big(",
    r"{", r"M_2", r"+", r"M_3", r"+", r"A", r"-", r"(1", r"-", r"S)", r"M_2", r"\over", 
    r"M_2", r"+", r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Line break
    r"\\",
    
    # Plus sign
    r"+",
    
    # Third log
    r"\ln", r"\big(",
    r"{", r"M_3", r"+", r"A", r"-", r"(1", r"-", r"S)", r"M_3", r"\over", 
    r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Closing bracket
    r"\big]"
).scale(0.8).next_to(addition, DOWN, buff=0.7)
        self.play(TransformMatchingTex(addition.copy(), addition2))
        self.div()

        addition3 = MathTex(
    # c[
    r"=", r"c", r"\big[",
    
    # First log
    r"\ln", r"\big(",
    r"{", 
        r"M_1", r"+", r"M_2", r"+", r"M_3", r"+", r"A", r"\over",
        r"S", r"M_1", r"+", r"M_2", r"+", r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Plus sign
    r"+",
    
    # Second log
    r"\ln", r"\big(",
    r"{",
        r"M_2", r"+", r"M_3", r"+", r"A", r"\over",
        r"S", r"M_2", r"+", r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Plus sign
    r"+",
    
    # Third log
    r"\ln", r"\big(",
    r"{",
        r"M_3", r"+", r"A", r"\over",
        r"S", r"M_3", r"+", r"A",
    r"}",
    r"\big)",
    
    # Closing bracket
    r"\big]"
).scale(0.875).next_to(addition2, DOWN, buff=1)
        self.play(TransformMatchingTex(addition2.copy(), addition3))
        self.play(Wiggle(addition3))
        self.div()

        self.play(FadeOut(*self.mobjects), run_time=1.5)
        self.div()
    

class LagrangeSetup(Slide):
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
        pass




        


                            







        

        




        








