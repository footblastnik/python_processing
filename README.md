# python_processingx = 1
def setup():
    size(800,800)
    colorMode(HSB)
    
def draw():
    global x
    fill(255,255,x)
    ellipse(100,300,80,80)
    fill(255,x,255)
    ellipse(300,300,80,80)
    fill(x,255,255)
    ellipse(500,300,80,80)
    x = x + 1
