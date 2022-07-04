import pygame
import OCF


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.config = OCF.open_conf_file()
        self.velocity_x = 0
        self.velocity_y = 0
        self.start_x = start_x
        self.start_y = start_y
        self.image = image
        self.rect = pygame.Rect(start_x,
                                start_y,
                                int(self.config["SIZES"]["player_width"]),
                                int(self.config["SIZES"]["player_height"]))
        self.on_ground = False
