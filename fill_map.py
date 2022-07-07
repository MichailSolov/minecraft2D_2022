import pygame
from platform import Platform
import OCF

config = OCF.open_conf_file()
objects = {"sky": [],
           "diamond_ore": [],
           "dirt": []}


def check_layer(x_block, y_count):
    if x_block < y_count // 2:
        return "sky", pygame.image.load(config["IMAGES"]["sky"])
    if x_block == y_count // 2:
        return "dirt", pygame.image.load(config["IMAGES"]["dirt"])
    return "diamond_ore", pygame.image.load(config["IMAGES"]["diamond_ore"])


def fill_map(x_count, y_count, surface_all):
    for x_block in range(y_count):
        for y_block in range(x_count):
            block_type, image = check_layer(x_block, y_count)
            platform = Platform(image, y_block * Platform.platform_height, x_block * Platform.platform_width)
            surface_all.add(platform)
