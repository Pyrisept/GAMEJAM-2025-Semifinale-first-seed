import pygame, random, os
from states.state import State

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400
FINISH_LINE = CANVAS_WIDTH - 100
NUM_POKEMON = 2
MIN_SPEED = 2
MAX_SPEED = 8

class PokemonRace(State):
    def __init__(self, game):
        super().__init__(game)
        
        self.game_canvas = pygame.Surface(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.screen = game.screen

        self.pokemon_images = [
            pygame.image.load(os.path.join(self.game.bilder_dir, "Pokemon_racer", "pikachu.jpg")).convert_alpha(),
            pygame.image.load(os.path.join(self.game.bilder_dir, "Pokemon_racer", "evil_pokemon.png")).convert_alpha()
        ]

        self.pokemon_rects = [
            self.pokemon_images[0].get_rect(topleft=(50, 100)),
            self.pokemon_images[1].get_rect(topleft=(50, 250))
        ]

        self.font = pygame.font.SysFont("Arial", 24)
        self.race()

    def race(self):
        winner = None
        for i, rect in enumerate(self.pokemon_rects):
            speed = random.randint(MIN_SPEED, MAX_SPEED)
            rect.x += speed  # Move the Pokémon

            if rect.x >= FINISH_LINE:
                winner = i
                break

        self.game_canvas.fill((255, 255, 255))

        pygame.draw.line(self.game_canvas, (255, 0, 0), (FINISH_LINE, 0), (FINISH_LINE, CANVAS_HEIGHT), 3)

        for i, (image, rect) in enumerate(zip(self.pokemon_images, self.pokemon_rects)):
            self.game_canvas.blit(image, rect)

        if winner is not None:
            pokemon_names = ["Pikachu", "Evil Pokémon"]
            self.display_winner(pokemon_names[winner])

        else:
            self.game.screen.blit(self.game_canvas, (0, 0))
            pygame.display.flip()
            pygame.time.delay(50)
            self.game.screen.fill((0, 0, 0))

            self.game.reset_keys()
            self.game.state_stack[-1].update(self.game.dt, self.game.actions)

            self.game.screen.blit(self.game_canvas, (0, 0))
            pygame.display.flip()
    
    def display_winner(self, winner_name):
        text_surface = self.font.render(f"{winner_name} Vant!", True, (0, 0, 255))
        self.game_canvas.blit(text_surface, (CANVAS_WIDTH // 2 - text_surface.get_width() // 2, CANVAS_HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()

        pygame.time.delay(2000)