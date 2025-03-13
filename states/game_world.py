import pygame, os 
from states.state import State
from states.pause_skjerm import PauseMenu


class Game_world(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.genius = pygame.image.load(os.path.join(self.game.bilder_dir, "Map", "genius.jpg"))
        self.spiller = Spiller(self.game)

    def update(self, delta_time, actions):
        if actions["start"]:
            ny_state = PauseMenu(self.game)
            ny_state.enter_states()
        self.spiller.update(delta_time, actions)

    def render(self, display):
        display.blit(self.genius, (0, 0))
        self.spiller.render(display)

class Spiller():
    def __init__(self, game):
        self.game = game
        self.sprite_dir = os.path.join(self.game.assets_dir, "sprites", "character.png")
        self.load_sprites()
        self.posisjon_x, self.posisjon_y = 200, 200
        self.current_frame, self.last_frame_update = 0, 0
        self.curr_img = self.front_sprites[0]
        self.curr_anim_list = self.front_sprites

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
        self.idle_sprites = []

        walk_sheet = pygame.image.load(self.sprite_dir, "walk.png").convert_alpha()
        idle_sheet = pygame.image.load(self.sprite_dir, "idle.png").convert_alpha()

        walk_frame_width = walk_sheet.get_width() // 5
        walk_frame_height = walk_sheet.get_height() // 4

        idle_frame_width = idle_sheet.get_width() // 2
        idle_frame_height = idle_sheet.get_height // 4

        def get_sprite(sheet, x, y, width, height):
             return sheet.subsurface(pygame.Rect(x * width, y * height, width, height))

        for i in range(5):
            self.front_sprites.append(get_sprite(walk_sheet, i, 0, walk_frame_width, walk_frame_height))  # Row 0 = Front
            self.back_sprites.append(get_sprite(walk_sheet, i, 3, walk_frame_width, walk_frame_height))   # Row 3 = Back
            self.right_sprites.append(get_sprite(walk_sheet, i, 2, walk_frame_width, walk_frame_height))  # Row 2 = Right
            self.left_sprites.append(get_sprite(walk_sheet, i, 1, walk_frame_width, walk_frame_height))   # Row 1 = Left
        
        for i in range(2):
            self.idle_sprites.append(get_sprite(idle_sheet, i, 0, idle_frame_width, idle_frame_height))

        self.curr_img = self.idle_sprites[0]
        self.curr_anim_list = self.idle_sprites
