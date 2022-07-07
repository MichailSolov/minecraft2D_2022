import pygame
import fill_map
from player import Player
import OCF


class GameStart:
    surface_all = pygame.sprite.Group()
    player_all = pygame.sprite.Group()

    def __init__(self):
        self.config = OCF.open_conf_file()
        self.FPS = int(self.config["GAME"]["FPS"])
        self.WIDTH = int(self.config["SCREEN"]["width"]) * 0.5
        self.HEIGHT = int(self.config["SCREEN"]["height"]) * 0.5
        self.mainloop = self.config["GAME"]["mainloop"]


def main():
    pygame.init()
    game = GameStart()
    screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
    pygame.display.set_caption("test")
    clock = pygame.time.Clock()
    fill_map.fill_map(int(game.WIDTH // 40),
                      int(game.HEIGHT // 40),
                      game.surface_all)

    player = Player(1, 1, pygame.image.load(game.config["IMAGES"]["player"]))
    game.player_all.add(player)

    while game.mainloop:
        clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.mainloop = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                player.left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                player.right = True

            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                player.left = False
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                player.right = False

        for obj in game.surface_all:
            screen.blit(obj.image, (obj.rect.x, obj.rect.y))
        for obj in game.player_all:
            screen.blit(obj.image, (obj.rect.x, obj.rect.y))

        player.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
