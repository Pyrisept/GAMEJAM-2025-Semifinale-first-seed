#GAMES 
#spill.py
import os
import time
import pygame

from states.start_skjerm import StartSkjerm
from states.Horse import PokemonRace
from states.state import State


class Spill():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False, "mouse_click" : False}
        self.dt, self.prev_time = 0, time.time()
        self.state_stack = []
        self.load_assets()
        self.load_states()


    def game_loop(self):
        while self.playing:
            #print("Funny fun not fun time time fun")
            self.get_dt()
            self.get_events()
            self.update()
            self.render()


    def get_events(self):

        for event in pygame.event.get():
            #print(f"Event detected: {event}")
            if event.type == pygame.QUIT:
                print("QUIT event detected")
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("SHAKING SCREEN! 💥")
                    self.shake_screen()
                
                if event.key == pygame.K_l:
                    print("JELLY MODE ACTIVATED! 🍮")
                    self.bouncy_screen()

            
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE key detected")
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['action1'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True    
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True  

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False 
            if event.type == pygame.MOUSEBUTTONDOWN:  # Capture mouse clicks
                if event.button == 1:  # Left mouse button
                    self.actions["mouse_click"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions["mouse_click"] = False


    def update(self):
        if self.state_stack:
            self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)

        #print("Jeg skulle ønske noen kunne rendere... Den ydmyke renderfunskjon")
        #print(f"Current state: {type(self.state_stack[-1])}")
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()



    def get_dt(self):
        nå = time.time()
        self.dt = nå - self.prev_time
        self.prev_time = nå

    def render_tekst(self, surface, text, colour, x, y):
        tekst_surface = self.font.render(text, True, colour)
        tekst_rect = tekst_surface.get_rect()   
        tekst_rect.center = (x,y)
        surface.blit(tekst_surface, tekst_rect)


    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.spiller_dir = os.path.join(self.sprite_dir, "actual_player")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.bilder_dir = os.path.join(self.assets_dir, "bilder")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "AGoblinAppears-o2aV.ttf"), 20)

    def load_states(self):
        print("Så sa han det er lastetid og lastet overalt...")
        self.title_screen = StartSkjerm(self)
        self.state_stack.append(self.title_screen)
        print(f"State stack: {self.state_stack}")


    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def shake_screen(self, intensity=10, duration=0.5):
        """Shakes the screen for dramatic effect!"""
        import random
        start_time = time.time()

        while time.time() - start_time < duration:
            offset_x = random.randint(-intensity, intensity)
            offset_y = random.randint(-intensity, intensity)
            self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (offset_x, offset_y))
            pygame.display.flip()
            pygame.time.delay(50)  # Small delay for effect

        print("Screen shake over!")  # Funny debug message



    def bouncy_screen(self, intensity=1.2, duration=0.5):
        """Makes the screen stretch and squish like jelly!"""
        import random

        start_time = time.time()
        original_size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        while time.time() - start_time < duration:
            # Randomly stretch the screen size
            scale_x = random.uniform(1.0, intensity)
            scale_y = random.uniform(1.0, intensity)

            new_width = int(original_size[0] * scale_x)
            new_height = int(original_size[1] * scale_y)

            squished_screen = pygame.transform.scale(self.game_canvas, (new_width, new_height))
            self.screen.blit(squished_screen, ((self.SCREEN_WIDTH - new_width) // 2, (self.SCREEN_HEIGHT - new_height) // 2))

            pygame.display.flip()
            pygame.time.delay(50)  # Delay for effect

        # Reset screen back to normal
        self.screen.blit(pygame.transform.scale(self.game_canvas, original_size), (0, 0))
        pygame.display.flip()
        
        print("Bouncy screen over! 🍮😂")  # Funny debug message


    
    def chaos_mode(self, intensity=1.5, duration=2.0):  
        """The most unnecessary, dumb, chaotic screen effect ever made."""
        import random

        start_time = time.time()
        original_size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        # Load a funny sound (you need to add a "boing.wav" sound in assets)
        boing_path = os.path.join(self.assets_dir, "boing.wav")
        if os.path.exists(boing_path):
            pygame.mixer.Sound(boing_path).play()
        
        while time.time() - start_time < duration:
            # Generate random scale, rotation, and colors
            scale_x = random.uniform(0.8, intensity)
            scale_y = random.uniform(0.8, intensity)
            new_width = int(original_size[0] * scale_x)
            new_height = int(original_size[1] * scale_y)

            angle = random.randint(-10, 10)  # Slight random rotation
            color_overlay = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Transform the screen
            temp_screen = pygame.transform.scale(self.game_canvas, (new_width, new_height))
            temp_screen = pygame.transform.rotate(temp_screen, angle)

            self.screen.fill(color_overlay)  # Flash colors like a rave
            self.screen.blit(temp_screen, ((self.SCREEN_WIDTH - new_width) // 2, (self.SCREEN_HEIGHT - new_height) // 2))

            pygame.display.flip()
            pygame.time.delay(50)  # Delay for effect

        # Reset back to normal
        self.screen.blit(pygame.transform.scale(self.game_canvas, original_size), (0, 0))
        pygame.display.flip()
        
        print("CHAOS MODE OVER! 🤡💥")  # Stupid debug message









if __name__ == "__main__":
    g = Spill()
    while g.running:
        print("Main loop running")
        g.game_loop()


