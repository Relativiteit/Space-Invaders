import pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = 100
        self.block_y = 100
        pass

    def draw(self,surface):
        surface.fill((60, 209, 197))
        surface.blit(block, (block_x, block_y))
        pygame.display.flip()
        surface.parent_screen.blit(self.block,(self.block_x, self.block_y)) 


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((60, 209, 197))
        self.snake = Snake(self.surface)
        self.snake.draw()

        pass

    def run(self):
        
        pass

def draw_block():
    surface.fill((60, 209, 197))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()

   
   pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    pass

            elif event.type == QUIT:
                running = False

