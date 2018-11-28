import pygame
import time
import random

# initialising 
pygame.init()

# defining the colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
gray=(211,211,211)
green=(0,255,0)

# dimensions
block=20
width=800
height=600

# creating a display
Display=pygame.display.set_mode([width,height])

# creating a caption or title 
pygame.display.set_caption('Slither')

# declaring a global variable "direction"
global direction

# importing clock feature of time library(for no of frames per second)
clock=pygame.time.Clock()

# fonts
font=pygame.font.SysFont(None,40)
font1=pygame.font.SysFont(None,25)

# geting images
head=pygame.image.load('head.png')
tail=pygame.image.load('tail.png')
background=pygame.image.load('grass.png')
apple=pygame.image.load('apple.png')
body=pygame.image.load('body.png')

# geting sounds
eat=pygame.mixer.Sound("eat_apple.wav")

# defining function to display text on screen
def text_on_screen(text,color,x=400,y=100):
 message_shown=font.render(text,True,color)
 Display.blit(message_shown,[x,y])

# defining function to get score 
def score_on_screen(text,color,x=200,y=300):
 message_shown=font1.render(text,True,color)
 Display.blit(message_shown,[x,y])


# adding introduction to the game
def gameintro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        Display.fill(black)
        text_on_screen("SLITHER", white,200,200)
        text_on_screen("press c to play or q to quit!", white,200,400)
                           
    
                          
        pygame.display.update()
        clock.tick(5)           
# defining the main game loop
def gameloop():
 exit=False
 over=False

 # seting the x and y coordinates
 lead_x=width/2
 lead_y=height/2

 # initialising the change in coordinates
 lead_x_change=0
 lead_y_change=0
 
 # generating apples randomly
 applex=random.randrange(0,width-block)
 appley=random.randrange(0,height-block)
 
 sum1=1
 
 # initialising the no of frames per second to 10
 FPS=10
 
 # defining a list
 snakelist=[]

 # initialising the snake 
 direction="right"
 
 # defining the snake taking the snakelist as an attribute
 def snake(snakelist): #setting angle of rotation and coordinates of the snake head
  if direction=="right":
   snake_head=pygame.transform.rotate(head,270)
   Display.blit(snake_head,[snakelist[-1][0],snakelist[-1][1]])
  if direction=="left":
   snake_head=pygame.transform.rotate(head,90)
   Display.blit(snake_head,[snakelist[-1][0],snakelist[-1][1]])
  if direction=="up":
   snake_head=pygame.transform.rotate(head,0)
   Display.blit(snake_head,[snakelist[-1][0],snakelist[-1][1]])
  if direction=="down":
   snake_head=pygame.transform.rotate(head,180)
   Display.blit(snake_head,[snakelist[-1][0],snakelist[-1][1]])
  
  for locate in snakelist[:-1]:
   Display.blit(body,[locate[0],locate[1]])
  q=snakelist[::-1]
  if sum1>5: # location and angle of rotation of the tail
   if (q[len(snakelist)-1][0]-q[len(snakelist)-2][0]<0):
    qtail=pygame.transform.rotate(tail,270)
    Display.blit(qtail,[(q[len(snakelist)-1][0]),(q[len(snakelist)-1][1])])
   if (q[len(snakelist)-1][0]-q[len(snakelist)-2][0]>0):
    qtail=pygame.transform.rotate(tail,90)
    Display.blit(qtail,[(q[len(snakelist)-1][0]),(q[len(snakelist)-1][1])])
   if (q[len(snakelist)-1][1]-q[len(snakelist)-2][1]>0):
    qtail=pygame.transform.rotate(tail,0)
    Display.blit(qtail,[(q[len(snakelist)-1][0]),(q[len(snakelist)-1][1])])
   if (q[len(snakelist)-1][1]-q[len(snakelist)-2][1]<0):
    qtail=pygame.transform.rotate(tail,180)
    Display.blit(qtail,[(q[len(snakelist)-1][0]),(q[len(snakelist)-1][1])])
 
  
 while  exit==False:
  while over==True: # adding menu if to play again or quit
   Display.blit(background,[0,0])
   pygame.draw.rect(Display,black,[0,100,800,100])
   text_on_screen("Press C to retry or Q to quit",red)
   pygame.display.update()
   
   for event in pygame.event.get(): # options to either quit or retry
    if event.type==pygame.QUIT:
     pygame.quit()
     quit()
    if event.type==pygame.KEYDOWN:
     if event.key==pygame.K_q:
      exit=True
      over=False
     
     if event.key==pygame.K_c:
      text_on_screen(str(sum1-1),black,300,100)
      pygame.display.update()
      time.sleep(1)
      gameloop()
  
  # movement of the snake
  for event in pygame.event.get():
   if event.type==pygame.QUIT:
    exit=True
   if (event.type==pygame.KEYDOWN):
    if ((event.key==pygame.K_LEFT) and (lead_x_change<=0)) :  
     direction="left"  
     lead_x_change=-20
     lead_y_change=0
    if ((event.key==pygame.K_RIGHT) and (lead_x_change>=0)):
     direction="right"  
     lead_x_change=20
     lead_y_change=0
    if ((event.key==pygame.K_UP) and (lead_y_change<=0)):
     direction="up"     
     lead_y_change=-20
     lead_x_change=0
    if ((event.key==pygame.K_DOWN) and (lead_y_change>=0)):
     direction="down"  
     lead_y_change=20
     lead_x_change=0
  
   
  
  # change in the coordinates
  lead_x+=lead_x_change
  lead_y+=lead_y_change
  
  # appending the snakehead
  snakehead=[]
  if lead_x>800:
   lead_x=lead_x-800
  if lead_x<0:
   lead_x=lead_x+800
  snakehead.append(lead_x)
  if lead_y>600:
   lead_y=lead_y-600
  if lead_y<0:
   lead_y=lead_y+600
  snakehead.append(lead_y)
  
  # appending snakelist with snakehead
  snakelist.append(snakehead)
  pygame.display.update()
  Display.blit(background,[0,0])
  Display.blit(apple,[applex,appley])
  score_on_screen("SCORE:"+str(sum1-1),black,710,5)

  if len(snakelist)>sum1:
   del snakelist[0]

  snake(snakelist)
  for i in snakelist[:-1]:
   if snakehead==i:
    Display.fill(red,rect=[i[0],i[1],20,20])
    time.sleep(2)
    over= True
  
  # sounds when snake eats a apple
  if(((applex +block >=lead_x>=applex)and(appley +block >=lead_y>=appley))or((applex +block >=lead_x+20>=applex)and(appley +block >=lead_y+20>=appley))):
   pygame.mixer.Sound.play(eat)
   sum1+=5
   applex=random.randrange(20,780)
   appley=random.randrange(30,height-block)
   if [applex,appley] in snakelist:
    applex=random.randrange(20,780)
    appley=random.randrange(30,height-block) 
  
  # increasing the speed of snake using no of frames per second
  pygame.display.update()
  if(11<=sum1<=31):
   FPS=13
  if(31<sum1<=51):
   FPS=16
  if(51<sum1<=71):
   FPS=19
  if(sum1>71):
   FPS=25
  clock.tick(FPS)


 
 pygame.quit()
 quit()

gameintro() # calling the gameinto function
gameloop()  # calling the gameloop function


