from manim import *

class FirstScene(Scene):
    def construct(self):
        d1 = Dot([-2, -2, 0], color=RED)
        d2 = Dot([-2, -3, 0], color=RED)
        d3 = Dot([2, -3, 0], color=RED)
        d4 = Dot([2, -2, 0], color=RED)

        line1 = Line(d1, d2, color=ORANGE)
        line2 = Line(d2, d3, color=ORANGE)
        line3 = Line(d3, d4, color=ORANGE)

        d5 = Dot([0, -0.5, 0])
        circle1 = Circle(radius=2.5, color=GREEN).move_to([0, -0.5, 0])

        self.play(FadeIn(d1, d2, d3, d4, d5, line1, line2, line3, circle1))
        self.wait(2)