import pygame
import sys

# Window dimensions
WIDTH = 500
HEIGHT = 500

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Buttons in pygame')
clock = pygame.time.Clock()

class Button:
	def __init__(self, width, height, x, y, color, hover_color, text, text_size, text_color):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.color = color
		self.hover_color = hover_color
		self.text = text
		self.text_size = text_size
		
                # Set up the text that will be on top of the button
		self.font = pygame.font.SysFont(None, text_size)
		self.screen_text = self.font.render(text, True, text_color)
		self.text_rect = self.screen_text.get_rect()
		self.text_rect.center = (x+self.width/2, y+self.height/2)

                # Draw the button and draw the text on the button
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
		screen.blit(self.screen_text, self.text_rect)
		
        
	def action(self, action = None):
		# Get the mouse position and the button pressed
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
                # Check if the mouse is inside the button
		if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
			pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
			screen.blit(self.screen_text, self.text_rect)
			
                        # Check if left mouse button is clicked
			if click[0] == 1:
				action()

def game_quit():
	pygame.quit()
	sys.exit()

while True:
        # Check for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_quit()
		
	screen.fill((0, 0, 0))

        #  Button(width, height, x, y, color, hover_color, text, text_size, text_color)
	b1 = Button(100, 60, WIDTH/2, HEIGHT/2, GREEN, BLUE, 'QUIT', 50,  RED)
	b1.action(game_quit)

	pygame.display.update()
	clock.tick(60)