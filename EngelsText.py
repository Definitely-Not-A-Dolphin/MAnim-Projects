from manim import *

def addPosition(list1,list2):
  result = [0,0,0]
  for i in range(0,2,1):
    result[i]=list1[i]+list2[i]
  
  return result

def Ophelia(mirror):
  result = VGroup()

  #Body
  bodyTopPos = [0,.6,0]
  bodyBottomPos=[0,-.6,0]
  bodyLine = Line(bodyTopPos,bodyBottomPos)
  
  #Arms
  armCenterPos = [0,.3,0]
  armLeftPos = [-.4,-.2,0]
  armRightPos = [.4,-.2,0]
  armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
  armRight = Line(armRightPos,armCenterPos,color=WHITE)
  
  #Legs
  legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
  legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
  legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
  legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
  
  #Head
  headCenterPos=addPosition(bodyTopPos,[0,.6,0])
  head=Circle(color=WHITE,radius=.5).move_to([0,1.1,0])
  
  m=1
  if(mirror):
    m=-1
  
  #Hair
  hair1Pos=addPosition(headCenterPos,[0.2*m,0.35,0])
  hair2Pos=addPosition(headCenterPos,[0.4*m,-.1,0])
  
  for k in [.4,.25,.1]:
    result.add(
      Difference(head,Circle(radius=k).move_to(hair1Pos),color=RED)
    )
  
  for k in [.3,.15]:
    result.add(
      Difference(head,Difference(Circle(radius=k, color=WHITE).move_to(hair2Pos),Circle(radius=.4,color=WHITE).move_to(hair1Pos)),color=RED)
    )
  
  result.add(head,
             bodyLine, 
             armLeft, armRight,
             legLeft, legRight,
  )
  return result

def Hamlet(mirror):
  result = VGroup()
  
  #Body
  bodyTopPos = [0,.6,0]
  bodyBottomPos=[0,-.6,0]
  bodyLine = Line(bodyTopPos,bodyBottomPos)
  
  #Arms
  armCenterPos = [0,.3,0]
  armLeftPos = [-.4,-.2,0]
  armRightPos = [.4,-.2,0]
  armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
  armRight = Line(armRightPos,armCenterPos,color=WHITE)
  
  #Legs
  legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
  legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
  legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
  legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
  
  p=1
  if (mirror):
    p=-1
  #Head
  headCenterPos=addPosition(bodyTopPos,[0,.6,0])
  head=Circle(color=WHITE,radius=.5).move_to([0,1.1,0])
  
  faceDot1Pos=addPosition(headCenterPos,[-0.325*p,-0.2,0])
  faceDot2Pos=addPosition(headCenterPos,[-0.075*p,-0.2,0])
  faceDot3Pos=addPosition(headCenterPos,[-0.05*p,-0.4,0])
  faceDot4Pos=addPosition(headCenterPos,[-0.35*p,-0.4,0])
  faceLine1=Line(faceDot1Pos,faceDot4Pos,color=WHITE)
  faceLine2=Line(faceDot2Pos,faceDot3Pos,color=WHITE)
  
  mouthDot1=Dot(addPosition(headCenterPos,[-.15*p,-.35,0]))
  mouthDot2=Dot(addPosition(headCenterPos,[-.25*p,-.35,0]))
  mouthLine=Line(addPosition(headCenterPos,[-.15*p,-.35,0]),addPosition(headCenterPos,[-.25*p,-.35,0]),color=WHITE)
  
  #Hair
  hair1Pos=addPosition(headCenterPos,[-0.2*p,-0.3,0])
  hair1Diff=Difference(head,Square(side_length=1,color=GRAY).move_to(hair1Pos))
  
  headFill=Difference(Circle(radius=.5).move_to([-0,1.1,0]),Square(side_length=1,color=GRAY).move_to(hair1Pos),fill_opacity=1, color=GRAY)
  
  result.add(head,
             bodyLine, 
             armLeft, armRight,
             legLeft, legRight,
             hair1Diff, headFill,
             faceLine1, faceLine2,
             mouthLine
  )
  return result

