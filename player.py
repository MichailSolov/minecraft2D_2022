import pygame
import OCF


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.config = OCF.open_conf_file()
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = int(self.config["PLAYER"]["speed"])
        self.start_x = start_x
        self.start_y = start_y
        self.image = image
        self.rect = pygame.Rect(start_x,
                                start_y,
                                int(self.config["SIZES"]["player_width"]),
                                int(self.config["SIZES"]["player_height"]))
        self.on_ground = False

        self.left = False
        self.right = False

    def mov_right(self, ):
        self.rect.x += self.speed

    def mov_left(self):
        self.rect.x -= self.speed

    def update(self):
        if self.left:
            self.mov_left()
        if self.right:
            self.mov_right()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
