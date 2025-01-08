from manim import *

class Transform1(Scene):
  def construct(self):
    tex1 = MathTex(r"f(x) = \frac{2 + x}{1 - x^2} \\"
                   r"g(y) = \frac{9 + y}{1 - y^3}", font_size=50)
    tex2 = MathTex(r"f(11) = \frac{2 +\left(11 \right)}{1 - \left(11 \right)^2} \\"
                   r"g(6) = \frac{9 + \left(6 \right)}{1 - \left( 6 \right)^3}", font_size=50)
    
    self.add(tex1)
    self.wait(.5)
    self.play(Transform(tex1,tex2))
    self.wait(1)

class TransformMatchingTex2(Scene):
  def construct(self):
    tex1 = MathTex(r"f(x) = \frac{2 + x}{1 - x^2} \\"
                   r"g(y) = \frac{9 + y}{1 - y^3}", font_size=50)
    tex2 = MathTex(r"f(11) = \frac{2 +\left(11 \right)}{1 - \left(11 \right)^2} \\"
                   r"g(6) = \frac{9 + \left(6 \right)}{1 - \left( 6 \right)^3}", font_size=50)
    
    self.add(tex1)
    self.wait(.5)
    self.play(TransformMatchingTex(tex1,tex2))
    self.wait(1)
    
class ReplacementTransform3(Scene):
  def construct(self):
    tex1 = MathTex(r"f(x) = \frac{2 + x}{1 - x^2} \\"
                   r"g(y) = \frac{9 + y}{1 - y^3}", font_size=50)
    tex2 = MathTex(r"f(11) = \frac{2 +\left(11 \right)}{1 - \left(11 \right)^2} \\"
                   r"g(6) = \frac{9 + \left(6 \right)}{1 - \left( 6 \right)^3}", font_size=50)
    
    self.add(tex1)
    self.wait(.5)
    self.play(ReplacementTransform(tex1,tex2))
    self.wait(1)