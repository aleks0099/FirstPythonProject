import pygame
import random
import time
import sys
import os
import json
import random

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

def prev_window(rec, heatmap, screen, background):
        screen.fill(background)
        font1 = pygame.font.SysFont('arial', 60)
        text1 = font1.render("Press Enter to start gamemode 1", 1, (255, 255, 255))
        text55 = font1.render("Press Tab to start gamemode 2", 1, (255, 255, 255))
        text11 = font1.render("Press Space to invalidate statistics", 1, (155, 205, 150))
        font2 = pygame.font.SysFont('arial', 25)
        text2 = font2.render("Symbols per sec: " + "0", 1, (255, 255, 255))
        if int(rec[0])/1000 != 0:
            text2 = font2.render("Symbols per sec: " + str(round(int(rec[1])/(int(rec[0])/1000), 3)), 1, (255, 255, 255))
        text3 = font2.render("Total symbols: " + rec[1], 1, (255, 255, 255))
        text4 = font2.render("Mistakes: " + rec[2], 1, (255, 255, 255))
        place = text1.get_rect(center=(WIDTH/2, HEIGHT/3))     
        screen.blit(text1, place)
        place = text55.get_rect(center=(WIDTH/2, HEIGHT/2))     
        screen.blit(text55, place)
        place = text11.get_rect(center=(WIDTH/2, HEIGHT/6))
        screen.blit(text11, place)
        place = text2.get_rect(center=(110, 15))     
        screen.blit(text2, place)
        place = text3.get_rect(center=(WIDTH/2, 15))     
        screen.blit(text3, place)
        place = text4.get_rect(center=(WIDTH - 90, 15))     
        screen.blit(text4, place)
        img = pygame.image.load('src/keyboard.png')
        rct = img.get_rect()
        rct.centerx = screen.get_rect().centerx
        rct.bottom = screen.get_rect().bottom - 160
        screen.blit(img, rct)
        index = 0
        arr = []
        for item in heatmap.items():
            if item[0] == ' ':
                arr.append(['Space', item[1]])
            else:
                arr.append(item)
            index += 1
            if index == 5:
                break
        font = pygame.font.SysFont('arial', 25)
        text = font.render("Top mistakes:", 1, (30,144,255))
        place = text.get_rect(center=(WIDTH/7, rct.top))
        screen.blit(text, place)
        k = 0
        key_brd0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
        key_brd1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        key_brd2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        key_brd3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
        for i in arr:
            k += 1
            text = font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, (30,144,255))
            if i[1] == 1:
                text = font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, (30,144,255))
            rect = text.get_rect()
            rect.left = 50
            rect.bottom = rct.top + 55*k
            screen.blit(text, rect)
            h = 25
            if i[0].lower() in key_brd0:
                ind = key_brd0.index(i[0].lower())
                Red = (255, 0, 0)
                pygame.draw.circle(screen, Red, (rct.left + 36 + 25*ind, rct.top + h + 0*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 
            if i[0].lower() in key_brd1:
                ind = key_brd1.index(i[0].lower())
                Red = (255, 0, 0)
                pygame.draw.circle(screen, Red, (rct.left + 47 + 25*ind, rct.top + h + 1*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
                if i[0].isupper() and i[0].isalpha():
                    pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i[0].lower() in key_brd2:
                ind = key_brd2.index(i[0].lower())
                Red = (255, 0, 0)
                pygame.draw.circle(screen, Red, (rct.left + 58 + 25*ind, rct.top + h + 2*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
                if i[0].isupper() and i[0].isalpha():
                    pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i[0].lower() in key_brd3:
                ind = key_brd3.index(i[0].lower())
                Red = (255, 0, 0)
                pygame.draw.circle(screen, Red, (rct.left + 69 + 25*ind, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
                if i[0].isupper() and i[0].isalpha():
                    pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i[0] == 'Space':
                Red = (255, 0, 0)
                pygame.draw.circle(screen, Red, (rct.left + 175, rct.top + h + 4*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 

def key_board_drawer(screen, arr, rct):
    k = 0
    key_brd0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
    key_brd1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    key_brd2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    key_brd3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
    for i in arr:
        k += 1
        h = 25
        if i.lower() in key_brd0:
            ind = key_brd0.index(i.lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 36 + 25*ind, rct.top + h + 0*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 
            pygame.display.update()
        if i.lower() in key_brd1:
            ind = key_brd1.index(i.lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 47 + 25*ind, rct.top + h + 1*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i.isupper() and i.isalpha():
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            pygame.display.update()
        if i.lower() in key_brd2:
            ind = key_brd2.index(i.lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 58 + 25*ind, rct.top + h + 2*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i.isupper() and i.isalpha():
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            pygame.display.update()
        if i.lower() in key_brd3:
            ind = key_brd3.index(i.lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 69 + 25*ind, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if i.isupper() and i.isalpha():
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            pygame.display.update()
        if i == 'Space':
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 175, rct.top + h + 4*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 
            pygame.display.update()

def game1_window(background, time, screen, input_text, error_message, mainstr, mistakes, begin_time, count):
    screen.fill(background)
    font2 = pygame.font.SysFont('arial', 25)
    time = pygame.time.get_ticks()
    text2 = font2.render("Time: " + str(round((time-begin_time)/1000, 3)), 1, (255, 255, 255))
    text3 = font2.render("Total symbols: " + str(count), 1, (255, 255, 255))
    text4 = font2.render("Mistakes: " + str(mistakes), 1, (255, 255, 255))
    place = text2.get_rect(center=(90, 15))     
    screen.blit(text2, (45, 0))
    place = text3.get_rect(center=(WIDTH/2, 15))     
    screen.blit(text3, place)
    place = text4.get_rect(center=(WIDTH - 90, 15))     
    screen.blit(text4, place)
    font = pygame.font.SysFont('arial', 25)
    text = font.render(mainstr, 1, (255, 255, 255))
    place = text.get_rect(center=(WIDTH/2, HEIGHT/3))     
    screen.blit(text, place)
    input_rect = pygame.Rect(250, HEIGHT/2, 500, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
    text_surface = font.render(str(input_text), 1, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))
    text5 = font.render(mainstr, 1, (255, 255, 255))
    place = text5.get_rect(center=(WIDTH/2, HEIGHT/3))     
    screen.blit(text5, place)
    text = font.render(error_message, 1, (255, 0, 0))
    place = text.get_rect(center=(WIDTH/2, HEIGHT/6))     
    screen.blit(text, place)
    font22 = pygame.font.SysFont('arial', 40)
    text22 = font22.render("Press ESC to exit", 1, (255, 255, 255))
    place = text22.get_rect(center=(WIDTH/2, HEIGHT - 100))     
    screen.blit(text22, place)

def game2_window(background, time, screen, error_message, mainstr, mistakes, begin_time, count):
    screen.fill(background)
    font2 = pygame.font.SysFont('arial', 25)
    time = pygame.time.get_ticks()
    text2 = font2.render("Time: " + str(round(60-(time-begin_time)/1000, 3)), 1, (255, 255, 255))
    text3 = font2.render("Total symbols: " + str(count), 1, (255, 255, 255))
    text4 = font2.render("Mistakes: " + str(mistakes), 1, (255, 255, 255))
    place = text2.get_rect(center=(90, 15))     
    screen.blit(text2, (45, 0))
    place = text3.get_rect(center=(WIDTH/2, 15))     
    screen.blit(text3, place)
    place = text4.get_rect(center=(WIDTH - 90, 15))     
    screen.blit(text4, place)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = screen.get_rect().centerx
    rct.bottom = screen.get_rect().bottom - 400
    screen.blit(img, rct)
    font = pygame.font.SysFont('arial', 60)
    text = font.render(error_message, 1, (255, 0, 0))
    place = text.get_rect(center=(WIDTH/2, HEIGHT/6))     
    screen.blit(text, place)
    arr = [mainstr]
    key_board_drawer(screen, arr, rct)

def game2_end_window(background, time, screen, mistakes, count, heatmap, heatmap0):
    screen.fill(background)
    font1 = pygame.font.SysFont('arial', 60)
    text1 = font1.render("Your session statistics", 1, (255, 255, 255))
    place = text1.get_rect(center=(WIDTH/2, HEIGHT/3))     
    screen.blit(text1, place)
    font22 = pygame.font.SysFont('arial', 40)
    text22 = font22.render("Press ESC to exit", 1, (255, 255, 255))
    place = text22.get_rect(center=(WIDTH/2, HEIGHT - 60))     
    screen.blit(text22, place)
    font2 = pygame.font.SysFont('arial', 25)
    text2 = font2.render("Symbols per sec: " + "0", 1, (255, 255, 255))
    if int(time)/1000 != 0:
        text2 = font2.render("Symbols per sec: " + str(round(int(count)/(int(time)/1000), 3)), 1, (255, 255, 255))
    text3 = font2.render("Total symbols: " + str(count), 1, (255, 255, 255))
    text4 = font2.render("Mistakes: " + str(mistakes), 1, (255, 255, 255))
    place = text2.get_rect(center=(110, 15))     
    screen.blit(text2, place)
    place = text3.get_rect(center=(WIDTH/2, 15))     
    screen.blit(text3, place)
    place = text4.get_rect(center=(WIDTH - 90, 15))     
    screen.blit(text4, place)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = screen.get_rect().centerx
    rct.bottom = screen.get_rect().bottom - 160
    screen.blit(img, rct)
    arr = []
    for item in heatmap.items():
        x = 0
        if item[0] in heatmap0.keys():
            x = heatmap0[item[0]]
        if item[1] - x != 0:
            if item[0] == ' ':
                arr.append(('Space', item[1] - x))
            else:
                arr.append((item[0], item[1] - x))
    arr = sorted(arr, key=lambda x: x[1], reverse=True)
    arr = arr[:5]
    font = pygame.font.SysFont('arial', 25)
    text = font.render("Top mistakes:", 1, (30,144,255))
    place = text.get_rect(center=(WIDTH/7, rct.top))
    screen.blit(text, place)
    k = 0
    key_brd0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
    key_brd1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    key_brd2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    key_brd3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
    for i in arr:
        k += 1
        text = font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, (30,144,255))
        if i[1] == 1:
            text = font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, (30,144,255))
        rect = text.get_rect()
        rect.left = 50
        rect.bottom = rct.top + 55*k
        screen.blit(text, rect)
        h = 25
        if i[0].lower() in key_brd0:
            ind = key_brd0.index(i[0].lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 36 + 25*ind, rct.top + h + 0*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 
        if i[0].lower() in key_brd1:
            ind = key_brd1.index(i[0].lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 47 + 25*ind, rct.top + h + 1*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if (i[0] == i[0].upper()):
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
        if i[0].lower() in key_brd2:
            ind = key_brd2.index(i[0].lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 58 + 25*ind, rct.top + h + 2*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if (i[0] == i[0].upper()):
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
        if i[0].lower() in key_brd3:
            ind = key_brd3.index(i[0].lower())
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 69 + 25*ind, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
            if (i[0] == i[0].upper()):
                pygame.draw.circle(screen, Red, (rct.left + 12, rct.top + h + 3*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5)
        if i[0] == 'Space':
            Red = (255, 0, 0)
            pygame.draw.circle(screen, Red, (rct.left + 175, rct.top + h + 4*(rct.height-h)/5 + ((rct.height-h)/5)/2), 5) 

WIDTH = 1000
HEIGHT = 800
pygame.init()


def action(screen, background, flag, rec, lines, input_text, mainstr, i, time, count, mistakes, begin_time, error_message, heatmap, heatmap0):
    font = pygame.font.SysFont('arial', 25)
    if flag == -1:
        arr = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', 'Space', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        if mainstr == '':
            mainstr = random.choice(arr)
        game2_window(background, time, screen, error_message, mainstr, mistakes, begin_time, count)
        time = pygame.time.get_ticks()
        if 60-(time-begin_time)/1000 <= 0:
            flag = -2
    if flag == -2:
        game2_end_window((252, 15, 192), time, screen, mistakes, count, heatmap, heatmap0)
    if flag == 2:
        game1_window(background, time, screen, input_text, error_message, mainstr, mistakes, begin_time, count)
    for event in pygame.event.get():
        if flag == -2:
            game2_end_window((252, 15, 192), time, screen, mistakes, count, heatmap, heatmap0)
        if flag == 2:
            game1_window(background, time, screen, input_text, error_message, mainstr, mistakes, begin_time, count)
        if flag == 1:
            screen.fill(background)
            random_line = random.choice(lines)
            random_line = random_line.replace('\n', '')
            mainstr = random_line
            font = pygame.font.SysFont('arial', 25)
            text = font.render(random_line, 1, (255, 255, 255))
            place = text.get_rect(center=(WIDTH/2, HEIGHT/3))     
            screen.blit(text, place)
            font2 = pygame.font.SysFont('arial', 25)
            time = pygame.time.get_ticks()
            text2 = font2.render("Time: " + str((time-begin_time)/1000), 1, (255, 255, 255))
            text3 = font2.render("Total symbols: " + str(count), 1, (255, 255, 255))
            text4 = font2.render("Mistakes: " + str(mistakes), 1, (255, 255, 255))
            place = text2.get_rect(center=(90, 15))     
            screen.blit(text2, place)
            place = text3.get_rect(center=(WIDTH/2, 15))     
            screen.blit(text3, place)
            place = text4.get_rect(center=(WIDTH - 90, 15))     
            screen.blit(text4, place)
            font = pygame.font.SysFont('arial', 25)
            input_rect = pygame.Rect(250, HEIGHT/2, 500, 32)
            pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
            text_surface = font.render(str(input_text), 1, (255, 255, 255))
            screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))
            text5 = font.render(mainstr, 1, (255, 255, 255))
            place = text5.get_rect(center=(WIDTH/2, HEIGHT/3)) 
            screen.blit(text5, place)
            error_message = ""
            flag = 2
            font22 = pygame.font.SysFont('arial', 40)
            text22 = font22.render("Press ESC to exit", 1, (255, 255, 255))
            place = text22.get_rect(center=(WIDTH/2, HEIGHT - 100))     
            screen.blit(text22, place)
        if event.type == pygame.QUIT:
            save(time, count, mistakes, heatmap, rec)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and flag == 0:
                with open('src/record.txt', "w") as f:
                    f.seek(0)
                    f.write("0 0 0 {}")
                rec = ['0', '0', '0']
                heatmap = dict()
                heatmap0 = dict()
                prev_window(rec, heatmap, screen, background)
            if event.key == pygame.K_ESCAPE and (flag == -2):
                flag = 0
                save(time, count, mistakes, heatmap, rec)
                rec = record();
                index = 0
                for j in range(len(rec)):
                    if rec[j] == '{':
                        index = j
                        break
                input_text = ""
                mistakes = 0
                begin_time = 0
                count = 0
                mainstr = ""
                error_message = ""
                heatmap = json.loads(rec[index:])
                heatmap = dict(sorted(heatmap.items(), key=lambda x: x[1], reverse =True))
                rec = rec[:index].split();
                prev_window(rec, heatmap, screen, background)
            if event.key == pygame.K_ESCAPE and (flag == 1 or flag == 2):
                flag = 0
                save(time, count, mistakes, heatmap, rec)
                rec = record();
                index = 0
                for j in range(len(rec)):
                    if rec[j] == '{':
                        index = j
                        break
                input_text = ""
                mistakes = 0
                begin_time = 0
                count = 0
                mainstr = ""
                error_message = ""
                heatmap = json.loads(rec[index:])
                heatmap = dict(sorted(heatmap.items(), key=lambda x: x[1], reverse =True))
                rec = rec[:index].split();
                prev_window(rec, heatmap, screen, background)
            if event.key == pygame.K_RETURN and flag == 0:
                screen.fill(background)
                begin_time = pygame.time.get_ticks()
                mistakes = 0
                count = 0
                flag = 1
            if flag == -1:
                key_name = pygame.key.name(event.key)
                if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
                    key_name = key_name.upper()
                if key_name == "space":
                    key_name = "Space"
                if key_name == mainstr:
                    count += 1
                    input_text = ""
                    mainstr = ""
                    error_message = ""
                    game2_window(background, time, screen, error_message, mainstr, mistakes, begin_time, count)
                else:
                    font = pygame.font.SysFont('arial', 60)
                    if key_name != "LEFT SHIFT" and key_name != "RIGHT SHIFT" and key_name != "CAPS LOCK" and key_name != "caps lock":
                        if mainstr in heatmap:
                            heatmap[mainstr] += 1
                        else:
                            heatmap[mainstr] = 1
                        error_message = "Mistake :)"
                        text = font.render(error_message, 1, (255, 0, 0))
                        place = text.get_rect(center=(WIDTH/2, HEIGHT/6))     
                        screen.blit(text, place)
                        mistakes += 1
            if event.key == pygame.K_TAB and flag == 0:
                screen.fill(background)
                begin_time = pygame.time.get_ticks()
                mistakes = 0
                count = 0
                error_message = ""
                flag = -1
            if flag == 2:
                key_name = pygame.key.name(event.key)
                if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
                    key_name = key_name.upper()
                if key_name == "space":
                    key_name = " "
                if key_name == mainstr[i]:
                    screen.fill(background)
                    font = pygame.font.SysFont('arial', 25)
                    text = font.render(mainstr, 1, (255, 255, 255))
                    place = text.get_rect(center=(WIDTH/2, HEIGHT/3))     
                    screen.blit(text, place)
                    input_text += str(key_name)
                    input_rect = pygame.Rect(250, HEIGHT/2, 500, 32)
                    pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
                    text_surface = font.render(str(input_text), 1, (255, 255, 255))
                    screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))
                    text = font.render(error_message, 1, (255, 0, 0))
                    place = text.get_rect(center=(WIDTH/2, HEIGHT/6))     
                    screen.blit(text, place)
                    error_message = ""
                    font22 = pygame.font.SysFont('arial', 40)
                    text22 = font22.render("Press ESC to exit", 1, (255, 255, 255))
                    place = text22.get_rect(center=(WIDTH/2, HEIGHT - 100))     
                    screen.blit(text22, place)
                    i += 1
                    count += 1
                    if i == len(mainstr):
                        i = 0
                        flag = 1
                        input_text = ""
                else:
                    font = pygame.font.SysFont('arial', 60)
                    st = mainstr[i]
                    if st == " ":
                        st = "space"
                    if key_name != "LEFT SHIFT" and key_name != "RIGHT SHIFT" and key_name != "CAPS LOCK" and key_name != "caps lock":
                        if mainstr[i] in heatmap:
                            heatmap[mainstr[i]] += 1
                        else:
                            heatmap[mainstr[i]] = 1
                        error_message = "ERROR!!! It should be: " + st
                        text = font.render(error_message, 1, (255, 0, 0))
                        place = text.get_rect(center=(WIDTH/2, HEIGHT/6))     
                        screen.blit(text, place)
                        mistakes += 1
    return (flag, rec, input_text, mainstr, i, time, count, mistakes, begin_time, error_message, heatmap, heatmap0)