def Polonius(mirror):
  result = VGroup()
  
  #Body
  bodyTopPos = [0,.6,0]
  bodyBottomPos=[0,-.6,0]
  bodyEllipse = Ellipse(height=1.2,width=0.6,color=GRAY,fill_opacity=1)
  
  #Arms
  armCenterPos = [0,.3,0]
  armLeftPos = [-.5,-.2,0]
  armCenterLeftPos = addPosition(armCenterPos,[-.1,0,0])
  armRightPos = [.5,-.2,0]
  armCenterRightPos = addPosition(armCenterPos,[.1,0,0])
  armLeft = Line(armLeftPos,armCenterLeftPos,color=WHITE)
  armRight = Line(armRightPos,armCenterRightPos,color=WHITE)
  
  #Legs
  legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
  legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
  legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
  legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
  
  #Head
  headCenterPos=addPosition(bodyTopPos,[0,.6,0])
  head=Circle(color=WHITE,radius=.5).move_to([0,1.1,0])
  p=1
  if (mirror):
    p=-1
  
  #Mustache
  mustache=Rectangle(height=0.15, width=0.4,fill_opacity=1,color=GRAY).move_to(addPosition(headCenterPos,[-0.2*p,-0.25,0]))
        
  result.add(head,
             bodyEllipse, 
             armLeft, armRight,
             legLeft, legRight,
             mustache
  )
  return result

def AuntAgony(mirror):
  result = VGroup()
  
  #Body
  bodyTopPos = [0,.6,0]
  bodyBottomPos=[0,-.6,0]
  bodyLine = Line(bodyTopPos,bodyBottomPos)
  
  #Arms
  armCenterPos = [0,.3,0]
  armLeftPos = [-.4,-.2,0]
  armRightPos = [.4,-.2,0]
  armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
  armRight = Line(armRightPos,armCenterPos,color=WHITE)
  
  #Legs
  legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
  legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
  legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
  legRight = Line(legRightPos, bodyBottomPos, color=WHITE)

  p=1
  if (mirror):
    p=-1
  headCenterPos=addPosition(bodyTopPos,[0,.6,0])     
  hat1=addPosition(headCenterPos,[.4*p,-.05,0])
  hat3=addPosition(headCenterPos,[.6*p,.15,0])
  hat2=addPosition(headCenterPos,[0,.25,0])
  hat4=addPosition(headCenterPos,[0.2*p,.45,0])
  
  #Head
  head=Circle(color=WHITE,radius=.5).move_to([0,1.1,0])
  temp1=Difference(head,Polygon(addPosition(headCenterPos,[.6*p,-.2,0]),hat3,hat4,addPosition(headCenterPos,[-.2*p,.4,0])))
  
  #Hat
  hatgroup=VGroup()
  hatBrim=Line(addPosition(headCenterPos,[.6*p,-.2,0]),addPosition(headCenterPos,[-.2*p,.4,0]))
  hat=Polygon(hat1,hat2,hat4,hat3, color=WHITE)
  
  hatgroup.add(hat,
               hatBrim
  )
  
  result.add(temp1,
             bodyLine, 
             armLeft, armRight,
             legLeft, legRight,
             hatgroup
  )
  return result

