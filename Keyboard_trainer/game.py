import pygame
import events
import magic_constants
import json
from useful_functions import record
from drawers import draws_heatmap_and_whole_statistics

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((magic_constants.WIDTH, magic_constants.HEIGHT))
        pygame.display.set_caption("Keyboard trainer")
        pygame.display.set_icon(pygame.image.load("src/keyboard.png"))
        self.background = (0, 0, 0)
        self.screen.fill(self.background)
        self.flag = 0
        self.index = 0
        self.rec = []
        self.heatmap = []
        self.heatmap0 = []
        self.begin_time = 0
        self.lines = 0
        self.time = 0
        self.mistakes = 0
        self.count = 0
        self.input_text = ""
        self.mainstr = ""
        self.error_message = ""
        self.symbol_number_in_str = 0
    
    def start(self):
        self.rec = record();
        for j in range(len(self.rec)):
            if self.rec[j] == '{':
                self.index = j
                break
        self.heatmap = json.loads(self.rec[self.index:])
        self.heatmap = dict(sorted(self.heatmap.items(), key=lambda x: x[1], reverse =True))
        self.heatmap0 = self.heatmap.copy()
        self.rec = self.rec[:self.index].split();
        draws_heatmap_and_whole_statistics(self)
        with open('src/material.txt') as f:
            self.lines = f.readlines()
        while True:
            events.action(self)
            pygame.display.flip()

game = Game()
game.start()