x = 1
x1 = 1
        
def setup():
    size(800,800)
    colorMode(HSB,360,100,100)
def draw():
    global x,x1
    fill(255,0,0)
    ellipse(x1,x1,400,400)

    fill(255,20,x)
    ellipse(280,350,80,80)
    fill(0,x,20)
    ellipse(480,350,80,80)
   

    
    x = x + 1
    x1 = x1 + 1
   
