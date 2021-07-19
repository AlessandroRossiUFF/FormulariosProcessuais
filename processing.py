


from browser import window # document, , alert
import random 


verm = [21, 22, 23, 24];
gren = [21, 22, 23, 24];
blue = [21, 22, 23, 24];
colorlist = ['purple','red', 'yellow', 'turquoise', 'orange']
def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.frameRate(40);
        p.createCanvas(700, 410)
        p.background(205)
        p.rectMode(p.CENTER)
    

    def draw():
       # cor=verm
        p.noStroke()
        p.fill(random.choice(colorlist))
        p.ellipse(p.mouseX,p.mouseY,50,50)

    
    def mousePressed(self):
   
        p.background(random.choice(colorlist))
    

    def keyPressed(self):
      if p.key==" ":
        print("Hallo")
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
