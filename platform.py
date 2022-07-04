import pygame
import OCF


class Platform(pygame.sprite.Sprite):
    config = OCF.open_conf_file()
    platform_height = int(config["SIZES"]["platform_height"])
    platform_width = int(config["SIZES"]["platform_width"])

    def __init__(self, image, x_pos, y_pos, transparency=255):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.transparency = self.image.set_alpha(transparency)
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.platform_width, self.platform_height)
