from manim import *

class Scene1(Scene):
  def construct(self):

    def MoveTo(Mobject,OldPos,NewPos):
      self.play(Mobject.animate.shift(RIGHT*(NewPos[0]-OldPos[0])))
      self.play(Mobject.animate.shift(UP*(NewPos[1]-OldPos[1])))
      
      return Mobject

    self.wait()
    ExampleDot=Dot([2,2,0])
    MoveTo(ExampleDot,[2,2,0],[-1,-1,0])
    self.wait(3)