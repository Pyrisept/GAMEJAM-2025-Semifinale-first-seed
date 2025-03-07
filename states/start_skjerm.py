# Start skjerm for Rudmon spill.
import pygame, sys, os
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
assets_dir = os.path.join("assets")
font_dir = os.path.join(assets_dir, "font")

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rudmon")

try:
    BG = pygame.image.load(os.path.join("assets", "bilder", "Menu", "RUD.jpg"))
except pygame.error:
    print("Feil: Kunne ikke laste bakgrunnsbildet!")
    sys.exit()

def get_font(size):
    return pygame.font.Font(os.path.join(font_dir, "AGoblinAppears-o2aV.ttf"), size)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image if image else None
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) if self.image else self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        pygame.draw.rect(screen, "#FFFFFF", self.rect.inflate(20, 20), border_radius=10)
        if self.image:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        self.text = self.font.render(self.text_input, True, self.hovering_color if self.rect.collidepoint(position) else self.base_color)

class Menu:
    def __init__(self):
        self.running = True
    
    def main_menu(self):
        pygame.display.set_caption("Hovedmeny")
        while self.running:
            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = get_font(100).render("HOVEDMENY", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            buttons = [
                Button(None, (640, 250), "PLAY", get_font(75), "#EF0107", "Black"),
                Button(None, (640, 400), "OPTIONS", get_font(75), "#EF0107", "Black"),
                Button(None, (640, 550), "QUIT", get_font(75), "#EF0107", "Black")
            ]

            for button in buttons:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[0].checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if buttons[1].checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if buttons[2].checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            
            pygame.display.update()
    
    def play(self):
        pygame.display.set_caption("Play")
        while True:
            SCREEN.fill("black")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            PLAY_TEXT = get_font(45).render("Dette er Spill skjermen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(None, (640, 460), "TILBAKE", get_font(75), "White", "Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return

            pygame.display.update()
    
    def options(self):
        pygame.display.set_caption("Options")
        while True:
            SCREEN.fill("white")
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            OPTIONS_TEXT = get_font(45).render("Dette er Innstillinger.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(None, (640, 460), "TILBAKE", get_font(75), "Black", "Green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        return
            
            pygame.display.update()

if __name__ == "__main__":
    Menu().main_menu()