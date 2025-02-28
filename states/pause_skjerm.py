import pygame

# Initialize Pygame
pygame.init()

# Load the uploaded pixel font
font_path = "AGoblinAppears-o2aV.ttf"  # Ensure this font is in your script's folder
font_size = 16  # Adjust to match original image style
font = pygame.font.Font(font_path, font_size)

# Create the menu surface
width, height = 100, 158
menu_surface = pygame.Surface((width, height))
menu_surface.fill((255, 255, 255))  # White background

# Draw black border
pygame.draw.rect(menu_surface, (0, 0, 0), (0, 0, width, height), 3)

# Menu title
title_text = font.render("MENU", True, (0, 0, 0))
menu_surface.blit(title_text, (width // 2 - title_text.get_width() // 2, 5))

# Menu options
options = ["Party", "Items", "Dex", "Exit"]
y_offset = 30

for option in options:
    text_surface = font.render(option, True, (0, 0, 0))
    menu_surface.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y_offset))
    y_offset += 30  # Space between options

# Save the updated menu image
pygame.image.save(menu_surface, "menu_pixel_font.png")

print("Pixel-style menu saved as 'menu_pixel_font.png'")
pygame.quit()
