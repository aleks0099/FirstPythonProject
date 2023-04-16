import pygame
import ev
import json

def start():

    pygame.init()
    screen = pygame.display.set_mode((ev.WIDTH, ev.HEIGHT))
    pygame.display.set_caption("Keyboard trainer")
    pygame.display.set_icon(pygame.image.load("src/keyboard.png"))
    black = (0, 0, 0)
    background = black
    screen.fill(background)
    flag = 0
    rec = ev.record();
    index = 0
    for j in range(len(rec)):
        if rec[j] == '{':
            index = j
            break
    heatmap = json.loads(rec[index:])
    heatmap = dict(sorted(heatmap.items(), key=lambda x: x[1], reverse =True))
    heatmap0 = heatmap.copy()
    rec = rec[:index].split();
    ev.prev_window(rec, heatmap, screen, background)
    begin_time = 0
    lines = 0
    time = 0
    mistakes = 0
    count = 0
    input_text = ""
    mainstr = ""
    error_message = ""
    i = 0
    with open('src/material.txt') as f:
        lines = f.readlines()

    while True:
        temp = ev.action(screen, background, flag, rec, lines, input_text, mainstr, i, time, count, mistakes, begin_time, error_message, heatmap, heatmap0)
        flag = temp[0]
        rec = temp[1]
        input_text = temp[2]
        mainstr = temp[3]
        i = temp[4]
        time = temp[5]
        count = temp[6]
        mistakes = temp[7]
        begin_time = temp[8]
        error_message = temp[9]
        heatmap = temp[10]
        heatmap0 = temp[11]
        pygame.display.flip()

start()