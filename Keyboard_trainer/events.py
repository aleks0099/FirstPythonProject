import pygame
import random
import sys
import random
import magic_constants
import drawers
import useful_functions
import global_variables

def quit(self):
    useful_functions.save(global_variables.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
    sys.exit()

def changing_sentence(self):
    global_variables.screen.fill(global_variables.BACKGROUND)
    random_line = random.choice(self.lines)
    random_line = random_line.replace('\n', '')
    self.mainstr = random_line
    random_line_text = magic_constants.average_font.render(random_line, 1, magic_constants.WHITE)
    place = random_line_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))
    x = place.x
    w = place.width
    h = place.height
    global_variables.screen.blit(random_line_text, place)
    global_variables.time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str((global_variables.time-self.begin_time)/magic_constants.milisec_in_sec), 1, magic_constants.WHITE)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(self.count), 1, magic_constants.WHITE)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(self.mistakes), 1, magic_constants.WHITE)
    place = time_text.get_rect(center=(magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    global_variables.screen.blit(time_text, place)
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    global_variables.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    global_variables.screen.blit(mistakes_text, place)
    input_rect = pygame.Rect(x, magic_constants.center_height, w, h)
    pygame.draw.rect(global_variables.screen, magic_constants.WHITE, input_rect, magic_constants.frame)
    text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.WHITE)
    global_variables.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
    mainstr_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.WHITE)
    place = mainstr_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height)) 
    global_variables.screen.blit(mainstr_text, place)
    self.error_message = ""
    self.flag = magic_constants.user_is_typing_sentence
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
    global_variables.screen.blit(magic_constants.exit_text, place)

def invalidate_statistic(self):
    with open('src/record.txt', "w") as f:
        f.seek(0)
        f.write(magic_constants.RESET_STATISTICS_IN_FILE)
    self.rec = ['0', '0', '0']
    self.heatmap = dict()
    self.heatmap0 = self.heatmap.copy()
    self.index = drawers.draws_heatmap_and_whole_statistics(self.rec, self.begin_time, self.mistakes, self.count, self.heatmap)

def exit(self):
    self.flag = magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen
    useful_functions.save(global_variables.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
    self.rec = useful_functions.record()
    self.index = 0
    for j in range(len(self.rec)):
        if self.rec[j] == '{':
            self.index = j
            break
    useful_functions.annul(self)
    self.index = drawers.draws_heatmap_and_whole_statistics(self.rec, self.begin_time, self.mistakes, self.count, self.heatmap)

def invalidate_mistakes_symbols_and_error_message(self):
    global_variables.screen.fill(global_variables.BACKGROUND)
    self.begin_time = pygame.time.get_ticks()
    self.mistakes = 0
    self.count = 0
    self.error_message = ""

def error_key_pressed(self):
    if self.mainstr in self.heatmap:
        self.heatmap[self.mainstr] += 1
    else:
        self.heatmap[self.mainstr] = 1
    self.error_message = "Mistake :)"
    error_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.RED)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    global_variables.screen.blit(error_text, place)
    self.mistakes += 1

def getting_key_pressed(event):
    key_name = pygame.key.name(event.key)
    if event.key == magic_constants.full_stop_code:
        key_name = '.'
    if event.key == magic_constants.comma_code:
        key_name = ','
    if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
        key_name = key_name.upper()
    if key_name == magic_constants.SPACE:
        key_name = magic_constants.SPACE.title()
    return key_name

def pressing_keys(self, event):
    key_name = getting_key_pressed(event)
    if key_name == self.mainstr:
        self.count += 1
        self.input_text = ""
        self.mainstr = ""
        self.error_message = ""
        drawers.draws_keys_to_be_pressed(self.begin_time, self.count, self.mistakes, self.mainstr, self.error_message)
    elif not (key_name == magic_constants.LEFT_SHIFT and self.mainstr.istitle()) and not (key_name == magic_constants.RIGHT_SHIFT and self.mainstr.istitle()) \
        and not (key_name == magic_constants.CAPS_LOCK_ON and self.mainstr.istitle()) and not (key_name == magic_constants.CAPS_LOCK_OFF and self.mainstr.islower()):
        error_key_pressed(self)

