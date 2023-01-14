import numpy as np
import pygame
# Initialize pygame
pygame.init()
# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# Set title
pygame.display.set_caption("Gnome Coin Collector")
# Load gnome and coin images
gnome_image = pygame.image.load("gnome.png")
coin_image = pygame.image.load("coin.png")
# Set gnome starting position
gnome_x = 50
gnome_y = 50
# Set coin starting position
coin_x = 400
coin_y = 300
# Set coin collected variable
coin_collected = 0
# Initialize font for displaying score
font = pygame.font.Font(None, 30)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Move gnome based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gnome_x -= 5
    if keys[pygame.K_RIGHT]:
        gnome_x += 5
    if keys[pygame.K_UP]:
        gnome_y -= 5
    if keys[pygame.K_DOWN]:
        gnome_y += 5
    # Check if gnome has collected coin
    if gnome_x < coin_x + 50 and gnome_x > coin_x - 50:
        if gnome_y < coin_y + 50 and gnome_y > coin_y - 50:
            coin_collected += 1
            coin_x = np.random.randint(0, screen_width-50)
            coin_y = np.random.randint(0, screen_height-50)
    # Clear screen
    screen.fill((255, 255, 255))
    # Draw gnome and coin
    screen.blit(gnome_image, (gnome_x, gnome_y))
    screen.blit(coin_image, (coin_x, coin_y))
    # Draw score
    score_text = font.render("Coins collected: " + str(coin_collected), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    # Update display
    pygame.display.update()
# Quit pygame
pygame.quit()









