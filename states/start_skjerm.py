# Start skjerm for Rudmon spill.
#start_skjerm.py

import pygame, os
from states.state import State  
from states.game_world import Game_world

class StartSkjerm(State):
    def __init__(self, game):
        super().__init__(game)
        print("StartScreen initialized")
        self.bg = pygame.image.load(os.path.join(self.game.assets_dir, "bilder", "Menu", "RUD.jpg"))

        # Load font
        self.font = pygame.font.Font(os.path.join(self.game.font_dir, "AGoblinAppears-o2aV.ttf"), 50)

        # Create menu buttons
        self.buttons = [
            Button("START", (self.game.SCREEN_WIDTH // 2, 300), self.font, (255, 255, 255), (200, 200, 200)),
            Button("QUIT", (self.game.SCREEN_WIDTH // 2, 400), self.font, (255, 255, 255), (200, 200, 200))
        ]

    def update(self, delta_time, actions):
        """Skal håndtere keys og handlinger"""
        if actions["start"]:  
            new_state = Game_world(self.game)  # Gå til game_world
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        """Tegenr startskjermen"""
        print("Rendering tid. og han rendereret overalt. Morgz mum")
        
        self.game.game_canvas.fill((0, 0, 255))
        print("Game canvas filled with blue")

        title_text = self.font.render("RUDMON", True, (255, 215, 0))
        display.blit(title_text, (self.game.SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        print("Title text rendered")
       
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.change_color(mouse_pos)
            button.update(display)
        print("Buttons rendered")

class Button:
    def __init__(self, text, pos, font, base_color, hover_color):
        self.text = text
        self.pos = pos
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_render = self.font.render(self.text, True, self.base_color)
        self.rect = self.text_render.get_rect(center=self.pos)

    def update(self, screen):
        """Mus"""
        pygame.draw.rect(screen, (50, 50, 50), self.rect.inflate(20, 10), border_radius=5)  
        screen.blit(self.text_render, self.rect)

    def check_for_input(self, pos):
        """Sjekker input fra mus"""
        return self.rect.collidepoint(pos)

    def change_color(self, pos):
        """For å vise hover"""
        if self.rect.collidepoint(pos):
            self.text_render = self.font.render(self.text, True, self.hover_color)
        else:
            self.text_render = self.font.render(self.text, True, self.base_color)


