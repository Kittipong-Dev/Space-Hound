import pygame
import os

BASE_IMG_PATH = 'data/images/'

def load_image(path, mtype=""):
    if mtype == "a":
        img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    elif mtype == "":
        img = pygame.image.load(BASE_IMG_PATH + path).convert()
    elif mtype == "k":
        img = pygame.image.load(BASE_IMG_PATH + path).convert()
        img.set_colorkey((0, 0, 0))
    return img

def load_images(path, mtype=""):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + "/" + img_name, mtype))
    return images
        
def transform_images(images, size):
    images_list = []
    for image in images:
        images_list.append(pygame.transform.scale(image, size))
    return images_list

