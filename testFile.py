from manim import *
import math

mathText1 = [r"\left(-\frac{1}{2}\right)!",
             r"= \sqrt{\pi}"]

class TransformAttempt(Scene):
    def construct(self):
        tex1 = MathTex(mathText1[0], font_size = 60)
        tex2 = MathTex(mathText1[0] + mathText1[1], font_size = 60)
        tex3 = MathTex(mathText1[1], font_size = 60)

        self.play(Write(tex1))
        self.wait()
        self.play(Transform(tex1,tex2,tex3))
        self.wait(3)

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
      x_range = [-2*PI, 2*PI, PI/2], x_length = 4*PI, y_range = [-2, 2, 1], y_length = 4
    )

    #declare function here
    function1 = plane.plot(lambda x: math.cos(x), color = BLUE)
    
    functionA = plane.plot(lambda x: 1, 
                           color = RED)
    functionB = plane.plot(lambda x: 1 - (x**2)/2, 
                           color = ORANGE)
    functionC = plane.plot(lambda x: 1 - (x**2)/2 + (x**4)/24, 
                           color = YELLOW)
    functionD = plane.plot(lambda x: 1 - (x**2)/2 + (x**4)/24 - (x**6)/720, 
                           color = GREEN)
    functionE = plane.plot(lambda x: 1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320, 
                           color = BLUE)
    
    self.play(DrawBorderThenFill(plane))
    self.play(Create(function1, run_time = 2))
    self.wait(1)
    self.play(Create(functionA), run_time = 2)
    self.wait(1)
    self.play(Transform(functionA, functionB), run_time = 2)
    self.wait(1)
    self.play(Transform(functionA, functionC), run_time = 2)
    self.wait(1)
    self.play(Transform(functionA, functionD), run_time = 2)
    self.wait(1)
    self.play(Transform(functionA, functionE), run_time = 2)
    self.wait(3)