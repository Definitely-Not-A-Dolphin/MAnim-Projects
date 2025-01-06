from manim import *

class Test1(Scene):
    def construct(self):
        tex1 = MathTex("\int_{-\infty}^{\infty} x^{-x} d x", font_size = 80).move_to([3,3,0])
        tex2 = always_redraw(lambda : Tex("Manim", font_size = 80).next_to(tex1, DOWN))
        
        self.play(FadeIn(tex1, tex2))
        self.wait()
        self.play(tex1.animate.move_to([-3,-2,0]))
        self.wait()

class Test2(Scene):
  def construct(self):
    
    k = ValueTracker(0)
    num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))
    
    self.play(FadeIn(num))
    self.wait(1)
    self.play(k.animate.set_value(6), rate_func=linear)
    self.wait(1)
    
class Graphin(Scene):
  def construct(self):
    plane = NumberPlane(
      x_range=[-4, 4, 1], x_length=7, y_range=[0, 16, 4],y_length=8
    ).to_edge(DOWN)

    parab = plane.get_graph(lambda x: x ** 2, x_range=[-4, 4], color=GREEN)

    self.play(DrawBorderThenFill(plane))
    self.play(Create(parab))
    self.wait(3)