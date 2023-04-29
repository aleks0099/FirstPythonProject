import pygame
import random
import sys
import random
import magic_constants
import drawers
import useful_functions

def quit(self):
    useful_functions.save(self.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
    sys.exit()

def changing_sentence(self):
    self.screen.fill(self.background)
    random_line = random.choice(self.lines)
    random_line = random_line.replace('\n', '')
    self.mainstr = random_line
    random_line_text = magic_constants.average_font.render(random_line, 1, magic_constants.White)
    place = random_line_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))
    x = place.x
    w = place.width
    h = place.height
    self.screen.blit(random_line_text, place)
    self.time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str((self.time-self.begin_time)/magic_constants.milisec_in_sec), 1, magic_constants.White)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(self.count), 1, magic_constants.White)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(self.mistakes), 1, magic_constants.White)
    place = time_text.get_rect(center=(magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    self.screen.blit(time_text, place)
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    self.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    self.screen.blit(mistakes_text, place)
    input_rect = pygame.Rect(x, magic_constants.center_height, w, h)
    pygame.draw.rect(self.screen, magic_constants.White, input_rect, magic_constants.frame)
    text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.White)
    self.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
    mainstr_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
    place = mainstr_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height)) 
    self.screen.blit(mainstr_text, place)
    self.error_message = ""
    self.flag = magic_constants.user_is_typing_sentence
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
    self.screen.blit(magic_constants.exit_text, place)

def invalidate_statistic(self):
    with open('src/record.txt', "w") as f:
        f.seek(0)
        f.write("0 0 0 {}")
    self.rec = ['0', '0', '0']
    self.heatmap = dict()
    self.heatmap0 = self.heatmap.copy()
    drawers.draws_heatmap_and_whole_statistics(self)

def exit(self):
    self.flag = magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen
    useful_functions.save(self.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
    self.rec = useful_functions.record()
    self.index = 0
    for j in range(len(self.rec)):
        if self.rec[j] == '{':
            self.index = j
            break
    useful_functions.annul(self)
    drawers.draws_heatmap_and_whole_statistics(self)

def starting_gm1(self):
    self.screen.fill(self.background)
    self.begin_time = pygame.time.get_ticks()
    self.mistakes = 0
    self.count = 0
    self.flag = magic_constants.need_to_change_sentence

def starting_gm2(self):
    self.screen.fill(self.background)
    self.begin_time = pygame.time.get_ticks()
    self.mistakes = 0
    self.count = 0
    self.error_message = ""
    self.flag = magic_constants.only_keys_training_in_progress

def typing_symbols_gm2(self, event):
    key_name = pygame.key.name(event.key)
    if event.key == magic_constants.full_stop_code:
        key_name = '.'
    if event.key == magic_constants.comma_code:
        key_name = ','
    if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
        key_name = key_name.upper()
    if key_name == magic_constants.SPACE:
        key_name = magic_constants.SPACE.title()
    if key_name == self.mainstr:
        self.count += 1
        self.input_text = ""
        self.mainstr = ""
        self.error_message = ""
        drawers.draws_keys_to_be_pressed(self)
    else:
        if not (key_name == "LEFT SHIFT" and self.mainstr.istitle()) and not (key_name == "RIGHT SHIFT" and self.mainstr.istitle()) and not (key_name == "CAPS LOCK" and self.mainstr.istitle()) and not (key_name == "caps lock" and self.mainstr.islower()):
            if self.mainstr in self.heatmap:
                self.heatmap[self.mainstr] += 1
            else:
                self.heatmap[self.mainstr] = 1
            self.error_message = "Mistake :)"
            error_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.Red)
            place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
            self.screen.blit(error_text, place)
            self.mistakes += 1

def creating_error_message(self, key_name):
    st = self.mainstr[self.symbol_number_in_str]
    if st == " ":
        st = magic_constants.SPACE
    if key_name != "LEFT SHIFT" and key_name != "RIGHT SHIFT" and key_name != "CAPS LOCK" and key_name != "caps lock" and key_name != "LEFT ALT" and key_name != "left alt":
        if self.mainstr[self.symbol_number_in_str] in self.heatmap:
            self.heatmap[self.mainstr[self.symbol_number_in_str]] += 1
        else:
            self.heatmap[self.mainstr[self.symbol_number_in_str]] = 1
        self.error_message = "ERROR!!! It should be: " + st
        self.mistakes += 1

def typing_sentence_gm2(self, event):
    key_name = pygame.key.name(event.key)
    if event.key == magic_constants.full_stop_code:
        key_name = '.'
    if event.key == magic_constants.comma_code:
        key_name = ','
    if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
        key_name = key_name.upper()
    if key_name == magic_constants.SPACE:
        key_name = " "
    if key_name == self.mainstr[self.symbol_number_in_str]:
        self.screen.fill(self.background)
        random_line_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
        place = random_line_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT/3))     
        self.screen.blit(random_line_text, place)
        self.input_text += str(key_name)
        input_rect = pygame.Rect(place.x, magic_constants.center_height, place.width, place.height)
        pygame.draw.rect(self.screen, magic_constants.White, input_rect, magic_constants.frame)
        text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.White)
        self.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
        error_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.Red)
        place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
        self.screen.blit(error_text, place)
        self.error_message = ""
        place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
        self.screen.blit(magic_constants.exit_text, place)
        self.symbol_number_in_str += 1
        self.count += 1
        if self.symbol_number_in_str == len(self.mainstr):
            self.symbol_number_in_str = 0
            self.flag = magic_constants.need_to_change_sentence
            self.input_text = ""
    else:
        creating_error_message(self, key_name)

def action(self):
    drawers.drawing_without_events(self)
    for event in pygame.event.get():
        if self.flag == magic_constants.gm2_window_with_statistic_on_the_screen:
            drawers.draws_session_statistics_gm2(self)
        if self.flag == magic_constants.user_is_typing_sentence:
            drawers.draws_sentences_and_user_input_and_statistics(self)
        if self.flag == magic_constants.need_to_change_sentence:
            changing_sentence(self)
        if event.type == pygame.QUIT:
            quit(self)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                invalidate_statistic(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.gm2_window_with_statistic_on_the_screen):
                exit(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.need_to_change_sentence or self.flag == magic_constants.user_is_typing_sentence):
                exit(self)
            if event.key == pygame.K_RETURN and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                starting_gm1(self)
            if self.flag == magic_constants.only_keys_training_in_progress:
                typing_symbols_gm2(self, event)
            if event.key == pygame.K_TAB and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                starting_gm2(self)
            if self.flag == magic_constants.user_is_typing_sentence:
                typing_sentence_gm2(self,event)