import pygame
import sys
import math
import time
import random

WIDTH = 800
HEIGHT = int(WIDTH * 0.8)

pygame.init()
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


font = pygame.font.SysFont('Futura', 15)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def goto_main_menu():
    # import button
    quit()
    
def main():
    # define game varibles 
    GRAVITY = 1
    PLAYER_AMMO = 20
    PLAYER_MONEY = 20
    PLAYER_SHEILD = 0
    PLAYER_ARMOR = 0
    PLAYER_WEPIN = 1
    PLAYER_GRENADE = 4
    
    # define colors
    WHITE = (255, 255, 255) 
    GREEN1 = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREY = (119, 136, 153)

    FPS = 30
    
    # main

    # Create classes
    class Soldier():
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.dx = 0
            self.dy = 0
            self.width = width
            self.height = height
            self.speed = random.randint(5, 7)
            self.color=GREY
            self.friction = 0.9
            self.health = 30
            self.alive = True
            self.Fired = False
            self.x_moved = 0
            self.direction = 1 # 1: right, 0: left
            self.idle_counter = 0
            self.vision = pygame.Rect(0, 0, 150, 20)

            
        def goto(self, x, y):
            self.x = x
            self.y = y
            
        def render(self, camera):
            pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width/2.0-camera.x + WIDTH/2.0), int(self.y-self.height/2.0), self.width, self.height))

        def is_aabb_collision(self, other):
            # Axis Aligned Bounding Box
            x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
            y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
            return (x_collision and y_collision)
        
        def fireReady(self, bullet):
            # move bullet close to player
            bullet.x = self.x + self.direction * 20
            bullet.y = self.y
            self.Fired = True
            bullet.direction = self.direction
            bullet.flyingDistance = 0

        def shoot(self, bullet):
            if self.Fired == False:
                return
            
            # move bullet
            bullet.x += bullet.direction * 20
            bullet.flyingDistance += 20
            bullet.y = self.y

            if bullet.flyingDistance > 1.5 * WIDTH:
                self.Fired = False
                bullet.goto(100000, 100000)
                
                
        def ai(self):
            if self.alive and player.alive:

                if self.direction == 1:
                    self.x += self.speed
                    self.x_moved += self.speed
                else:
                    self.x -= self.speed
                    self.x_moved -= self.speed
                    
                if self.x_moved <= -100:
                    self.direction = 1
                    self.speed = 0
                elif self.x_moved >= 100:
                    self.direction = 0
                    self.speed = 0
                    
                # shoot
                enemy.shoot(bullet)
                
                if self.speed == 0:
                    self.idle_counter += 1
                    # check if idle counter is > then 50 to 70
                    if self.idle_counter >= random.randint(50, 70):
                        # set speed to 
                        self.speed = random.randint(4, 6)
                        self.idle_counter = 0
                if enemy.alive and player.alive == True:
                    enemy.vision.x = enemy.x
                enemy.vision.y = enemy.y
                if player.is_aabb_collision(enemy.vision):
                    enemy.speed = 0
                    enemy.fireReady(bullet)

                        
    class Grenade(Soldier):
        def __init__(self, x, y, width, height, direction):
            Soldier.__init__(self, x, y, width, height)
            self.timer = 100
            self.vel_y = -11
            self.speed = 7
            self.direction = direction
            self.throwing = False
            
        def update(self):
            grenade.throwing = True
            self.vel_y += GRAVITY
            self.dx = self.direction * self.speed
            self.dy = self.vel_y
            
            #check collision with floor
            for block in blocks:
                if self.is_aabb_collision(block):
                    self.dy = 300 - self.rect.bottom
                    self.speed = 0
                
    class Healthbar():
        def __init__(self, x, y, health, max_health):
            self.x = x
            self.y = y
            self.health = health
            self.max_health = max_health

        def draw(self, health):
            #update with new health
            self.health = health
            #calculate health ratio
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, RED, (self.x, self.y, 115, 20))
            pygame.draw.rect(screen, GREEN1, (self.x, self.y, 115 * ratio, 20))
            
    # class Explosion(self):
    #     def __init__(self):
    #         pygame.sprite.Soldier.__init__(self)
    #         self.timer = 2
            

    class Bullet(Soldier):
        def __init__(self, x, y, width, height, direction):
            Soldier.__init__(self, x, y, width, height)
            self.speed = 10
            self.direction = player.direction
            self.bullet_power = 1
            self.flyingDistance = 0
            self.color = WHITE


    class Player(Soldier):
        def __init__(self, x, y, width, height):
            Soldier.__init__(self, x, y, width, height)
            self.flip = False
            self.color=GREEN1
            self.cooldown = 0
            self.direction = 1
            self.speed = 10
            self.alive = True
            self.flip = False
            self.health = 100
            self.max_health = 100
                
        def check_health(self):
            if self.health > self.max_health:
                self.health = self.max_health
                
        def move(self):
            self.x += self.dx
            self.y += self.dy
            self.dy += GRAVITY
            
        def jump(self):
            self.dy -= 22
            self.y -= 22
            
        def left(self):
            self.dx -= 6
            if self.dx < -12:
                self.dx = -12

        def right(self):
            self.dx += 6
            if self.dx > 12:
                self.dx = 12
                
    class Camera():
        def __init__(self, target):
            self.x = target.x
            self.y = target.y
            
        def update(self, target):
            self.x = target.x
            self.y = target.y

    # Create game objects
    player = Player(600, 0, 20, 40)
    bullet = Bullet(10000, 10000, 5, 5, player.direction)
    grenade = Grenade(10000, 10000, 20, 20, player.direction)
    healthbar = Healthbar(5, 5, player.health, 100)
    #explosion = Explosion(10000, 10000, 20, 20)
    enemies = []
    enemies.append(Soldier(590, 370, 20, 40))
    enemies.append(Soldier(1500, 570, 20, 40))
    enemies.append(Soldier(1190, 570, 20, 40))
    enemies.append(Soldier(590, 570, 20, 40))
    enemies.append(Soldier(1540, 270, 20, 40))
    for enemy in enemies:
        enemy.color=RED
    waters = []
    waters.append(Soldier(3234, 555, 1200, 70))
    blocks = []
    blocks.append(Soldier(600, 200, 400, 20))
    blocks.append(Soldier(600, 400, 600, 20))
    blocks.append(Soldier(600, 600, 10000, 20))
    blocks.append(Soldier(1000, 500, 100, 200))
    blocks.append(Soldier(200, 500, 100, 200))
    blocks.append(Soldier(1500, 300, 400, 20))
    blocks.append(Soldier(1240, 200, 100, 20))
    blocks.append(Soldier(1000, 200, 100, 200))
    blocks.append(Soldier(50, 200, 50, 800))
    blocks.append(Soldier(2350, 400, 100, 300))
    blocks.append(Soldier(2450, 500, 100, 220))
    blocks.append(Soldier(2050, 513, 100, 200))
    blocks.append(Soldier(2050, 513, 100, 200))
    blocks.append(Soldier(2050, 513, 100, 200))
    blocks.append(Soldier(2050, 513, 100, 200))
    blocks.append(Soldier(2050, 513, 100, 200))
    blocks.append(Soldier(2830, 470, 100, 20))
    blocks.append(Soldier(3120, 360, 100, 20))
    blocks.append(Soldier(2550, 550, 150, 120))
    blocks.append(Soldier(3350, 390, 150, 20))
    blocks.append(Soldier(3570, 450, 100, 20))

    for water in waters:
        water.color=BLUE

    # Create camera object
    camera = Camera(player)

    # Main game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Move/Update objects
        player.move()
        camera.update(player)   

        for enemy in enemies:
            enemy.ai()
                
        player.shoot(bullet)
        # grenade.update()

        # Keyboard events
        if player.alive == True:
            keys = pygame.key.get_pressed()
            if keys[pygame. K_LEFT]:
                player.left( )
                player.direction = -1
            elif keys[pygame.K_RIGHT]:
                player.right()
                player.direction = 1
            elif keys[pygame.K_SPACE]:
                if PLAYER_AMMO > 0 and player.Fired == False:
                    player.fireReady(bullet)
                    PLAYER_AMMO -= 1
            elif keys[pygame.K_UP]:
                for block in blocks:
                    if player.is_aabb_collision(block):
                        player.jump()
                        break
            elif keys[pygame.K_g]:
                if PLAYER_GRENADE > 0:
                    if grenade.throwing == False:
                        grenade.update()
                        grenade.throwing = False
                        PLAYER_GRENADE -= 1
                        # grenade.explode()
            elif PLAYER_MONEY >= 100 and keys[pygame.K_s]:
                if keys[pygame.K_RETURN]:
                    PLAYER_ARMOR += 1
                    PLAYER_MONEY -= 100
                    time.sleep(0.2) # to avoid spend twice
            elif PLAYER_MONEY >= 200 and keys[pygame.K_d]:
                if keys[pygame.K_RETURN]:
                    PLAYER_WEPIN += 1
                    PLAYER_MONEY -= 200
                    time.sleep(0.2)
            elif PLAYER_MONEY >= 50 and keys[pygame.K_a]:
                if keys[pygame.K_RETURN]:
                    PLAYER_SHEILD += 1
                    PLAYER_MONEY -= 50
                    time.sleep(0.2)
                    
            if PLAYER_ARMOR == 1:
                if bullet.is_aabb_collision(player):
                    if player.alive == True:
                        bullet.goto(10000, 10000)
                        player.health -= 5
                        if player.health < 1:
                            PLAYER_MONEY += 20
                            player.width = 40
                            player.height = 20
                            player.y += 10
                            player.alive = False
                        elif PLAYER_WEPIN == 1:
                            for enemy in enemies:
                                if bullet.is_aabb_collision(enemy):
                                    if enemy.alive == True:
                                        bullet.goto(10000, 10000)
                                        enemy.health -= 5
                                        if enemy.health < 1:
                                            PLAYER_MONEY += 20
                                            enemy.width = 40
                                            enemy.height = 20
                                            enemy.y += 10
                                            enemy.alive = False
                                        elif PLAYER_SHEILD == 5:
                                            if bullet.is_aabb_collision(player):
                                                if player.alive == True:
                                                    bullet.goto(10000, 10000)
                                                    player.health -= 5
                                                    if player.health < 1:
                                                        PLAYER_MONEY += 20
                                                        player.width = 40
                                                        player.height = 20
                                                        player.y += 10
                                                        player.alive = False
        # Check for collisions
        if player.is_aabb_collision(water):
            if player.alive == True:
                player.health -= 100
                if player.health < 1:
                    player.width = 40
                    player.height = 20
                    player.dx = 0
                    player.dy = 0
                    GRAVITY = 0
                    player.alive = False
                    # goto_main_menu()
                    return

        grenade.timer -= 1
        if grenade.timer < 1:
            grenade.goto(10000, 10000)
            for enemy in enemies:
                if grenade.is_aabb_collision(enemy):
                    if enemy.alive == True:
                        enemy.health -= 15
                        if enemy.health < 1:
                            PLAYER_MONEY += 20
                            enemy.width = 40
                            enemy.height = 20
                            enemy.y += 10
                            enemy.alive = False
                            grenade.throwing = False
        for block in blocks:
            if grenade.is_aabb_collision(block):
                grenade.dy = 0
                grenade.y = 0
        for enemy in enemies:
            if bullet.is_aabb_collision(enemy):
                if enemy.alive == True:
                    bullet.goto(10000, 10000)
                    player.Fired = False
                    enemy.health -= 10
                    if enemy.health < 1:
                        PLAYER_MONEY += 20
                        enemy.width = 40
                        enemy.height = 20
                        enemy.y += 10
                        enemy.alive = False

            if bullet.is_aabb_collision(player):
                if player.alive == True:
                    bullet.goto(10000, 10000)
                    player.health -= 10
                    if player.health < 1:
                        player.width = 40
                        player.height = 20
                        player.y += 5
                        player.alive = False
                        return
                        
            for block in blocks:
                if bullet.is_aabb_collision(block):
                    bullet.goto(10000, 10000)
                        
        for block in blocks:
            if player.is_aabb_collision(block):
                # Player is to the left
                if player.x < block.x - block.width/2.0 and player.dx > 0:
                    player.dx = 0   
                    player.x = block.x - block.width/2.0 - player.width/2.0
                # Player is to the right
                elif player.x > block.x + block.width/2.0 and player.dx < 0:
                    player.dx = 0
                    player.x = block.x + block.width/2.0 + player.width/2.0
                # Player is above
                elif player.y < block.y:
                    player.dy = 0
                    player.y = block.y - block.height/2.0 - player.height/2.0 + 2
                    player.dx *= block.friction
                # Player is below
                elif player.y > block.y:
                    player.dy = 0
                    player.y = block.y + block.height/2.0 + player.height/2.0
            if player.dy > 800:
                player.goto(600, 0)
                
        # Render (Draw stuff)
        # Fill the background color
        screen.fill(BLACK)
        # draw text on screen
        draw_text('AMMO: ' + str(PLAYER_AMMO), font, WHITE, 5, 25)     
        draw_text('MONEY: ' + str(PLAYER_MONEY), font, WHITE, 125, 5)
        draw_text('GRENADES: ' + str(PLAYER_GRENADE), font, WHITE, 5, 40)
        draw_text('SHEILD: $50', font, WHITE, 223, 5)
        draw_text('ARMOR: $100', font, WHITE, 323, 5)
        draw_text('WEAPON: $200', font, WHITE, 435, 5)

        healthbar.draw(player.health)
        player.check_health()
        
        if player.y > 800:
            player.goto(600, 0)
            player.dx = 0
            player.dy = 0
            
        # Render objects
        player.render(camera)
        bullet.render(camera)
        grenade.render(camera)
        #explosion.render(camera)
        for block in blocks:
            block.render(camera)
        for enemy in enemies:
            enemy.render(camera)
        for water in waters:
            water.render(camera)
            
        # Flip the display
        pygame.display.flip()

        # Set the FPS
        clock.tick(FPS)