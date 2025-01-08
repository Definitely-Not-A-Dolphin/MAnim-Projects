from manim import *

class SceneOne(Scene):
  def construct(self):
    tex1 = MathTex(r"a x^3 + b x^2 + c x + d = 0", font_size = 60)
    tex2 = MathTex(r"a \left( y - \frac{b}{3a} \right)^3 + b \left( y - \frac{b}{3a} \right)^2 + c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 50)
    tex3 = MathTex(r"a \left( y - \frac{b}{3a} \right)^3 \\ "
                   r" + b \left( y - \frac{b}{3a} \right)^2 \\ "
                   r" + c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 40).move_to([0,.5,0])
    tex4 = MathTex(r"a \left( y^3 + 3 y^2 \left( -\frac{b}{3a}\right) + 3y \left( -\frac{b}{3a}\right)^2 + \left( -\frac{b}{3a} \right)^3 \right) \\ "
                   r" + b \left( y^2 + 2y \left(- \frac{b}{3a} \right) + \left( -\frac{b}{3a} \right)^2 \right) \\ "
                   r" + c \left( y - \frac{b}{3a} \right) + d = 0", font_size = 40).move_to([0,.5,0])
    tex5 = MathTex(r"a \left( y^3 - \frac{b}{a} y^2 + \frac{b^2}{3a^2} y -\frac{b^3}{27a^3} \right) \\ "
                   r" + b \left( y^2 - \frac{2b}{3a} y +\frac{b^2}{9a^2} \right) \\ "
                   r" + c y - \frac{b c}{3a} + d = 0", font_size = 40).move_to([0,.5,0])
    tex6 = MathTex(r"a y^3 - b y^2 + \frac{b^2}{3a} y -\frac{b^3}{27a^2} \\ "
                   r" + b y^2 - \frac{2b^2}{3a} y +\frac{b^3}{9a^2} \\ "
                   r" + c y - \frac{b c}{3a} + d = 0", font_size = 40).move_to([0,.5,0])
    tex7 = MathTex(r"a y^3 + \frac{b^2}{3a} y -\frac{b^3}{27a^2} \\ "
                   r" - \frac{2b^2}{3a} y +\frac{b^3}{9a^2} \\ "
                   r" + c y - \frac{b c}{3a} + d = 0", font_size = 40).move_to([0,.5,0])    
    tex8 = MathTex(r"a y^3 \\ "
                   r" + \frac{b^2}{3a} y + c y - \frac{2b^2}{3a} y \\ "
                   r" - \frac{b c}{3a} + \frac{b^3}{9a^2} - \frac{b^3}{27a^2} + d = 0", font_size = 40).move_to([0,.5,0])
    tex9 = MathTex(r"a y^3 \\ "
                   r" + \left( c - \frac{b^2}{3a} \right) y \\ "
                   r" + \left( - \frac{b c}{3a} + \frac{b^3}{9a^2} - \frac{b^3}{27a^2} + d \right) = 0", font_size = 40).move_to([0,.5,0])
    tex10 = MathTex(r"a y^3 \\ "
                   r" + \left( c - \frac{b^2}{3a} \right) y \\ "
                   r" + \left( - \frac{b c}{3a} + \frac{2b^3}{27a^2} + d \right) = 0", font_size = 40).move_to([0,.5,0])
    
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
    self.play(Transform(tex1, tex6))
    self.wait()
    texttemp3 = Tex(r"Cancel $ b y^2$ terms", font_size = 40).move_to([0,3,0])
    self.play(Write(texttemp3))
    self.wait()
    self.play(TransformMatchingTex(tex1, tex7))
    self.wait()
    self.play(Unwrite(texttemp3))
    self.wait(.5)
    texttemp4 = Tex(r"Combine like terms").move_to([0,3,0])
    self.play(Write(texttemp4))
    self.wait()
    self.play(TransformMatchingTex(tex7,tex8))
    self.wait()
    self.play(TransformMatchingTex(tex8,tex9))
    self.wait()
    self.play(TransformMatchingTex(tex9,tex10))
    self.wait()
    self.play(Unwrite(texttemp2), Unwrite(texttemp4))
    texttemp5 = Tex(r"Divide by $a$").move_to([0,3,0])
    tex11 = MathTex(r"y^3 \\ "
                   r" + \left( \frac{c}{a} - \frac{b^2}{3a^2} \right) y \\ "
                   r" + \left( - \frac{b c}{3a^2} + \frac{2b^3}{27a^3} + \frac{d}{a} \right) = 0", font_size = 40).move_to([0,.5,0])
    self.play(Write(texttemp5))
    self.wait()
    self.play(Transform(tex10,tex11))
    self.wait()
    self.play(Unwrite(texttemp5))
    tex12 = Tex(r"Define $$p = \frac{c}{a} - \frac{b^2}{3a^2}$$", font_size = 40).move_to([0,3,0])
    self.play(Write(tex12))
    tex13 = MathTex(r"y^3 \\ "
                   r" + p y \\ "
                   r" + \left( - \frac{b c}{3a^2} + \frac{2b^3}{27a^3} + \frac{d}{a} \right) = 0", font_size = 40).move_to([0,.5,0])
    self.play(Transform(tex10, tex13))
    self.play(Unwrite(tex12))
    self.wait(.5)
    tex14 = Tex(r"Define $$q = - \frac{b c}{3a^2} + \frac{2b^3}{27a^3} + \frac{d}{a}$$", font_size = 40).move_to([0,3,0])
    self.play(Write(tex14))
    tex15 = MathTex(r"y^3 \\"
                    r" + p y \\ "
                    r" + q = 0", font_size = 40).move_to([0,.5,0])
    self.play(Transform(tex10, tex15))
    self.wait()
    tex16 = MathTex(r"y^3 + p y + q = 0", font_size = 40).move_to([0,.5,0])
    