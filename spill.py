#GAMES 

import os
import time
import pygame


class Spill():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []


    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()


    def get_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        pass

    def render(self):
        self.screen.blit(pygame.transfrom.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
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
        self.sprite = os.path.join(self.assets_dir, "sprites")
        self.font = os.path.join(self.font_dir, "AGoblinAppears-o2aV.ttf")


 



