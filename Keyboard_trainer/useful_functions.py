import pygame
import random
import sys
import json
import random
import magic_constants

def record():
    with open ('src/record.txt') as f:
        return f.readline()

def save(a, b, c, k, rec):
    with open ('src/record.txt', 'w') as f:
        a += int(rec[0])
        b += int(rec[1])
        c += int(rec[2])
        f.seek(0)
        f.write(str(a) + " " + str(b) + " " + str(c) + " " + json.dumps(k))

def annul(self):
    self.input_text = ""
    self.mistakes = 0
    self.begin_time = 0
    self.count = 0
    self.mainstr = ""
    self.time = 0
    self.symbol_number_in_str = 0
    self.error_message = ""
    self.heatmap = json.loads(self.rec[self.index:])
    self.heatmap = dict(sorted(self.heatmap.items(), key=lambda x: x[1], reverse =True))
    self.rec = self.rec[:self.index].split();
    self.heatmap0 = self.heatmap.copy()