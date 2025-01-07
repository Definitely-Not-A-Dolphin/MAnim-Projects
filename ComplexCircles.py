from manim import *

class SceneOne(Scene):
  def construct(self):
    blank = Text("", font_size = 100)
    tex1 = MathTex(r"a x^3 + b x^2 + c x + d = 0", font_size = 60)
    tex2 = MathTex(r"a \left( y - \frac{b}{3a} \right)^3 + b \left( y - \frac{b}{3a} \right)^2 + c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 50)
    tex3 = MathTex(r"a \left( y - \frac{b}{3a} \right)^3 + \\ "
                   r"b \left( y - \frac{b}{3a} \right)^2 + \\ "
                   r"c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 40).move_to([0,.5,0])
    tex4 = MathTex(r"a \left( y^3 + 3 y^2 \left( -\frac{b}{3a}\right) + 3y \left( -\frac{b}{3a}\right)^2 + \left( -\frac{b}{3a} \right)^3 \right) + \\ "
                   r" b \left( y^2 + 2y \left(- \frac{b}{3a} \right) + \left( -\frac{b}{3a} \right)^2 \right) + \\ "
                   r"c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 40).move_to([0,.5,0])
    tex5 = MathTex(r"a \left( y^3 - \frac{b}{a} y^2 + \frac{b^2}{3a^2} y -\frac{b^3}{27a^3} \right) + \\ "
                   r" b \left( y^2 - \frac{2b}{3a} y +\frac{b^2}{9a^2} \right) + \\ "
                   r"c y - \frac{b c}{3a} + d = 0", font_size = 40).move_to([0,.5,0])    
    
    self.play(Write(tex1))
    self.wait(1)
    texttemp1 = Text("The full derivation of the cubic formula", font_size = 40).move_to([0,3,0])
    self.play(Write(texttemp1))
    self.wait(1)
    self.play(Unwrite(texttemp1))
    texttemp2 = Tex(r"Substitute $$x = \left( y - \frac{b}{3a} \right)$$ ", font_size = 40).move_to([0,-3,0])
    self.play(Write(texttemp2))
    self.wait(1)
    self.play(Transform(tex1, tex2))
    self.wait(1)
    self.play(Transform(tex1, tex3))
    self.wait()
    self.play(Transform(tex1, tex4))
    self.wait()
    self.play(Transform(tex1, tex5))
    self.wait()