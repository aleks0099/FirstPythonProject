import pygame
import random
import sys
import json
import random
import magic_constants
import drawers

def draws_statistics_on_the_top_of_the_window(self, mod):
    if mod == 1:
        symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + "0", 1, magic_constants.White)
        if int(self.rec[0])/magic_constants.milisec_in_sec != 0:
            symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + str(round(int(self.rec[1])/(int(self.rec[0])/magic_constants.milisec_in_sec), 3)), 1, magic_constants.White)
        totsymbols_text = magic_constants.average_font.render("Total symbols: " + self.rec[1], 1, magic_constants.White)
        mistakes_text = magic_constants.average_font.render("Mistakes: " + self.rec[2], 1, magic_constants.White)
    if mod == 2:
        symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + "0", 1, magic_constants.White)
        if (self.time-self.begin_time)/magic_constants.milisec_in_sec != 0:
            symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + str(round(self.count/((self.time-self.begin_time)/magic_constants.milisec_in_sec), 3)), 1, magic_constants.White)
        totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(self.count), 1, magic_constants.White)
        mistakes_text = magic_constants.average_font.render("Mistakes: " + str(self.mistakes), 1, magic_constants.White)
    place = symbols_per_sec_text.get_rect(center=(magic_constants.symbols_per_sec_place, magic_constants.indent_from_above))     
    self.screen.blit(symbols_per_sec_text, place)
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    self.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    self.screen.blit(mistakes_text, place)

def drawing_without_events(self):
    if self.flag == magic_constants.only_keys_training_in_progress:
        if self.mainstr == '':
            self.mainstr = random.choice(magic_constants.keys_arr)
        self.time = drawers.draws_keys_to_be_pressed(self)
        self.time = pygame.time.get_ticks()
        if magic_constants.one_minute-(self.time-self.begin_time)/magic_constants.milisec_in_sec <= 0:
            self.flag = magic_constants.gm2_window_with_statistic_on_the_screen
    if self.flag == magic_constants.gm2_window_with_statistic_on_the_screen:
        drawers.draws_session_statistics_gm2(self)
    if self.flag == magic_constants.user_is_typing_sentence:
        drawers.draws_sentences_and_user_input_and_statistics(self)

def draws_heatmap_and_whole_statistics(self):
        self.screen.fill(self.background)
        gm1_text = magic_constants.big_font.render("Press Enter to start gamemode 1", 1, magic_constants.White)
        gm2_text = magic_constants.big_font.render("Press Tab to start gamemode 2", 1, magic_constants.White)
        inval_text = magic_constants.big_font.render("Press Space to invalidate statistics", 1, magic_constants.Green)
        place = gm1_text.get_rect(center=(magic_constants.center_width, magic_constants.gm1_text_height))     
        self.screen.blit(gm1_text, place)
        place = gm2_text.get_rect(center=(magic_constants.center_width, magic_constants.center_height))     
        self.screen.blit(gm2_text, place)
        place = inval_text.get_rect(center=(magic_constants.center_width, magic_constants.inval_text_height))
        self.screen.blit(inval_text, place)
        draws_statistics_on_the_top_of_the_window(self, 1)
        img = pygame.image.load('src/keyboard.png')
        rct = img.get_rect()
        rct.centerx = self.screen.get_rect().centerx
        rct.bottom = self.screen.get_rect().bottom - magic_constants.keyboard_lower_indent
        self.screen.blit(img, rct)
        self.index = 0
        arr = []
        for item in self.heatmap.items():
            if item[0] == ' ':
                arr.append([magic_constants.SPACE.title(), item[1]])
            else:
                arr.append(item)
            self.index += 1
            if self.index == magic_constants.number_of_main_mistakes:
                break
        mist_text = magic_constants.average_font.render("Top mistakes:", 1, magic_constants.Blue)
        place = mist_text.get_rect(center=(magic_constants.mistakes_text_left, rct.top))
        self.screen.blit(mist_text, place)
        k = 0
        for i in arr:
            k += 1
            mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, magic_constants.Blue)
            if i[1] == 1:
                mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, magic_constants.Blue)
            rect = mist_text.get_rect()
            rect.left = magic_constants.mistakes_left
            rect.bottom = rct.top + magic_constants.mistakes_interval*k
            self.screen.blit(mist_text, rect)
            key_board_drawer(self, i[0], rct) 

def one_symbol_draw(self, i, rct, ind, num1, num2):
    pygame.draw.circle(self.screen, magic_constants.Red, (rct.left + magic_constants.height_of_key + num1*magic_constants.interv + magic_constants.height_of_key*ind, rct.top + magic_constants.height_of_key + num2*(rct.height-magic_constants.height_of_key)/5 + ((rct.height-magic_constants.height_of_key)/5)/2), magic_constants.circle_rad)
    if i.isupper():
        pygame.draw.circle(self.screen, magic_constants.Red, (rct.left + magic_constants.interv, rct.top + magic_constants.height_of_key + 3*(rct.height-magic_constants.height_of_key)/5 + ((rct.height-magic_constants.height_of_key)/5)/2), magic_constants.circle_rad)

