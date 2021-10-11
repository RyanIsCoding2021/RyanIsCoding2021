import sys
import pygame
from pygame.locals import *
import platformer

pygame.init()

WIDTH = 800
HEIGHT = int(WIDTH * 0.8)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Shooter')
pygame.display.set_icon(pygame.image.load("0.png"))

# load button images
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()

bg = (202, 228, 241)

# button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

# create button instances
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

run = True
draw_button = True
while run:

	screen.fill(bg)

	if draw_button == True: 
		if start_button.draw(screen):
			platformer.main()
		if exit_button.draw(screen):
			sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()