import pygame
from create_platform import Platform
import OCF

config = OCF.open_conf_file()


def check_layer(x_block, y_count):
    if x_block <= y_count // 2:
        return pygame.image.load(config["IMAGES"]["sky"])
    return pygame.image.load(config["IMAGES"]["diamond_ore"])


def fill_map(x_count, y_count, surface_all):
    for x_block in range(y_count):
        image = check_layer(x_block, y_count)
        for y_block in range(x_count):
            platform = Platform(image, y_block * Platform.platform_height, x_block * Platform.platform_width)
            surface_all.add(platform)
