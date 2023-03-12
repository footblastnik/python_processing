shirina_x = 0
x = 0
y = 0
def setup():
    size(600,600)
def draw():
    global shirina_x,x,y
    background(255)
    fill(random(255),random(255),random(255))
    
    ellipse(300,300,100,100)
    strokeWeight(shirina_x)
    
    line(300,shirina_x,300,250)
    line(260,300,shirina_x,shirina_x)
    line(550,x,450,120)
    shirina_x = shirina_x + 1
    x += 1
    y -= 1
 
 