def key_board_drawer(self, i, rct):
    if i.lower() in magic_constants.key_brd0:
        ind = magic_constants.key_brd0.index(i.lower())
        one_symbol_draw(self, i, rct, ind, 1, 0)
    if i.lower() in magic_constants.key_brd1:
        ind = magic_constants.key_brd1.index(i.lower())
        one_symbol_draw(self, i, rct, ind, 2, 1)
    if i.lower() in magic_constants.key_brd2:
        ind = magic_constants.key_brd2.index(i.lower())
        one_symbol_draw(self, i, rct, ind, 3, 2)
    if i.lower() in magic_constants.key_brd3:
        ind = magic_constants.key_brd3.index(i.lower())
        one_symbol_draw(self, i, rct, ind, 4, 3)
    if i == magic_constants.SPACE.title():
        pygame.draw.circle(self.screen, magic_constants.Red, (rct.left + magic_constants.sp_koord, rct.top + magic_constants. height_of_key + 4*(rct.height-magic_constants.height_of_key)/5 + ((rct.height-magic_constants.height_of_key)/5)/2), magic_constants.circle_rad) 

def draws_sentences_and_user_input_and_statistics(self):
    self.screen.fill(self.background)
    self.time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str(round((self.time-self.begin_time)/magic_constants.milisec_in_sec, 3)), 1, magic_constants.White)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(self.count), 1, magic_constants.White)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(self.mistakes), 1, magic_constants.White)
    place = time_text.get_rect(center=(magic_constants.time_center, magic_constants.indent_from_above))     
    self.screen.blit(time_text, (magic_constants.left_indent, 0))
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    self.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    self.screen.blit(mistakes_text, place)
    main_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
    place = main_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))
    self.screen.blit(main_text, place)
    input_rect = pygame.Rect(place.x, magic_constants.center_height, place.width, place.height)
    pygame.draw.rect(self.screen, magic_constants.White, input_rect, magic_constants.frame)
    text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.White)
    self.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
    mainstr_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
    place = mainstr_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))     
    self.screen.blit(mainstr_text, place)
    error_text = magic_constants.average_font.render(self.error_message, 1, magic_constants.Red)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    self.screen.blit(error_text, place)
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
    self.screen.blit(magic_constants.exit_text, place)
    return self.time

def draws_keys_to_be_pressed(self):
    self.screen.fill(self.background)
    time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str(round(magic_constants.one_minute-(self.time-self.begin_time)/magic_constants.milisec_in_sec, 3)), 1, magic_constants.White)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(self.count), 1, magic_constants.White)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(self.mistakes), 1, magic_constants.White)
    place = time_text.get_rect(center=(magic_constants.time_center, magic_constants.indent_from_above))     
    self.screen.blit(time_text, (magic_constants.left_indent, 0))
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    self.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    self.screen.blit(mistakes_text, place)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = self.screen.get_rect().centerx
    rct.bottom = self.screen.get_rect().bottom - magic_constants.center_height
    self.screen.blit(img, rct)
    error_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.Red)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    self.screen.blit(error_text, place)
    arr = [self.mainstr]
    for i in arr:
        key_board_drawer(self, i, rct)
    return time

def draws_session_statistics_gm2(self):
    self.screen.fill(magic_constants.Pink)
    main_text = magic_constants.big_font.render("Your session statistics", 1, magic_constants.White)
    place = main_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))     
    self.screen.blit(main_text, place)
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_indent))     
    self.screen.blit(magic_constants.exit_text, place)
    draws_statistics_on_the_top_of_the_window(self, 2)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = self.screen.get_rect().centerx
    rct.bottom = self.screen.get_rect().bottom - magic_constants.keyboard_lower_indent
    self.screen.blit(img, rct)
    main_mistakes_array = []
    for item in self.heatmap.items():
        x = 0
        if item[0] in self.heatmap0.keys():
            x = self.heatmap0[item[0]]
        if item[1] - x != 0:
            if item[0] == ' ':
                main_mistakes_array.append((magic_constants.SPACE.title(), item[1] - x))
            else:
                main_mistakes_array.append((item[0], item[1] - x))
    main_mistakes_array = sorted(main_mistakes_array, key=lambda x: x[1], reverse=True)
    main_mistakes_array = main_mistakes_array[:magic_constants.number_of_main_mistakes]
    mist_text = magic_constants.average_font.render("Top mistakes:", 1, magic_constants.Blue)
    place = mist_text.get_rect(center=(magic_constants.mistakes_text_left, rct.top))
    self.screen.blit(mist_text, place)
    k = 0
    for i in main_mistakes_array:
        k += 1
        mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, magic_constants.Blue)
        if i[1] == 1:
            mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, magic_constants.Blue)
        rect = mist_text.get_rect()
        rect.left = magic_constants.mistakes_left
        rect.bottom = rct.top + magic_constants.mistakes_interval*k
        self.screen.blit(mist_text, rect)
        key_board_drawer(self, i[0], rct)