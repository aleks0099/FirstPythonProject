import pygame
import random
import sys
import random
import magic_constants
import drawers
import useful_functions

def action(self):
    if self.flag == magic_constants.game2_window_process:
        if self.mainstr == '':
            self.mainstr = random.choice(magic_constants.keys_arr)
        self.time = drawers.second_game_window_drawer(self)
        self.time = pygame.time.get_ticks()
        if magic_constants.one_minute-(self.time-self.begin_time)/magic_constants.milisec_in_sec <= 0:
            self.flag = magic_constants.game2_end
    if self.flag == magic_constants.game2_end:
        drawers.game2_end_window(self)
    if self.flag == magic_constants.game1_window_process:
        drawers.first_game_window_drawer(self)
    for event in pygame.event.get():
        if self.flag == magic_constants.game2_end:
            drawers.game2_end_window(self)
        if self.flag == magic_constants.game1_window_process:
            drawers.first_game_window_drawer(self)
        if self.flag == magic_constants.game1_window_change:
            self.screen.fill(self.background)
            random_line = random.choice(self.lines)
            random_line = random_line.replace('\n', '')
            self.mainstr = random_line
            random_line_text = magic_constants.average_font.render(random_line, 1, magic_constants.White)
            place = random_line_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT/3))
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
            place = totsymbols_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.indent_from_above))     
            self.screen.blit(totsymbols_text, place)
            place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
            self.screen.blit(mistakes_text, place)
            input_rect = pygame.Rect(x, magic_constants.HEIGHT/2, w, h)
            pygame.draw.rect(self.screen, magic_constants.White, input_rect, 2)
            text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.White)
            self.screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))
            mainstr_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
            place = mainstr_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT/3)) 
            self.screen.blit(mainstr_text, place)
            self.error_message = ""
            self.flag = magic_constants.game1_window_process
            place = magic_constants.exit_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT - magic_constants.HEIGHT/8))     
            self.screen.blit(magic_constants.exit_text, place)
        if event.type == pygame.QUIT:
            useful_functions.save(self.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.flag == magic_constants.prev_window:
                with open('src/record.txt', "w") as f:
                    f.seek(0)
                    f.write("0 0 0 {}")
                self.rec = ['0', '0', '0']
                self.heatmap = dict()
                self.heatmap0 = self.heatmap.copy()
                drawers.prev_window(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.game2_end):
                self.flag = magic_constants.prev_window
                useful_functions.save(self.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
                self.rec = useful_functions.record();
                self.index = 0
                for j in range(len(self.rec)):
                    if self.rec[j] == '{':
                        self.index = j
                        break
                useful_functions.annul(self)
                drawers.prev_window(self)
            if event.key == pygame.K_ESCAPE and (self.flag == magic_constants.game1_window_change or self.flag == magic_constants.game1_window_process):
                self.flag = magic_constants.prev_window
                useful_functions.save(self.time-self.begin_time, self.count, self.mistakes, self.heatmap, self.rec)
                self.rec = useful_functions.record()
                self.index = 0
                for j in range(len(self.rec)):
                    if self.rec[j] == '{':
                        self.index = j
                        break
                useful_functions.annul(self)
                drawers.prev_window(self)
            if event.key == pygame.K_RETURN and self.flag == magic_constants.prev_window:
                self.screen.fill(self.background)
                self.begin_time = pygame.time.get_ticks()
                self.mistakes = 0
                self.count = 0
                self.flag = magic_constants.game1_window_change
            if self.flag == magic_constants.game2_window_process:
                key_name = pygame.key.name(event.key)
                if event.key == 1102:
                    key_name = '.'
                if event.key == 1073:
                    key_name = ','
                if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
                    key_name = key_name.upper()
                if key_name == "space":
                    key_name = "Space"
                if key_name == self.mainstr:
                    self.count += 1
                    self.input_text = ""
                    self.mainstr = ""
                    self.error_message = ""
                    drawers.second_game_window_drawer(self)
                else:
                    if not (key_name == "LEFT SHIFT" and self.mainstr.istitle()) and not (key_name == "RIGHT SHIFT" and self.mainstr.istitle()) and not (key_name == "CAPS LOCK" and self.mainstr.istitle()) and not (key_name == "caps lock" and self.mainstr.islower()):
                        if self.mainstr in self.heatmap:
                            self.heatmap[self.mainstr] += 1
                        else:
                            self.heatmap[self.mainstr] = 1
                        self.error_message = "Mistake :)"
                        random_line_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.Red)
                        place = random_line_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT/6))     
                        self.screen.blit(random_line_text, place)
                        self.mistakes += 1
            if event.key == pygame.K_TAB and self.flag == magic_constants.prev_window:
                self.screen.fill(self.background)
                self.begin_time = pygame.time.get_ticks()
                self.mistakes = 0
                self.count = 0
                self.error_message = ""
                self.flag = magic_constants.game2_window_process
            if self.flag == magic_constants.game1_window_process:
                key_name = pygame.key.name(event.key)
                if event.key == 1102:
                    key_name = '.'
                if event.key == 1073:
                    key_name = ','
                if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
                    key_name = key_name.upper()
                if key_name == "space":
                    key_name = " "
                if key_name == self.mainstr[self.symbol_number_in_str]:
                    self.screen.fill(self.background)
                    random_line_text = magic_constants.average_font.render(self.mainstr, 1, magic_constants.White)
                    place = random_line_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT/3))     
                    self.screen.blit(random_line_text, place)
                    self.input_text += str(key_name)
                    input_rect = pygame.Rect(place.x, magic_constants.HEIGHT/2, place.width, place.height)
                    pygame.draw.rect(self.screen, magic_constants.White, input_rect, 2)
                    text_surface = magic_constants.average_font.render(str(self.input_text), 1, magic_constants.White)
                    self.screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))
                    random_line_text = magic_constants.big_font.render(self.error_message, 1, magic_constants.Red)
                    place = random_line_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT/6))     
                    self.screen.blit(random_line_text, place)
                    self.error_message = ""
                    place = magic_constants.exit_text.get_rect(center=(magic_constants.WIDTH/2, magic_constants.HEIGHT - magic_constants.HEIGHT/8))     
                    self.screen.blit(magic_constants.exit_text, place)
                    self.symbol_number_in_str += 1
                    self.count += 1
                    if self.symbol_number_in_str == len(self.mainstr):
                        self.symbol_number_in_str = 0
                        self.flag = magic_constants.game1_window_change
                        self.input_text = ""
                else:
                    st = self.mainstr[self.symbol_number_in_str]
                    if st == " ":
                        st = "space"
                    if key_name != "LEFT SHIFT" and key_name != "RIGHT SHIFT" and key_name != "CAPS LOCK" and key_name != "caps lock" and key_name != "LEFT ALT" and key_name != "left alt":
                        if self.mainstr[self.symbol_number_in_str] in self.heatmap:
                            self.heatmap[self.mainstr[self.symbol_number_in_str]] += 1
                        else:
                            self.heatmap[self.mainstr[self.symbol_number_in_str]] = 1
                        self.error_message = "ERROR!!! It should be: " + st
                        self.mistakes += 1