#GAMES 
#spill.py
import os
import time
import pygame

from states.start_skjerm import StartSkjerm
from states.state import State


class Spill():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
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
        self.spiller_dir = os.path.join(self.sprite_dir, "spiller")
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

 

if __name__ == "__main__":
    g = Spill()
    while g.running:
        print("Main loop running")
        g.game_loop()


