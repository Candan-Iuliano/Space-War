import os
import random
import turtle
import time

turtle.fd(0)
#sets animation speed to max
turtle.speed(0)
#changes background color
turtle.bgcolor("black")
turtle.bgpic("Space_Invaders_Background.gif")
turtle.title("Space War")
#hide the default turtle
turtle.ht()
#saves memory
turtle.setundobuffer(1)
#speeds up drawing
turtle.tracer(0)

turtle.register_shape("player_up.gif")
turtle.register_shape("player_right.gif")
turtle.register_shape("player_left.gif")
turtle.register_shape("player_down.gif")
turtle.register_shape("player_up_right.gif")
turtle.register_shape("player_up_left.gif")
turtle.register_shape("player_down_right.gif")
turtle.register_shape("player_down_left.gif")
turtle.register_shape("explosion.gif")
turtle.register_shape("invader_left.gif")
turtle.register_shape("invader_right.gif")
turtle.register_shape("ally_upright.gif")
turtle.register_shape("ally_upleft.gif")
turtle.register_shape("ally_downright.gif")
turtle.register_shape("ally_downleft.gif")

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        #Boundry Detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_Collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
         (self.xcor() <= (other.xcor() + 20)) and \
         (self.ycor() >= (other.ycor() - 20)) and \
         (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False





class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shape("player_right.gif")
        self.speed = 0
        self.lives = 3

    def turn_left(self):
        self.lt(45)
        if self.heading() == 0:
            self.shape("player_right.gif")
        if self.heading() == 45:
            self.shape("player_up_right.gif")
        if self.heading() == 90:
            self.shape("player_up.gif")
        if self.heading() == 135:
            self.shape("player_up_left.gif")
        if self.heading() == 180:
            self.shape("player_left.gif")
        if self.heading() == 225:
            self.shape("player_down_left.gif")
        if self.heading() == 270:
            self.shape("player_down.gif")
        if self.heading() == 315:
            self.shape("player_down_right.gif")

    def turn_right(self):
        self.lt(-45)
        if self.heading() == 0:
            self.shape("player_right.gif")
        if self.heading() == 45:
            self.shape("player_up_right.gif")
        if self.heading() == 90:
            self.shape("player_up.gif")
        if self.heading() == 135:
            self.shape("player_up_left.gif")
        if self.heading() == 180:
            self.shape("player_left.gif")
        if self.heading() == 225:
            self.shape("player_down_left.gif")
        if self.heading() == 270:
            self.shape("player_down.gif")
        if self.heading() == 315:
            self.shape("player_down_right.gif")

    def accelerate(self):
        self.speed += 1
        if self.speed > 3:
            self.speed = 3

    def decelerate(self):
        self.speed -= 1
        if self.speed < 0:
            self.speed = -1

    def move(self):
        self.fd(self.speed)
#Boundry Detection
        if self.xcor() > 290:
            self.setx(290)
            self.speed = 0
        if self.xcor() < -290:
            self.setx(-290)
            self.speed = 0
        if self.ycor() > 290:
            self.sety(290)
            self.speed = 0
        if self.ycor() < -290:
            self.sety(-290)
            self.speed = 0




class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        direction = random.randint(0,360)
        self.speed = 1
        self.setheading(direction)
        if self.heading() > 270 or self.heading() < 90:
             self.shape("invader_right.gif")
        else:
            self.shape("invader_left.gif")
        self.death = 0
    def move(self):
        self.fd(self.speed)

        if self.xcor() > 500:
            self.setx(-1000)
            self.sety(1000)
        else:
            # Boundry Detection
            if self.xcor() > 290 and self.xcor() < 300:
                self.setx(290)
                self.rt(60)
                self.shape("invader_left.gif")
            if self.xcor() < -290 and self.xcor() > -300:
                self.setx(-290)
                self.rt(60)
                self.shape("invader_right.gif")
            if self.ycor() > 290 and self.ycor() < 300:
                self.sety(290)
                self.rt(60)
                if self.heading() > 270 or self.heading() < 90:
                    self.shape("invader_right.gif")
                else:
                    self.shape("invader_left.gif")
            if self.ycor() < -290 and self.ycor() > -300:
                self.sety(-290)
                self.rt(60)
                if self.heading() > 270 or self.heading() < 90:
                    self.shape("invader_right.gif")
                else:
                    self.shape("invader_left.gif")





class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        direction1 = random.randint(0, 360)
        self.speed = 1
        self.setheading(direction1)
        print(self.heading())
        if self.heading() > 0 and self.heading() < 90:
            self.shape("ally_upright.gif")
        elif self.heading() >= 90 and self.heading() <= 180:
             self.shape("ally_upleft.gif")
        elif self.heading() >= 180 and self.heading() <= 270:
            self.shape("ally_downleft.gif")
        else: #self.heading() >= 270 or self.heading() <= 360:
            self.shape("ally_downright.gif")

        self.death = 0

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 500:
            self.setx(-1000)
            self.sety(1000)
        else:

            # Boundry Detection
            if self.xcor() > 290 and self.xcor() < 300:
                self.setx(290)
                self.rt(60)
                if self.heading() > 0 and self.heading() < 90:
                    self.shape("ally_upright.gif")
                elif self.heading() >= 90 and self.heading() <= 180:
                    self.shape("ally_upleft.gif")
                elif self.heading() >= 180 and self.heading() <= 270:
                    self.shape("ally_downleft.gif")
                else:  # self.heading() >= 270 or self.heading() <= 360:
                    self.shape("ally_downright.gif")
            if self.xcor() < -290 and self.xcor() > -300:
                self.setx(-290)
                self.rt(60)
                if self.heading() > 0 and self.heading() < 90:
                    self.shape("ally_upright.gif")
                elif self.heading() >= 90 and self.heading() <= 180:
                    self.shape("ally_upleft.gif")
                elif self.heading() >= 180 and self.heading() <= 270:
                    self.shape("ally_downleft.gif")
                else:  # self.heading() >= 270 or self.heading() <= 360:
                    self.shape("ally_downright.gif")
            if self.ycor() > 290 and self.ycor() < 300:
                self.sety(290)
                self.rt(60)
                if self.heading() > 0 and self.heading() < 90:
                    self.shape("ally_upright.gif")
                elif self.heading() >= 90 and self.heading() <= 180:
                    self.shape("ally_upleft.gif")
                elif self.heading() >= 180 and self.heading() <= 270:
                    self.shape("ally_downleft.gif")
                else:  # self.heading() >= 270 or self.heading() <= 360:
                    self.shape("ally_downright.gif")
            if self.ycor() < -290 and self.ycor() > -300:
                self.sety(-290)
                self.rt(60)
                if self.heading() > 0 and self.heading() < 90:
                    self.shape("ally_upright.gif")
                elif self.heading() >= 90 and self.heading() <= 180:
                    self.shape("ally_upleft.gif")
                elif self.heading() >= 180 and self.heading() <= 270:
                    self.shape("ally_downleft.gif")
                else:  # self.heading() >= 270 or self.heading() <= 360:
                    self.shape("ally_downright.gif")





class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.1, stretch_len = 0.5, outline = None)
        self.speed = 20
        self.status = "ready"
        self.goto(500, 500)

    def fire(self):
        #winsound.PlaySound("sound.wav", winsound.SND_FILENAME |  winsound.SND_ASYNC)
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(500, 500)

        if self.status == "firing":
            self.fd(self.speed)

        #Border Check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(500, 500)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        #self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=None)
        self.goto(-1000, 1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            #self.fd(5)
            self.frame += 1


        if self.frame > 20:
            self.frame = 0
            self.goto (-1000, 1000)

        # if self.frame > 0:
        #     self.fd(5)
        #     self.frame += 1
        #
        # if self.frame > 10:
        #     self.frame = 0
        #     self.goto(-1000, 1000)



class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range (4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.write(msg, font=("Arial", 16, "normal"))


    def show_instructions(self):
        inst = "Press up to increase speed, down to decrease speed and the side arrows to turn \nWin by detroying all the tie fighters, but be careful not to shoot your allies"
        self.pen.penup()
        self.pen.goto(-300, -340)
        self.pen.write(inst, font=("Arial", 10, "normal"))
        self.pen.pendown()

    def game_win(self):
        win = "You Win"
        self.pen.penup()

        self.pen.goto(-30, 0)
        self.pen.write(win, font=("Arial", 16, "normal"))

    def game_over(self):
        win = "Game Over"
        self.pen.penup()

        self.pen.goto(-30, 0)
        self.pen.write(win, font=("Arial", 16, "normal"))

enemy_death = 0
ally_death = 0

#Create game objects
game = Game()

#draw game border
game.draw_border()

game.show_instructions()

#show game status
game.show_status()



#Create Sprites
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("square", "blue", 0, 0)
#ally = Ally("square", "blue", 0, 0)

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

particles = []
for i in range(1):
    particles.append(Particle("explosion.gif", "orange", 100, 0))

#Keyboard Bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()




#Main game loop
while True:
    turtle.update()
    time.sleep(0.01)


    player.move()
    #enemy.move()
    missile.move()

    #ally.move()

    for enemy in enemies:
        enemy.move()
        # Check for a collision
        if player.is_Collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
        # Check for a collision with the Missile and Enemy
        if missile.is_Collision(enemy):
            # x = random.randint(-250, 250)
            # y = random.randint(-250, 250)
            # enemy.goto(x,y)
            enemy.goto(-1000, 1000)
            enemy.speed = 0

            enemy_death += 1
            missile.status = "ready"
             # Increase Score
            game.score += 100
            game.show_status()
            #explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
                particle.setheading((random.randint(0,360)))


        if enemy_death == len(enemies):
            game.game_win()
            player.speed = 0
            turtle.onkey(None, "Up")
            turtle.onkey(None, "Left")
            turtle.onkey(None, "Right")
            turtle.onkey(None, "Down")
            for ally in allies:
                 ally.speed = 0



    for ally in allies:
        ally.move()
        # Check for a collision with the Missile and Ally
        if missile.is_Collision(ally):
            ally.goto(-1000, 1000)
            ally.speed = 0
            missile.status = "ready"
            ally_death += 1
            # Decrease score
            game.score -= 100
            game.show_status()
            # explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
                particle.setheading((random.randint(0, 360)))
        if ally_death == len(allies):
            game.game_over()
            player.speed = 0
            turtle.onkey(None, "Up")
            turtle.onkey(None, "Left")
            turtle.onkey(None, "Right")
            turtle.onkey(None, "Down")
            for enemy in enemies:
                enemy.speed = 0




    for particle in particles:
        particle.move()




delay = input()