class Scene1(Scene):
  def construct(self):

    def MoveTo(Mobject,OldPos,NewPos):
      self.play(Mobject.animate.shift(RIGHT*(NewPos[0]-OldPos[0])))
      self.play(Mobject.animate.shift(UP*(NewPos[1]-OldPos[1])))
      
      return Mobject

    self.wait(1)
    
    IntroText=Text('Animation Play Hamlet', font_size=50)
    IntroText2=Text('By Derek Verduijn',font_size=30).next_to(IntroText,DOWN)

    self.play(Write(IntroText))
    self.play(Write(IntroText2))
    self.wait(2)
    self.play(Unwrite(IntroText),Unwrite(IntroText2))

    AgonyPos=[6,-2.5,0]
    AgonyPer=always_redraw(lambda : AuntAgony(False).move_to(AgonyPos))
    self.play(FadeIn(AgonyPer))

    AgonyIntro=Text('I am A. Agony, an Agony aunt that writes for the Daily Dane. \n' 
                    'I have recently received a letter from Ophelia requesting advice, \n' 
                    'and here it is.',
                    font_size=25).to_edge(DL)

    Advice1=Text('The first thing that came to mind was to just talk with Lord \n'
                 'Hamlet about his mental health.',
                 font_size=25).to_edge(DL)

    self.play(Write(AgonyIntro))
    self.wait(3)
    self.play(Unwrite(AgonyIntro))
    self.play(Write(Advice1))

    OpheliaPer=Ophelia(False).move_to([8,0,0])
    HamletPer=Hamlet(True).move_to([-8,0,0])

    self.play(FadeIn(OpheliaPer), FadeIn(HamletPer))
    MoveTo(OpheliaPer,[8,0,0],[2,0,0])
    MoveTo(HamletPer,[-8,0,0],[-2,0,0])

    OphText1=Text('Dear Lord Hamlet, I have grown a concern \n'
                  'about your mental health, you seem to have \n'
                  'descended into madness!',
                  font_size=30).to_edge(UR)
    HamText1=Text('Oh Ophelia, do not concern about me. \n'
                  'I only avenge the death of my beloved father, \n'
                  'that is all.',
                  font_size=30).to_edge(UL)
    OphText2=Text('Well then, if that is truly the case, \n'
                  'than I shall worry no longer. Have a marvellous day.',
                  font_size=30).to_edge(UR)
    
    self.play(Write(OphText1))
    self.wait(3)
    self.play(Unwrite(OphText1))
    self.play(Write(HamText1))
    self.wait(3)
    self.play(Unwrite(HamText1))
    self.play(Write(OphText2))
    self.wait(3)
    self.play(Unwrite(OphText2))

    MoveTo(HamletPer,[-2,0,0],[-8,0,0])
    self.play(FadeOut(HamletPer))
    PoloniusPer=Polonius(True).move_to([-8,0,0])
    self.play(FadeIn(PoloniusPer))
    MoveTo(PoloniusPer,[-8,0,0],[-2,0,0])

    OphText4=Text('Father, I must say that I just had a \n'
                  'talk with Lord Hamlet and he only seems \n'
                  'to be upset about his father sudden death',
                  font_size=30).to_edge(UR)
    PolText1=Text('Ophelia, don\'t you see, he is \n'
                  'telling half the truth; do you \n'
                  'not realise that he is withholding information?',
                  font_size=30).to_edge(UL)
    OphText5=Text('But father, he really is just in disstress \n'
                  'solely about his father!',
                  font_size=30).to_edge(UR)
    PolText2=Text('So his insanity has managed to convince \n'
                  'you all these untruths? I forbid you from \n'
                  'speaking to him again!',
                  font_size=30).to_edge(UL)

    self.play(Write(OphText4))
    self.wait(3)
    self.play(Unwrite(OphText4))
    self.play(Write(PolText1))
    self.wait(3)
    self.play(Unwrite(PolText1))
    self.play(Write(OphText5))
    self.wait(3)
    self.play(Unwrite(OphText5))
    self.play(Write(PolText2))
    self.wait(3)
    self.play(Unwrite(PolText2))

    self.play(FadeOut(OpheliaPer),FadeOut(PoloniusPer))

    self.play(Unwrite(Advice1))
    AgonyText3=Text('Oh nay, well that clearly did not work \n'
                    'like I intended, let us try oncemore.',
                    font_size=30).to_edge(DL)
    self.play(Write(AgonyText3))

    self.wait(3)