def creating_error_message(self, key_name):
    st = self.mainstr[self.symbol_number_in_str]
    if st == " ":
        st = magic_constants.SPACE
    if key_name != magic_constants.LEFT_SHIFT and key_name != magic_constants.RIGHT_SHIFT and key_name != magic_constants.CAPS_LOCK_ON and key_name != magic_constants.CAPS_LOCK_OFF \
        and key_name != magic_constants.BIG_LEFT_ALT and key_name != magic_constants.SMALL_LEFT_ALT:
        if self.mainstr[self.symbol_number_in_str] in self.heatmap:
            self.heatmap[self.mainstr[self.symbol_number_in_str]] += 1
        else:
            self.heatmap[self.mainstr[self.symbol_number_in_str]] = 1
        self.error_message = "ERROR!!! It should be: " + st
        self.mistakes += 1

def printing(self, key_name):
    global_variables.screen.fill(global_variables.BACKGROUND)
    random_line_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.WHITE)
    place = random_line_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))     
    global_variables.screen.blit(random_line_text, place)
    self.input_text += str(key_name)
    input_rect = pygame.Rect(place.x, magic_constants.center_height, place.width, place.height)
    pygame.draw.rect(global_variables.screen, magic_constants.WHITE, input_rect, magic_constants.frame)
    text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.WHITE)
    global_variables.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
    error_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.RED)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    global_variables.screen.blit(error_text, place)
    self.error_message = ""
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
    global_variables.screen.blit(magic_constants.exit_text, place)
    self.symbol_number_in_str += 1
    self.count += 1
    if self.symbol_number_in_str == len(self.mainstr):
        self.symbol_number_in_str = 0
        self.flag = magic_constants.need_to_change_sentence
        self.input_text = ""

def typing_sentence(self, event):
    key_name = getting_key_pressed(event)
    if key_name == magic_constants.SPACE.title():
        key_name = " "
    if key_name == self.mainstr[self.symbol_number_in_str]:
       printing(self, key_name)
    else:
        creating_error_message(self, key_name)

def action(self):
    arr = drawers.drawing_without_events(self.flag, self.mainstr, self.rec, self.begin_time, self.mistakes, self.count, \
        self.heatmap, self.heatmap0, self.error_message, self.input_text)
    self.mainstr = arr[0]
    self.flag = arr[1]
    for event in pygame.event.get():
        if self.flag == magic_constants.gm2_window_with_statistic_on_the_screen:
            drawers.draws_session_statistics_gm2(self.rec, self.begin_time, self.mistakes, self.count, self.heatmap, self.heatmap0)
        if self.flag == magic_constants.user_is_typing_sentence:
            drawers.draws_sentences_and_user_input_and_statistics(self.begin_time, self.count, self.mistakes, \
                self.mainstr, self.input_text, self.error_message)
        if self.flag == magic_constants.need_to_change_sentence:
            changing_sentence(self)
        if event.type == pygame.QUIT:
            quit(self)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                invalidate_statistic(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.gm2_window_with_statistic_on_the_screen):
                exit(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.need_to_change_sentence \
                or self.flag == magic_constants.user_is_typing_sentence):
                exit(self)
            if event.key == pygame.K_RETURN and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                invalidate_mistakes_symbols_and_error_message(self)
                self.flag = magic_constants.need_to_change_sentence
            if self.flag == magic_constants.only_keys_training_in_progress:
                pressing_keys(self, event)
            if event.key == pygame.K_TAB and self.flag == magic_constants.prev_window_with_statistic_and_heatmap_on_the_screen:
                invalidate_mistakes_symbols_and_error_message(self)
                self.flag = magic_constants.only_keys_training_in_progress
            if self.flag == magic_constants.user_is_typing_sentence:
                typing_sentence(self,event)