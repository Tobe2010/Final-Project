import pygame
import pymunk
import sqlite3

class Ball():
    def __init__(self, x, color):
        self.color = color
        self.body = pymunk.Body()
        self.body.postition = x, 400