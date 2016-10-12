'''
Created on Dec 16, 2014

@author: justin
'''
import sys, pygame
from random import randint
from random import random
import math, time
from datetime import datetime

pygame.init()

nowHealth = time.time()
nowHunger = time.time()
currentTime = datetime.now()
hour = currentTime.hour
print hour

try:
    data = open("fishData.txt", "r+")
    
    fishName = data.readline()
    fishName = fishName.strip()
    print "yesName"
    fishHealth = int(data.readline())
    print "yesHealth"
    fishHunger = int(data.readline())
    print "yesHunger"
    money = int(data.readline())
    print "yesMoney"
    image = data.readline()
    image = image.strip()
    print "yesImage"
    lastTime = float(data.readline())
    print "yesLastTime"
except:
    fishName = "Tyrone"
    fishHealth = 100
    fishHunger = 100
    money = 500
    image = "Fishes/fish1.png"
    lastTime = time.time()
data.close()

print fishName, fishHealth, fishHunger, money, 
print "imageName '",image,"'", lastTime, time.time()

hoursPassed = int((time.time() - lastTime)/3600)
print hoursPassed
fishHunger -= hoursPassed
if fishHunger <= 25:
    fishHealth -= hoursPassed

class Fish(pygame.sprite.Sprite):
    def __init__(self, image_file, location, name, health, hunger):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.health = health
        self.hunger = hunger
        self.name = name
        self.vector = (0, 0)
        self.speed = 1
        self.origImage = self.image
        self.movingNow = False
        self.interval = 0
        self.timeElapsed = 0
        self.quadrant = 1
    def __repr__(self):
        print self.rect.center, self.name, self.health, self.hunger
    def rotate(self, angle):
        angle = -(angle * 180) / math.pi
        self.image = self.origImage
        if angle < -90 and angle > -270:
            self.image = pygame.transform.flip(self.image, False, True)
        self.image = pygame.transform.rotate(self.image, angle)
    def rotateTan(self, angle):
        angle = -(angle * 180) / math.pi
        angle = angle % 360
        self.image = self.origImage
        if angle > 90 and angle < 270:
            self.image = pygame.transform.flip(self.image, False, True)
        self.image = pygame.transform.rotate(self.image, angle)        
    def move(self):
        global numTimes
        
        if fish.hunger >= 75:
            magRange = 30
        elif fish.hunger >= 50:
            magRange = 20
        elif fish.hunger >= 25:
            magRange = 10
        elif fish.hunger >= 0:
            magRange = 1
        else:
            magRange = 0;
        hour = currentTime.hour
        if hour >= 20:
            magRange = 20
        
        if self.movingNow == False:
            self.turn = random() * math.pi * 2
            self.magnitude = randint(0, magRange)
            numTimes = randint(8, 20)
            self.origTimes = numTimes
            self.vector = [0, 0]
            self.movingNow = True
            self.rotate(self.turn)
        
        if numTimes > 0:
            numTimes -= 1
            
            self.rect.centerx += self.vector[0]
            self.rect.centery += self.vector[1]
            self.rect.centerx %= width
            self.rect.centery %= height
            
            R = self.magnitude * math.sin((math.pi * numTimes)/float(self.origTimes)) ** 2
            self.vector[0] = R * math.cos(self.turn)
            self.vector[1] = R * math.sin(self.turn)
            
        if numTimes == 0:
            self.movingNow = False
        screen.blit(self.image, self.rect)
    
    def moveToFood(self):
        part1 = pelletList[0].rect.centerx - fish.rect.centerx
        part1 /= 30.0
        part2 = pelletList[0].rect.centery - fish.rect.centery
        part2 /= 30.0
        
        #puts in radians automatically
        if part1 != 0:
            angle = math.atan2(part2, part1)
        elif part1 == 0:
            part1 = 0.00001
            angle = math.atan2(part2, part1)

        fish.rotateTan(angle)
        
        if abs(part1) > 1:
            fish.rect.centerx += part1
        else:
            if part1 >= 0:
                fish.rect.centerx += 1
            else:
                fish.rect.centerx -= 1
        
        if abs(part2) > 1:
            fish.rect.centery += part2
        else:
            if part2 >= 0:
                fish.rect.centery += 1
            else:
                fish.rect.centery -= 1
                
        fish.rect.centerx %= width
        fish.rect.centery %= height
        screen.blit(fish.image, fish.rect)
        
def drawFish():
    if len(pelletList) == 0 or fish.hunger == 100:
        fish.move()
    elif len(pelletList) > 0 and fish.hunger < 100:
        fish.moveToFood()
    
def save():
    data = open("fishData.txt", "w")
    data.write(fish.name + "\n")
    data.write(str(fish.health) + "\n")
    data.write(str(fish.hunger) + "\n")
    data.write(str(money) + "\n")
    data.write(image + "\n")
    data.write(str(time.time()) + "\n")
    data.close()
    
def calcHunger():
    global nowHunger
    
    decreaseHunger = False

    now = time.time()
    if now - nowHunger >= 3600:
        nowHunger = now
        decreaseHunger = True
    if decreaseHunger and fish.hunger > 1:
        fish.hunger -= 2
        print "food", fish.hunger
        print "one hour"

def calcHealth():
    global nowHealth
    
    decreaseHealth = False
    
    now = time.time()
    if now - nowHealth >= 3600:
        nowHealth = now
        decreaseHealth = True
    if decreaseHealth and fish.health > 0 and fish.hunger <= 25:
        fish.health -= 2
        print "health", fish.health
    if decreaseHealth and fish.hunger >= 75:
        fish.health += 2
    decreaseHealth = False
        
