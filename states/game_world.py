
import pygame, os 
from states.state import State


class Game_world(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.genius = pygame.image.load(os.path.join(self.game.bilder_dir, "Map", "genius.jpg"))


        self.walls = [Wall(100, 100, 50, 200), Wall(300, 300, 200, 50)]

        self.spiller = Spiller(self.game, self.walls)


    def update(self, delta_time, actions):
        self.spiller.update(delta_time, actions)

    def render(self, display):
        display.blit(self.genius, (0, 0))
        self.spiller.render(display)


        for wall in self.walls:
            wall.render(display)

class Spiller():
    def __init__(self, game, walls):
        self.game = game
        self.walls = walls
        self.posisjon_x, self.posisjon_y = 200, 200  # Starting position
        self.size = 50  # Size of the square
        self.color = (0, 0, 255)  # Blue color
        self.rect = pygame.Rect(self.posisjon_x, self.posisjon_y, self.size, self.size)       
        
        """
        self.spiller_dir = os.path.join(self.game.sprite_dir, "actual_player")
        self.load_sprites()
        self.sprite_dir = game.spiller_dir
        self.posisjon_x, self.posisjon_y = 200, 200
        self.current_frame, self.last_frame_update = 0, 0
        self.curr_img = self.front_sprites[0]
        self.curr_anim_list = self.front_sprites
    
        self.rect = self.curr_img.get_rect(topleft=(self.posisjon_x, self.posisjon_y))
        """
        

    def update(self, delta_time, actions):

        prev_x, prev_y = self.posisjon_x, self.posisjon_y
        #leser av input
        retning_x = actions["right"] - actions["left"]
        retning_y = actions["down"] - actions["up"]
        #reagerer
        self.posisjon_x += 100 * delta_time * retning_x
        self.posisjon_y += 100 * delta_time * retning_y

        if self.check_collision():
            # Revert to previous position if there's a collision
            self.posisjon_x, self.posisjon_y = prev_x, prev_y
            self.rect.topleft = (self.posisjon_x, self.posisjon_y)

        #self.animer(delta_time, retning_x, retning_y)
        self.rect.topleft = (self.posisjon_x, self.posisjon_y)

    def render(self, display):
        #display.blit(self.curr_img, (self.posisjon_x, self.posisjon_y))
        pygame.draw.rect(display, self.color, self.rect)  # Draw a blue square    

    def animer(self, delta_time, retning_x, retning_y):
        #Sjekke når den sist oppdaterte animasjonen
        self.last_frame_update += delta_time

        #sette til idle om ingenting har skjedd
        if not (retning_x or retning_y):
            self.curr_anim_list = self.idle_sprites
            self.curr_img = self.idle_sprites[self.current_frame % len(self.idle_sprites)]
            return

        #Velger riktig bilder fra listene, egne lister for forskjellige retninger, valgfritt hvor mange animasjonsframes
        if retning_x:
            self.curr_anim_list = self.right_sprites if retning_x > 0 else self.left_sprites
        
        if retning_y:
            self.curr_anim_list = self.front_sprites if retning_y > 0 else self.back_sprites
        

        #gå på rundgang igjennom de forskjellige framesene
        if self.last_frame_update > 0.15:
            self.last_frame_update = 0
            self.current_frame = (self.current_frame + 1) % len(self.curr_anim_list)
            self.curr_img = self.curr_anim_list[self.current_frame]



    def check_collision(self):
        # Example: Check collision with screen boundaries
        if self.posisjon_x < 0 or self.posisjon_x + self.rect.width > self.game.GAME_W:
            return True
        if self.posisjon_y < 0 or self.posisjon_y + self.rect.height > self.game.GAME_H:
            return True

        # Example: Check collision with other objects (e.g., walls)
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                return True
        
        return False


"""
    def load_sprites(self):

        self.front_sprites, self.back_sprites, self.right_sprites, self.left_sprites = [],[],[],[]
        self.idle_sprites = []

        try : 
            walk_sheet = pygame.image.load(os.path.join(self.spiller_dir, "walk.png")).convert_alpha()
            idle_sheet = pygame.image.load(os.path.join(self.spiller_dir, "idle.png")).convert_alpha()
        except FileNotFoundError:
                print("Even test_image.png is missing—something is wrong with paths!")

        print(f"Loading walk sheet from: {walk_sheet}")
        print(f"Loading idle sheet from: {idle_sheet}")

        # Check if files exist
        if not os.path.exists(walk_sheet):
            print(f"Error: File not found - {walk_sheet}")
        if not os.path.exists(idle_sheet):
            print(f"Error: File not found - {idle_sheet}")

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
"""



class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def render(self, display):
        pygame.draw.rect(display, (255, 0, 0), self.rect)


































