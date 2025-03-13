#game_world.py

import pygame, os 
from states.state import State


class Game_world(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.genius = pygame.load(os.path.join(self.game.bilder_dir, "Map", "genius.jpg"))
        self.spiller = Spiller(self.game)

    def update(self, delta_time, actions):
        self.spiller.update(delta_time, actions)

    def render(self, display):
        display.blit(self.genius, (0, 0))
        self.spiller.render(display)

class Spiller():
    def __init__(self, game):
        self.game = game
        self.load_sprites()
        self.sprite_dir = game.spiller_dir
        self.posisjon_x, self.posisjon_y = 200, 200
        self.current_frame, self.last_frame_update = 0, 0


    def update(self, delta_time, actions):
        #leser av input
        retning_x = actions["right"] - actions["left"]
        retning_y = actions["down"] - actions["up"]
        #reagerer
        self.posisjon_x += 100 * delta_time * retning_x
        self.posisjon_y += 100 * delta_time * retning_y

        self.animer(delta_time, retning_x, retning_y)

    def render(self, display):
        display.blit(self.curr_img, (self.posisjon_x, self.posisjon_y))

    def animer(self, delta_time, retning_x, retning_y):
        #Sjekke når den sist oppdaterte animasjonen
        self.last_frame_update += delta_time

        #sette til idle om ingenting har skjedd
        if not (retning_x or retning_y):
            self.curr_img = self.curr_anim_list[0]
            return

        #Velger riktig bilder fra listene, egne lister for forskjellige retninger, valgfritt hvor mange animasjonsframes
        if retning_x:
            if retning_x > 0: self.curr_anim_list = self.right_sprites
            else:
                self.curr_anim_list = self.left_sprites
            
        if retning_y:
            if retning_y > 0: self.curr_anim_list = self.front_sprites
            else:
                self.curr_anim_list = self.back_sprites
        

        #gå på rundgang igjennom de forskjellige framesene
        if self.last_frame_update > 0.15:
            self.last_frame_update = 0
            self.current_frame = (self.current_frame + 1) % len(self.curr_anim_list)
            self.curr_img = self.curr_anim_list[self.current_frame]

    def load_sprites(self):
        
        self.front_sprites, self.back_sprites, self.right_sprites, self.left_sprites = [],[],[],[]

        for i in range(1, 5):
            try:
                self.front_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "spiller_front" + str(i) + ".png")))
                self.back_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "spiller_back" + str(i) + ".png")))
                self.right_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "spiller_right" + str(i) + ".png")))
                self.left_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "spiller_left" + str(i) + ".png")))
            except FileNotFoundError:
                print(f"Har ikke bilde for spiller_{i}.png")
        

        self.curr_img = self.front_sprites[0] if self.front_sprites else None
        self.curr_anim_list = self.front_sprites







