import pygame
import sys
import platformer
from pygame.locals import *

pygame.init()


WIDTH = 800
HEIGHT = int(WIDTH * 0.8)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Shooter')

font = pygame.font.SysFont('Constantia', 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# define colors
bg = (25, 126, 23)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# define global variable
clicked = False
counter = 0

class button():
	# colors for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		# get mouse position
		pos = pygame.mouse.get_pos()

		# create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		# check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		# add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		# add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


again = button(100, 250, 'Start Game')
controls = button(297, 250, 'Controls')
quit = button(490, 250, 'Quit Game')

run = True
while run:

	screen.fill(bg)

	if again.draw_button():
  		platformer.main()
	if controls.draw_button():
		again.delete()
		controls.delete()
		quit.delete()
		# # draw text on screen
        # draw_text('AMMO: ', font, black, 5, 25)     
        # draw_text('MONEY: ', font, black, 125, 5)
        # draw_text('GRENADES: ', font, black, 5, 40)
        # draw_text('SHEILD: $', font, black, 223, 5)
        # draw_text('ARMOR: $', font, black, 323, 5)
        # draw_text('WEAPON: $', font, black, 435, 5)
	if quit.draw_button():
		sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
				


	pygame.display.update()

pygame.quit()