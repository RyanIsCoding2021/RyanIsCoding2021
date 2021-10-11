import pygame
import sys
from pygame import mixer
import game_over
import math
import time
import random
import os

WIDTH = 800
HEIGHT = int(WIDTH * 0.8)

mixer.init()
pygame.init()

pygame.display.set_caption('Shooter')
pygame.display.set_icon(pygame.image.load("0.png"))
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


font = pygame.font.Font('PressStart2P-vaV7.ttf', 12)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

bg_scroll = 0
# load images
pine1_img = pygame.image.load('background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('background/mountain.png').convert_alpha()
sky_img = pygame.image.load('background/sky_cloud.png').convert_alpha()
grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()

def draw_bg():
    width = sky_img.get_width()
    for x in range(5):
        screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, HEIGHT - pine2_img.get_height()))

# load sounds
pygame.mixer.music.load('audio/music2.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 6000)
jump_fx = pygame.mixer.Sound('audio/jump.wav')
shot_fx = pygame.mixer.Sound('audio/shot.wav')
grenade_fx = pygame.mixer.Sound('audio/grenade.wav')


def g_render(color, x, y, width, height, camera):
    pygame.draw.rect(screen, color, pygame.Rect(int(x-width/2.0-camera.x + WIDTH/2.0), int(y-height/2.0), width, height))

def main():
    
    # define game varibles 
    GRAVITY = 0.75
    AMMO = 20
    SCORE = 0
    PLAYER_SHEILD = 0
    PLAYER_ARMOR = 0
    PLAYER_WEPIN_KIND = 1
    GRENADES = 4
    
    # define colors
    WHITE = (255, 255, 255) 
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREY = (119, 136, 153)

    FPS = 30
    
    # Create classes
    class Soldier():
        def __init__(self, char_type, x, y, width, height):
            self.x = x
            self.y = y
            self.dx = 0
            self.dy = 0
            self.width = width
            self.height = height
            self.speed = random.randint(5, 7)
            self.color = GREY
            self.friction = 0.9
            self.health = 30
            self.max_health = 100
            self.alive = True
            self.Fired = False
            self.x_moved = 0
            self.direction = 1 # 1: right, 0: left
            self.idle_counter = 0
            self.vision = pygame.Rect(0, 0, 150, 20)
            # animation varibles
            self.images = []
            self.index = 0
            self.counter = 0
            self.jump = False
            self.in_air = False
            self.frame_index = 0
            self.run = False
            self.death = False
            self.idle = True
            self.char_type = char_type
            self.animation_list = []
            self.action = 0
            self.update_time = pygame.time.get_ticks()
            self.stop_go_left = False
            self.stop_go_right = False
            
            # load all images for the players
            animation_types = ['Idle', 'Run', 'Jump']
            for animation in animation_types:
                # reset temporary list of images
                temp_list = []
                # count number of files in the folder
                num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
                for i in range(1, num_of_frames):
                    img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
                    img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                    temp_list.append(img)
                self.animation_list.append(temp_list)

            self.image = self.animation_list[self.action][self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        
        def update_animation(self):
            # update animation
            ANIMATION_COOLDOWN = 100
            # update image depending on current frame
            self.image = self.animation_list[self.action][self.frame_index]
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # if the animation has run out the reset back to the start
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0



        def update_action(self, new_action):
            # check if the new action is different to the previous one
            if new_action != self.action:
                self.action = new_action
                # update the animation settings
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()

        
        def goto(self, x, y):
            self.x = x
            self.y = y
            
        def render(self, camera):
            pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width/2.0-camera.x + WIDTH/2.0), int(self.y-self.height/2.0), self.width, self.height))

        def is_collision(self, other):
            # Axis Aligned Bounding Box
            x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
            y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
            return (x_collision and y_collision)
        
        def fireReady(self, bullet):
            shot_fx.play()
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
    
        def update_animation(self):
            # update animation
            ANIMATION_COOLDOWN = 100
            # update image depending on current frame
            self.image = self.animation_list[self.action][self.frame_index]
            # check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # if the animation has run out the reset back to the start
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
    
        def ai(self):
            if self.alive and player.alive:

                if self.direction == 1:
                    update_action_for_enemy_group()
                    self.x += self.speed
                    self.x_moved += self.speed
                else:
                    update_action_for_enemy_group()
                    self.x -= self.speed
                    self.x_moved -= self.speed
                    
                if self.x_moved <= -100:
                    update_action_for_enemy_group()
                    self.direction = 1
                    self.speed = 0
                elif self.x_moved >= 100:
                    update_action_for_enemy_group()
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
                if player.is_collision(enemy.vision):
                    enemy.speed = 0
                    enemy.fireReady(bullet)
                    
        def check_health(self):
            global player
            if self.health > self.max_health:
                self.health = self.max_health
                    
                
        def move(self):
            self.x += self.dx
            self.y += self.dy
            self.dy += GRAVITY
            
        def doJump(self):
            self.update_action(2)
            self.stop_go_right = False
            self.stop_go_left = False
            jump_fx.play()
            self.dy -= 22
            self.y -= 22
            
        def left(self):
            self.flip = True
            self.direction = 1
            if self.stop_go_left == True:
                return
            self.stop_go_right = False
            self.update_action(1)
            global bg_scroll
            bg_scroll -= 6
            self.dx -= 6
            if self.dx < -12:
                self.dx = -12

        def right(self):
            self.flip = False
            self.direction = -1
            if self.stop_go_right == True:
                return
            self.stop_go_left = False
            self.update_action(1)
            global bg_scroll
            bg_scroll += 6
            self.dx += 6
            if self.dx > 12:
                self.dx = 12
            
        # def draw(self):
            # screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)#, #player.x, player.y)
            
    class ScreenFade():
        def __init__(self, direction, color, speed):
            self.direction = direction
            self.color = color
            self.speed = speed
            self.fade_counter = 0

        def fade(self):
            self.fade_counter += self.speed
            pygame.draw.rect(screen, self.color, (0, 0, WIDTH, 0 + self.fade_counter))# vertical screen fade down

    # create Explosion class

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            for num in range(1, 6):
                img = pygame.image.load(f"img/explosion/exp{num}.png")
                img = pygame.transform.scale(img, (100, 100))
                self.images.append(img)
            self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.counter = 0

        def update(self):
            explosion_speed = 4
            # update explosion animation
            self.counter += 1

            if self.counter >= explosion_speed and self.index < len(self.images) - 1:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]

            # if the animation is complete, reset animation index
            if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()
                
    class Grenade(pygame.sprite.Sprite):
        def __init__(self, x, y, direction):
            pygame.sprite.Sprite.__init__(self)
            self.timer = 100
            self.vel_y = -11
            self.speed = 7
            self.image = grenade_img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.direction = direction
            self.x = x
            self.y = y

        def update(self):
            self.vel_y += GRAVITY
            dx = self.direction * self.speed
            dy = self.vel_y
            print(self.vel_y)

            # check collision with floor
            if self.rect.bottom + dy > 300:
                dy = 300 - self.rect.bottom
                self.speed = 0

            # check collision with walls
            if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH:
                self.direction *= -1
                dx = self.direction * self.speed

            # update grenade position
            self.rect.x += dx
            self.rect.y += dy

            # set the timer  
            self.timer -= 1
            if self.timer <= 0:
                explosion_group.draw(screen)
                explosion_group.update()
                    
                explosion = Explosion(self.x, self.y)
                explosion_group.add(explosion)
                
                # do damage to anyone that is nearby
                if abs(self.rect.centerx - player.rect.centerx) < 40 * 2 and \
                    abs(self.rect.centery - player.rect.centery) < 40 * 2:
                    player.health -= 100
                for enemy in enemy_group:
                    if abs(self.rect.centerx - enemy.rect.centerx) < 40 * 2 and \
                        abs(self.rect.centery - enemy.rect.centery) < 40 * 2:
                        enemy.health -= 100

    class Healthbar():
        def __init__(self, x, y, health, max_health):
            self.x = x
            self.y = y
            self.health = health
            self.max_health = max_health

        def draw(self, health):
            # update with new health
            self.health = health
            # calculate health ratio
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, RED, (self.x, self.y, 115, 20))
            pygame.draw.rect(screen, GREEN, (self.x, self.y, 115 * ratio, 20))

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height):
            pygame.sprite.Sprite.__init__(self)
            self.speed = 10
            self.direction = player.direction
            self.bullet_power = 1
            self.flyingDistance = 0
            self.color = WHITE
            self.width = width
            self.height = height
            self.x = x
            self.y = y
    class Camera():
        def __init__(self, target):
            self.x = target.x
            self.y = target.y
            
        def update(self, target):
            self.x = target.x
            self.y = target.y
            
    # create sprite groups
    explosion_group = pygame.sprite.Group()
    grenade_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    # Create game objects
    player = Soldier('player', 600, 0, 20, 40)
    bullet = Bullet(10000, 10000, 5, 5)
    grenade = Grenade(10000, 10000, player.direction)
    healthbar = Healthbar(5, 5, player.health, 100)
    # enemy_group
    enemy_group = []
    enemy_group.append(Soldier('enemy', 590, 370, 20, 40))
    enemy_group.append(Soldier('enemy', 1190, 570, 20, 40))
    enemy_group.append(Soldier('enemy', 590, 570, 20, 40))
    enemy_group.append(Soldier('enemy', 1540, 270, 20, 40))
    for enemy in enemy_group:
        enemy.color = RED
        
    block = pygame.draw.line(screen, RED, (0, 500), (10000, 30))
            # g_render(RED, 0, 500, 10000, 30, camera)

        
    # for enemy in enemy_group:
        
    def update_action_for_enemy_group():
        # idle
        for num in range(1, 5):
            img = pygame.image.load(f'img/enemy/Idle/{num}.png').convert_alpha()
            enemy.images.append(img)
        enemy.image = enemy.images[enemy.index]
        enemy.rect = enemy.image.get_rect()
        enemy.rect.center = [enemy.x, enemy.y]
        # run
        for num in range(0, 5):
            img = pygame.image.load(f'img/enemy/Run/{num}.png').convert_alpha()
            enemy.images.append(img)
        enemy.image = enemy.images[enemy.index]
        enemy.rect = enemy.image.get_rect()
        enemy.rect.center = [enemy.x, enemy.y]
        # jump
        img = pygame.image.load(f'img/enemy/Jump/0.png').convert_alpha()
        enemy.images.append(img)
        enemy.image = enemy.images[enemy.index]
        enemy.rect = enemy.image.get_rect()
        enemy.rect.center = [enemy.x, enemy.y]
        # death
        for num in range(0, 6):
            img = pygame.image.load(f'img/enemy/Death/{num}.png').convert_alpha()
            enemy.images.append(img)
        enemy.image = enemy.images[enemy.index]
        enemy.rect = enemy.image.get_rect()
        enemy.rect.center = [enemy.x, enemy.y]

    # Create camera object
    camera = Camera(player)
    
    ##################################################################################
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if player.health == 70:
            if Healthbar.draw:
                # calculate health ratio
                ratio = healthbar.health / healthbar.max_health
                pygame.draw.rect(screen, RED, (healthbar.x, healthbar.y, 115, 20))
                pygame.draw.rect(screen, (250, 255, 0), (healthbar.x, healthbar.y, 115 * ratio, 20))

        # Move/Update objects
        draw_bg()
        player.move()
        camera.update(player)
        screen.blit(player.image, (player.x, player.y)) 
        for enemy in enemy_group:
            screen.blit(enemy.image, (enemy.x, enemy.y)) 

        player.update_animation()

        #update player actions
        if player.alive:
            if player.in_air:
                player.update_action(2) # 2: jump
            elif player.dx > 0 or player.dx < 0:
                player.update_action(1) # 1: run
            else:
                player.update_action(0) # 0: idle

        for enemy in enemy_group:
            enemy.ai()
                
        player.shoot(bullet)
        # grenade.update()

        # Keyboard events
        if player.alive == True:
            keys = pygame.key.get_pressed()
            if keys[pygame. K_LEFT] or keys[pygame.K_a]:
                player.left( )
                player.direction = -1
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.right()
                player.direction = 1
            elif keys[pygame.K_SPACE]:
                if AMMO > 0 and player.Fired == False:
                    player.fireReady(bullet)
                    AMMO -= 1
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                if player.is_collision(block):
                    player.in_air = True
                    player.doJump()
                    player.in_air = False
                    break
            elif keys[pygame.K_q]:
                if GRENADES > 0:
                    grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),\
                    player.rect.top, player.direction)
                    grenade_group.add(grenade)
                    GRENADES -= 1
                    # grenade.explode()
            elif SCORE >= 100 and keys[pygame.K_s]:
                if keys[pygame.K_RETURN]:
                    PLAYER_ARMOR += 1
                    SCORE -= 100
                    time.sleep(0.2) # to avoid spend twice
            elif SCORE >= 200 and keys[pygame.K_d]:
                if keys[pygame.K_RETURN]:
                    PLAYER_WEPIN_KIND += 1
                    SCORE -= 200
                    time.sleep(0.2)
            elif SCORE >= 50 and keys[pygame.K_a]:
                if keys[pygame.K_RETURN]:
                    PLAYER_SHEILD += 1
                    SCORE -= 50
                    time.sleep(0.2)
                    
            if PLAYER_ARMOR == 1:
                if bullet.is_collision(player):
                    if player.alive == True:
                        bullet.goto(10000, 10000)
                        player.health -= 5
                        if player.health < 1:
                            SCORE += 20
                            player.width = 40
                            player.height = 20
                            player.y += 10
                            player.alive = False
                        elif PLAYER_WEPIN_KIND == 1:
                            for enemy in enemy_group:
                                if bullet.is_collision(enemy):
                                    if enemy.alive == True:
                                        bullet.goto(10000, 10000)
                                        enemy.health -= 5
                                        if enemy.health < 1:
                                            SCORE += 20
                                            enemy.width = 40
                                            enemy.height = 20
                                            enemy.y += 10
                                            enemy.alive = False
                                        elif PLAYER_SHEILD == 5:
                                            if bullet.is_collision(player):
                                                if player.alive == True:
                                                    bullet.goto(10000, 10000)
                                                    player.health -= 5
                                                    if player.health < 1:
                                                        SCORE += 20
                                                        player.width = 40
                                                        player.height = 20
                                                        player.y += 10
                                                        player.alive = False
        # Check for collisions
            # if pygame.sprite.spritecollide(player, [bullet], False):
                # if player.alive:
                #     player.health -= 10
                #     bullet.kill()
                # if player.health < 1:
                #     grenade_fx.play()
                #     player.width = 40
                #     player.height = 20
                #     player.y += 5
                #     player.alive = False
                #     game_over.game_over()
            for enemy in enemy_group:
                continue
                if pygame.sprite.spritecollide(enemy, [bullet], False):
                    if enemy.alive:
                        enemy.health -= 10
                        bullet.kill()
                    if enemy.health < 1:
                        grenade_fx.play()
                        enemy.width = 40
                        enemy.height = 20
                        enemy.y += 5
                        enemy.alive = False
                        
                if bullet.is_collision(block):
                    bullet.goto(10000, 10000)
                        
            if player.is_collision(block):
                # Player is to the left
                if player.x < block.x - block.width/2.0 and player.dx > 0:
                    player.dx = 0   
                    player.x = block.x - block.width/2.0 - player.width/2.0
                    player.stop_go_right = True
                # Player is to the right
                elif player.x > block.x + block.width/2.0 and player.dx < 0:
                    player.dx = 0
                    player.x = block.x + block.width/2.0 + player.width/2.0
                    player.stop_go_left = True
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

        # draw text on screen
        draw_text('AMMO:' + str(AMMO), font, WHITE, 5, 25)     
        draw_text('MONEY:' + str(SCORE), font, WHITE, 125, 5)
        draw_text('GRENADES:' + str(GRENADES), font, WHITE, 5, 40)
        draw_text('SHEILD:$50', font, WHITE, 240, 5)
        draw_text('ARMOR:$100', font, WHITE, 364, 5)
        draw_text('WEAPON:$200', font, WHITE, 487, 5)

        healthbar.draw(player.health)
        player.check_health()
        Soldier.idle = True
        
        if player.y > 800:
            return
            
        # Render objects
        # bullet.render(camera)
        
        #explosion.render(camera)
        # block.render(camera)
        g_render(RED, 0, 500, 10000, 30, camera)


        for enemy in enemy_group:
            enemy.render(camera)
            
        # Flip the display
        pygame.display.flip()

        # Set the FPS
        clock.tick(FPS)