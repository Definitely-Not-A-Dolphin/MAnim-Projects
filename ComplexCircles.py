from manim import *

class SceneOne(Scene):
  def construct(self):
    text1 = Text("Tervetuloa Manimissa", font_size = 80)
    
    self.play(FadeIn(text1))