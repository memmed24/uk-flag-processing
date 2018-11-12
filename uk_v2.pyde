grid = [[-1]*21 for n in range (35)]


def setup():
    size(1750, 1050)
    
w = 50

def draw():
     
    background(0, 31, 126)
    
    

    #scotland
    fill(255)
    stroke(255)
    triangle(0, 100, 0, 0, 200, 0)
    triangle(1550, 0, 1750, 100, 1750, 0)
    triangle(0, 950, 0, 1050, 200, 1050)
    triangle(1750, 1050, 1550, 1050, 1750, 950)
    stroke(255)
    quad(200, 0, 1750, 950, 1550, 1050, 0, 100)
    quad(1550, 0, 0, 950, 200, 1050, 1750, 100)
    
    #n.ireland
    fill(208, 12, 39)
    quad(0, 75, 0, 0, 701, 450, 623, 450)
    quad(125, 1050, 0, 1050, 750, 600, 800, 640)
    quad(1750, 975, 1750, 1050, 1080, 650, 1225, 650)
    quad(1750, 0, 1625, 0, 900, 450, 1000, 450)
    for i in range(len(grid)):
        for j in range(len(grid[i])): 
            noStroke()
            # stroke(0)
            noFill()
            
            if(i == 15 or i == 19 or j == 8 or j == 12):
                fill(255)
            if(i == 17 or i == 16 or i == 18 or j == 10 or j == 11 or j == 9):
                stroke(208, 12, 39)
                fill(208, 12, 39)

            
            rect(i * w, j * w, w, w)
            

  
    
    
