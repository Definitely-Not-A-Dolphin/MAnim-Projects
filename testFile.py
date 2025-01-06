from manim import *
import math

mathText1 = ["\int_{-\infty}^{\infty} e^{-x^2} d x",
             "\int_{-\infty}^{\infty} e^{-x^2} d x = \sqrt{\pi}"]

class TransformAttempt(Scene):
    def construct(self):
        tex1 = MathTex(mathText1[0], font_size = 80)
        tex2 = MathTex(mathText1[1], font_size = 80)
        
        self.play(Write(tex1))
        self.wait(2)
        self.play(tex1.animate.move_to([0,0,0]))
        self.play(tex1.animate.move_to([-1.2,0,0]))
        self.wait(2)
        self.play(ReplacementTransform(tex1,tex2))
        self.wait(2)
        self.play(Circumscribe(tex1))
        self.play(Unwrite(tex2))

class updaters(Scene):
  def construct(self):
    
    k = ValueTracker(0)
    num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))
    
    self.play(FadeIn(num))
    self.wait(1)
    self.play(k.animate.set_value(6), rate_func=linear)
    self.wait(1)
    
class Graphing(Scene):
  def construct(self):
    
    plane = NumberPlane(
      x_range=[-2*PI, 2*PI, PI/6], x_length=4*PI, y_range=[-2, 2, 1],y_length=4
    )

    #declare function here
    parabola = plane.plot(lambda x: math.sin(x), color = BLUE)
    
    
    self.play(DrawBorderThenFill(plane))
    self.play(Create(parabola, run_time = 3))
    self.wait(3)