class Button(pygame.sprite.Sprite):
    def __init__(self, location, image_file, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.right, self.rect.top = location
        self.name = name
    def pressed(self):
        self.image = pygame.image.load("Buttons/" + self.name + "Pressed.png")
    def notPressed(self):
        self.image = pygame.image.load("Buttons/" + self.name + "Button.png")

def drawButtons():
    for button in buttonList:
        screen.blit(button.image, button.rect) 
        
def checkPress(mousex, mousey, mouseDown):
    global money, mousePress
    for button in buttonList:
        if mousex < button.rect.right \
        and mousex > button.rect.left \
        and mousey < button.rect.bottom \
        and mousey > button.rect.top \
        and mouseDown:
            button.pressed()
            if button.name == "feed" and money >= 1:
                money -= 1
                newPellet = Pellets([randint(0, 1000), -10], "Fishes/pellet.png")
                pelletList.append(newPellet)
                mousePress = False
        else:
            button.notPressed()

class Pellets(pygame.sprite.Sprite):
    def __init__(self, location, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        
def drawPellets():
    j = 0
    for i in range(len(pelletList)):
        pelletList[j].rect.centery += 1
        screen.blit(pelletList[j].image, pelletList[j].rect)
        if pelletList[j].rect.centery > height:
            pelletList.remove(pelletList[j])
            j -= 1
        elif pygame.sprite.spritecollide(fish, [pelletList[j]], False) and fish.hunger < 100:
            fish.hunger += 1
            pelletList.remove(pelletList[j])
            j -= 1
        j += 1

class Bar(pygame.sprite.Sprite):
    def __init__(self, location, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def drawBars():
    for bar in barList:
        screen.blit(bar.image, bar.rect)
    drawBarBits()
        
class BarBits(pygame.sprite.Sprite):
    def __init__(self, location, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def change(self, color):
        if color == "green":
            self.image = pygame.image.load("Healther/green.png")
        elif color == "yellow":
            self.image = pygame.image.load("Healther/yellow.png")
        elif color == "red":
            self.image = pygame.image.load("Healther/red.png")

def drawBarBits():
    if fish.hunger >= 0:
        if fish.hunger >= 75:
            hungerBarBit.change("green")
        elif fish.hunger >= 25:
            hungerBarBit.change("yellow")
        elif fish.hunger >= 0:
            hungerBarBit.change("red")
        for i in range(fish.hunger):
            if i < 100:
                coor = [(i) * 3, height - hungery + 1]
                screen.blit(hungerBarBit.image, coor)
    text1 = "Hunger         " + str(fish.hunger)
    t1 = font.render(text1, 1, (0, 0, 0))
    screen.blit(t1, [30, height - hungery + 1])
    
    if fish.hunger > 100 and fish.health >= 0:
        fish.health -= 3
        fish.hunger = 100
        if fish.health < 0:
            fish.health = 0
            
    if fish.health >= 0:
        if fish.health >= 75:
            healthBarBit.change("green")
        elif fish.health >= 25:
            healthBarBit.change("yellow")
        elif fish.health >= 0:
            healthBarBit.change("red")
        for i in range(fish.health):
            if i < 100:
                coor = [(i) * 3, height - healthy + 1]
                screen.blit(healthBarBit.image, coor)
    if fish.health > 100:
        fish.health = 100
    text2 = "Health         " + str(fish.health)
    t2 = font.render(text2, 1, (0, 0, 0))
    screen.blit(t2, [30, height - healthy + 1])

def displayMoney():
    text = "Money: " + str(money)
    t = font2.render(text, 1, (0, 0, 0))
    screen.blit(t, [15, 8])

def displayName():
    nameText = fish.name
    t = font3.render(nameText, 1, (0, 0, 0))
    screen.blit(t, [725, 8])

def drawMonameBar():
    screen.blit(monameBar, [0, 0])

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Saniquarium")
screen.fill([47, 120, 29])
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 50)
font3 = pygame.font.Font(None, 75)

moving = False
numTimes = 0
interval = 0

pause = False

fish = Fish(image, [width/2, height/2], fishName, fishHealth, fishHunger)

pelletList = []

buttonx = 150
buttony = 37.5
buttonList = []
feedButton = Button([width, buttony], "Buttons/feedButton.png", "feed")
cleanButton = Button([width, buttony * 2 + buttonx], "Buttons/cleanButton.png", "clean")
buyButton = Button([width, buttony * 3 + buttonx * 2], "Buttons/buyButton.png", "buy")
buttonList.append(feedButton)
buttonList.append(cleanButton)
buttonList.append(buyButton)
mousex = 0
mousey = 0
mousePress = False
pressedTime = 0
nowPress = 0

barList = []
healthy = 100
hungery = 50
healthBar = Bar([0, height - healthy], "Healther/healtherBar.png")
hungerBar = Bar([0, height - hungery], "Healther/healtherBar.png")
barList.append(healthBar)
barList.append(hungerBar)

healthBarBit = BarBits([500, 300], "Healther/green.png")
hungerBarBit = BarBits([500, 300], "Healther/green.png")

monameBar = pygame.image.load("monameBar.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                save()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                pause = not pause
        elif event.type == pygame.MOUSEMOTION:
            mousex = event.pos[0]
            mousey = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePress = True
            pressedTime = time.time()
    if pause == False:          
#         green
#         screen.fill([47, 120, 29])
        screen.fill([42,186,201])
        fish.interval += 1
        drawFish()
        drawPellets()
        drawMonameBar()
        checkPress(mousex, mousey, mousePress)
        nowPress = time.time()
        if nowPress - pressedTime > .1:
            mousePress = False
        drawButtons()
        drawBars()
        calcHunger()
        calcHealth()
        displayMoney()
        displayName()
    pygame.display.flip()
    clock.tick(20)