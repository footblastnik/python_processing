x0= 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y0 = random(1000)
y1 = random(1000)
y2 = random(1000)
y3 = random(1000)
y4 = random(1000)
y5 = random(1000)
speed_0 = 5
speed_1 = 8
speed_2 = 11
speed_3 = 15
speed_4 = 20
flag = 0

def game_over(flag):
    background(0)
    
def setup():
    size(1000,1000)

def draw():
    global flag
    global x3,x4,x2,x1,x0
    global y0,y1,y2,y3,y4,y5
    global speed_0,speed_1,speed_2,speed_3,speed_4
    if not flag:
        background(0,250,250)
        ellipse(x0,y0,40,40)
        fill(0)
        ellipse(x1,y1,40,40)
        fill(250,250,0)
        ellipse(x4,y4,80,80)
        ellipse(x3,y3,60,60)
        fill(255,0,0)
        ellipse(x2,y5,20,20)
        
        dist1 = sqrt((x1 - mouseX)**2 + (y1 - mouseY)**2)
        dist2 = sqrt((x2 - mouseX)**2 + (y5 - mouseY)**2)
        dist3 = sqrt((x3 - mouseX)**2 + (y3 - mouseY)**2)
        dist4 = sqrt((x4 - mouseX)**2 + (y4 - mouseY)**2)
        dist5 = sqrt((x0 - mouseX)**2 + (y0 - mouseY)**2)
        dist6 = sqrt((x3 - mouseX)**2 + (300 - mouseY)**2)
        fill(0)
        text(dist1, 30, 30)
        text(dist2, 30, 60)
        text(dist3 ,30, 90)
        text(dist4 ,30, 120)
        text(dist5 ,30, 150)
        text(dist6 ,30, 180)
        fill(250,250,0)
        ellipse(x2,y2,20,20) 
        ellipse(x3,300,10,10)
    
        ellipse(mouseX,mouseY,random(40),(40))
        strokeWeight(random(5))
        fill(250,0,0)
        
    
    
            
        x0 = x0 + speed_0
        x1 = x1 + speed_1
        x2 = x2 + speed_2
        x3 = x3 + speed_3
        x4 = x4 + speed_4
        if x0 > width:
            x0 = 0
            y0 = random(500,700)
            speed_0 = random(5,15)
            
        if x1 > width:
            x1 = 0 
            y1 = random(300,600)
            speed_1 = random(5,15)
            
        if x2 > width:
            x2 = 0 
            y2 = random(100,800)
            speed_2 = random(5,15)
            
        if x3 > width:
            x3 = 0 
            y3 = random(50,1000)  
            
        if x4 > width:
            x4 = 0 
            y4 = random(0,1000) 
            y5 = random(0,900)
        if mousePressed:
            if mouseX < 470 and mouseY < 465 and mouseX > 390 and mouseY > 425  
           
        if dist1 < 20:
            flag = 1
        if dist2 < 20:
            flag = 1
        if dist3 < 35:
            flag = 1
        if dist4 < 25:
            flag = 1
        if dist5 < 30:
            flag = 1
        if dist6 < 30:
            flag = 1  
    else:
        textSize(80)
        fill(255,0,0)
        text("game over",325,400)  
        fill(255)    
        rect(390,425,80,40)
     
        
