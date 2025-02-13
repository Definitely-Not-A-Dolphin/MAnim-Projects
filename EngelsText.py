from manim import *

def addPosition(list1,list2):
  result = [0,0,0]
  for i in range(0,2,1):
    result[i]=list1[i]+list2[i]
  
  return result

class Scene1(Scene):
  def construct(self):
    
    def Ophelia(position,mirror):
      result = VGroup()
      
      #Body
      bodyTopPos = addPosition(position,[0,.6,0])
      bodyBottomPos=addPosition(position,[0,-.6,0])
      bodyLine = Line(bodyTopPos,bodyBottomPos)
      
      #Arms
      armCenterPos = addPosition(position,[0,.3,0])
      armLeftPos = addPosition(position,[-.4,-.2,0])
      armRightPos = addPosition(position,[.4,-.2,0])
      armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
      armRight = Line(armRightPos,armCenterPos,color=WHITE)
      
      #Legs
      legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
      legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
      legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
      legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
      
      #Head
      headCenterPos=addPosition(bodyTopPos,[0,.6,0])
      head=Circle(color=WHITE,radius=.5).move_to(addPosition(position,[0,1.1,0]))
      
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
    
    def Hamlet(position):
      result = VGroup()
      
      #Body
      bodyTopPos = addPosition(position,[0,.6,0])
      bodyBottomPos=addPosition(position,[0,-.6,0])
      bodyLine = Line(bodyTopPos,bodyBottomPos)
      
      #Arms
      armCenterPos = addPosition(position,[0,.3,0])
      armLeftPos = addPosition(position,[-.4,-.2,0])
      armRightPos = addPosition(position,[.4,-.2,0])
      armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
      armRight = Line(armRightPos,armCenterPos,color=WHITE)
      
      #Legs
      legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
      legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
      legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
      legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
      
      #Head
      headCenterPos=addPosition(bodyTopPos,[0,.6,0])
      head=Circle(color=WHITE,radius=.5).move_to(addPosition(position,[0,1.1,0]))
      
      faceDot1Pos=addPosition(headCenterPos,[0.325,-0.2,0])
      faceDot2Pos=addPosition(headCenterPos,[0.075,-0.2,0])
      faceDot3Pos=addPosition(headCenterPos,[0.05,-0.4,0])
      faceDot4Pos=addPosition(headCenterPos,[0.35,-0.4,0])
      faceLine1=Line(faceDot1Pos,faceDot4Pos,color=WHITE)
      faceLine2=Line(faceDot2Pos,faceDot3Pos,color=WHITE)
      
      mouthDot1=Dot(addPosition(headCenterPos,[.15,-.35,0]))
      mouthDot2=Dot(addPosition(headCenterPos,[.25,-.35,0]))
      mouthLine=Line(addPosition(headCenterPos,[.15,-.35,0]),addPosition(headCenterPos,[.25,-.35,0]),color=WHITE)
      
      #Hair
      hair1Pos=addPosition(headCenterPos,[0.2,-0.3,0])
      hair1Diff=Difference(head,Square(side_length=1,color=GRAY).move_to(hair1Pos))
      
      headFill=Difference(Circle(radius=.5).move_to(addPosition(position,[0,1.1,0])),Square(side_length=1,color=GRAY).move_to(hair1Pos),fill_opacity=1, color=GRAY)
      
      result.add(head,
                 bodyLine, 
                 armLeft, armRight,
                 legLeft, legRight,
                 hair1Diff, headFill,
                 faceLine1, faceLine2,
                 mouthLine
      )
      return result
    
    def Polonius(position):
      result = VGroup()
      
      #Body
      bodyTopPos = addPosition(position,[0,.6,0])
      bodyBottomPos=addPosition(position,[0,-.6,0])
      bodyEllipse = Ellipse(height=1.2,width=0.6,color=GRAY,fill_opacity=1).move_to(position)
      
      #Arms
      armCenterPos = addPosition(position,[0,.3,0])
      armLeftPos = addPosition(position,[-.5,-.2,0])
      armCenterLeftPos = addPosition(armCenterPos,[-.1,0,0])
      armRightPos = addPosition(position,[.5,-.2,0])
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
      head=Circle(color=WHITE,radius=.5).move_to(addPosition(position,[0,1.1,0]))

      #Mustache
      mustache=Rectangle(height=0.15, width=0.4,fill_opacity=1,color=GRAY).move_to(addPosition(headCenterPos,[0.2,-0.25,0]))
            
      result.add(head,
                 bodyEllipse, 
                 armLeft, armRight,
                 legLeft, legRight,
                 mustache
      )
      return result
    
    def AuntAgony(position):
      result = VGroup()
      
      #Body
      bodyTopPos = addPosition(position,[0,.6,0])
      bodyBottomPos=addPosition(position,[0,-.6,0])
      bodyLine = Line(bodyTopPos,bodyBottomPos)
      
      #Arms
      armCenterPos = addPosition(position,[0,.3,0])
      armLeftPos = addPosition(position,[-.4,-.2,0])
      armRightPos = addPosition(position,[.4,-.2,0])
      armLeft = Line(armLeftPos,armCenterPos,color=WHITE)
      armRight = Line(armRightPos,armCenterPos,color=WHITE)
      
      #Legs
      legLeftPos = addPosition(bodyBottomPos,[.4,-0.7,0])
      legRightPos = addPosition(bodyBottomPos,[-.4,-0.7,0])
      legLeft = Line(legLeftPos,bodyBottomPos,color=WHITE)
      legRight = Line(legRightPos, bodyBottomPos, color=WHITE)
      
      headCenterPos=addPosition(bodyTopPos,[0,.6,0])     
      hat1=addPosition(headCenterPos,[.4,-.05,0])
      hat3=addPosition(headCenterPos,[.6,.15,0])
      hat2=addPosition(headCenterPos,[0,.25,0])
      hat4=addPosition(headCenterPos,[0.2,.45,0])
      
      #Head
      head=Circle(color=WHITE,radius=.5).move_to(addPosition(position,[0,1.1,0]))
      temp1=Difference(head,Polygon(addPosition(headCenterPos,[.6,-.2,0]),hat3,hat4,addPosition(headCenterPos,[-.2,.4,0])))
      
      #Hat
      hatgroup=VGroup()
      hatBrim=Line(addPosition(headCenterPos,[.6,-.2,0]),addPosition(headCenterPos,[-.2,.4,0]))
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
    
    self.wait(1)
    
    self.play(FadeIn(Hamlet([-1,1,0]),
                     Ophelia([1,1,0], True),
                     Polonius([-3,1,0]),
                     AuntAgony([6,-2.5,0])
                     )
              )
    
    self.wait(3)