import pygame
import random
import sys
import json
import random
import magic_constants
import global_variables

def draws_statistics_on_the_top_of_the_window(rec, mod, begin_time, mistakes, count):
    if mod == 1:
        symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + "0", 1, magic_constants.WHITE)
        if int(rec[0])/magic_constants.milisec_in_sec != 0:
            symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + str(round(int(rec[1])/ \
                (int(rec[0])/magic_constants.milisec_in_sec), magic_constants.numbers_after_comma)), 1, magic_constants.WHITE)
        totsymbols_text = magic_constants.average_font.render("Total symbols: " + rec[1], 1, magic_constants.WHITE)
        mistakes_text = magic_constants.average_font.render("Mistakes: " + rec[2], 1, magic_constants.WHITE)
    if mod == 2:
        symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + "0", 1, magic_constants.WHITE)
        if (global_variables.time-begin_time)/magic_constants.milisec_in_sec != 0:
            symbols_per_sec_text = magic_constants.average_font.render("Symbols per sec: " + str(round(count/ \
                ((global_variables.time-begin_time)/magic_constants.milisec_in_sec), magic_constants.numbers_after_comma)), 1, magic_constants.WHITE)
        totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(count), 1, magic_constants.WHITE)
        mistakes_text = magic_constants.average_font.render("Mistakes: " + str(mistakes), 1, magic_constants.WHITE)
    place = symbols_per_sec_text.get_rect(center=(magic_constants.symbols_per_sec_place, magic_constants.indent_from_above))     
    global_variables.screen.blit(symbols_per_sec_text, place)
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    global_variables.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    global_variables.screen.blit(mistakes_text, place)

def drawing_without_events(flag, mainstr, rec, begin_time, mistakes, count, heatmap, heatmap0, error_message, input_text):
    if flag == magic_constants.only_keys_training_in_progress:
        if mainstr == '':
            mainstr = random.choice(magic_constants.all_keys)
        draws_keys_to_be_pressed(begin_time, count, mistakes, mainstr, error_message)
        global_variables.time = pygame.time.get_ticks()
        if magic_constants.one_minute-(global_variables.time-begin_time)/magic_constants.milisec_in_sec <= 0:
            flag = magic_constants.gm2_window_with_statistic_on_the_screen
    if flag == magic_constants.gm2_window_with_statistic_on_the_screen:
        draws_session_statistics_gm2(rec, begin_time, mistakes, count, heatmap, heatmap0)
    if flag == magic_constants.user_is_typing_sentence:
        draws_sentences_and_user_input_and_statistics(begin_time, count, mistakes, mainstr, input_text, error_message)
    return [mainstr, flag]  

def draws_heatmap_and_whole_statistics(rec, begin_time, mistakes, count, heatmap):
        global_variables.screen.fill(global_variables.BACKGROUND)
        how_to_start_the_first_game = magic_constants.big_font.render("Press Enter to start gamemode 1", 1, magic_constants.WHITE)
        how_to_start_the_second_game = magic_constants.big_font.render("Press Tab to start gamemode 2", 1, magic_constants.WHITE)
        inval_text = magic_constants.big_font.render("Press Space to invalidate statistics", 1, magic_constants.GREEN)
        place = how_to_start_the_first_game.get_rect(center=(magic_constants.center_width, magic_constants.how_to_start_the_first_game_text_height))     
        global_variables.screen.blit(how_to_start_the_first_game, place)
        place = how_to_start_the_second_game.get_rect(center=(magic_constants.center_width, magic_constants.center_height))     
        global_variables.screen.blit(how_to_start_the_second_game, place)
        place = inval_text.get_rect(center=(magic_constants.center_width, magic_constants.inval_text_height))
        global_variables.screen.blit(inval_text, place)
        draws_statistics_on_the_top_of_the_window(rec, 1, begin_time, mistakes, count)
        img = pygame.image.load('src/keyboard.png')
        rct = img.get_rect()
        rct.centerx = global_variables.screen.get_rect().centerx
        rct.bottom = global_variables.screen.get_rect().bottom - magic_constants.keyboard_lower_indent
        global_variables.screen.blit(img, rct)
        index = 0
        arr = []
        for item in heatmap.items():
            if item[0] == ' ':
                arr.append([magic_constants.SPACE.title(), item[1]])
            else:
                arr.append(item)
            index += 1
            if index == magic_constants.number_of_main_mistakes:
                break
        mist_text = magic_constants.average_font.render("Top mistakes:", 1, magic_constants.BLUE)
        place = mist_text.get_rect(center=(magic_constants.mistakes_text_left, rct.top))
        global_variables.screen.blit(mist_text, place)
        k = 0
        for i in arr:
            k += 1
            mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, magic_constants.BLUE)
            if i[1] == 1:
                mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, magic_constants.BLUE)
            rect = mist_text.get_rect()
            rect.left = magic_constants.mistakes_left
            rect.bottom = rct.top + magic_constants.mistakes_interval*k
            global_variables.screen.blit(mist_text, rect)
            key_board_drawer(i[0], rct)
        return index 

def one_symbol_draw(i, rct, ind, how_much_interv_we_need_to_leave_on_the_left, keyboard_row_index):
    pygame.draw.circle(global_variables.screen, magic_constants.RED, (rct.left + magic_constants.height_of_key + \
        how_much_interv_we_need_to_leave_on_the_left*magic_constants.INTERV + magic_constants.height_of_key*ind, rct.top + \
            magic_constants.height_of_key + keyboard_row_index*(rct.height-magic_constants.height_of_key)/magic_constants.number_of_keyboard_rows \
                 + ((rct.height-magic_constants.height_of_key)/magic_constants.number_of_keyboard_rows)/ \
                    magic_constants.devide_to_find_height_of_half_key), magic_constants.circle_rad)
    if i.isupper():
        pygame.draw.circle(global_variables.screen, magic_constants.RED, (rct.left + magic_constants.INTERV, rct.top + \
            magic_constants.height_of_key + magic_constants.shift_keyboard_row_index*(rct.height-magic_constants.height_of_key)/ \
                magic_constants.number_of_keyboard_rows + ((rct.height-magic_constants.height_of_key)/magic_constants.number_of_keyboard_rows)/ \
                    magic_constants.devide_to_find_height_of_half_key), magic_constants.circle_rad)

def key_board_drawer(i, rct):
    if i.lower() in magic_constants.keyboard_row_with_numbers:
        ind = magic_constants.keyboard_row_with_numbers.index(i.lower())
        one_symbol_draw(i, rct, ind, magic_constants.how_much_interv_we_need_to_leave_on_the_left_first_row, \
            magic_constants.first_keyboard_row_index)
    if i.lower() in magic_constants.first_keyboard_row_with_letters:
        ind = magic_constants.first_keyboard_row_with_letters.index(i.lower())
        one_symbol_draw(i, rct, ind, magic_constants.how_much_interv_we_need_to_leave_on_the_left_second_row, \
            magic_constants.second_keyboard_row_index)
    if i.lower() in magic_constants.second_keyboard_row_with_letters:
        ind = magic_constants.second_keyboard_row_with_letters.index(i.lower())
        one_symbol_draw(i, rct, ind, magic_constants.how_much_interv_we_need_to_leave_on_the_left_third_row, \
            magic_constants.third_keyboard_row_index)
    if i.lower() in magic_constants.third_keyboard_row_with_letters:
        ind = magic_constants.third_keyboard_row_with_letters.index(i.lower())
        one_symbol_draw(i, rct, ind, magic_constants.how_much_interv_we_need_to_leave_on_the_left_fourth_row, \
            magic_constants.fourth_keyboard_row_index)
    if i == magic_constants.SPACE.title():
        pygame.draw.circle(global_variables.screen, magic_constants.RED, (rct.left + magic_constants.space_koord, \
            rct.top + magic_constants. height_of_key + magic_constants.space_keyboard_row_index*(rct.height-magic_constants.height_of_key)/ \
                magic_constants.number_of_keyboard_rows + ((rct.height-magic_constants.height_of_key)/magic_constants.number_of_keyboard_rows)/ \
                    magic_constants.devide_to_find_height_of_half_key), magic_constants.circle_rad) 

def draws_sentences_and_user_input_and_statistics(begin_time, count, mistakes, mainstr, input_text, error_message):
    global_variables.screen.fill(global_variables.BACKGROUND)
    global_variables.time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str(round((global_variables.time-begin_time)/magic_constants.milisec_in_sec, \
        magic_constants.numbers_after_comma)), 1, magic_constants.WHITE)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(count), 1, magic_constants.WHITE)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(mistakes), 1, magic_constants.WHITE)
    place = time_text.get_rect(center=(magic_constants.time_center, magic_constants.indent_from_above))     
    global_variables.screen.blit(time_text, (magic_constants.left_indent, 0))
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    global_variables.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    global_variables.screen.blit(mistakes_text, place)
    main_text = magic_constants.average_font.render(mainstr, 1, magic_constants.WHITE)
    place = main_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))
    global_variables.screen.blit(main_text, place)
    input_rect = pygame.Rect(place.x, magic_constants.center_height, place.width, place.height)
    pygame.draw.rect(global_variables.screen, magic_constants.WHITE, input_rect, magic_constants.frame)
    text_surface = magic_constants.average_font.render(str(input_text), 1, magic_constants.WHITE)
    global_variables.screen.blit(text_surface, (input_rect.x + magic_constants.frame, input_rect.y + magic_constants.frame))
    mainstr_text = magic_constants.average_font.render(mainstr, 1, magic_constants.WHITE)
    place = mainstr_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))     
    global_variables.screen.blit(mainstr_text, place)
    error_text = magic_constants.average_font.render(error_message, 1, magic_constants.RED)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    global_variables.screen.blit(error_text, place)
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_lower_indent))     
    global_variables.screen.blit(magic_constants.exit_text, place)

def draws_keys_to_be_pressed(begin_time, count, mistakes, mainstr, error_message):
    global_variables.screen.fill(global_variables.BACKGROUND)
    global_variables.time = pygame.time.get_ticks()
    time_text = magic_constants.average_font.render("Time: " + str(round(magic_constants.one_minute-(global_variables.time-begin_time)/ \
        magic_constants.milisec_in_sec, magic_constants.numbers_after_comma)), 1, magic_constants.WHITE)
    totsymbols_text = magic_constants.average_font.render("Total symbols: " + str(count), 1, magic_constants.WHITE)
    mistakes_text = magic_constants.average_font.render("Mistakes: " + str(mistakes), 1, magic_constants.WHITE)
    place = time_text.get_rect(center=(magic_constants.time_center, magic_constants.indent_from_above))     
    global_variables.screen.blit(time_text, (magic_constants.left_indent, 0))
    place = totsymbols_text.get_rect(center=(magic_constants.center_width, magic_constants.indent_from_above))     
    global_variables.screen.blit(totsymbols_text, place)
    place = mistakes_text.get_rect(center=(magic_constants.WIDTH - magic_constants.above_left_and_right_indent, magic_constants.indent_from_above))     
    global_variables.screen.blit(mistakes_text, place)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = global_variables.screen.get_rect().centerx
    rct.bottom = global_variables.screen.get_rect().bottom - magic_constants.center_height
    global_variables.screen.blit(img, rct)
    error_text = magic_constants.big_font.render(error_message, 1, magic_constants.RED)
    place = error_text.get_rect(center=(magic_constants.center_width, magic_constants.error_text_height))     
    global_variables.screen.blit(error_text, place)
    arr = [mainstr]
    for i in arr:
        key_board_drawer(i, rct)

def draws_session_statistics_gm2(rec, begin_time, mistakes, count, heatmap, heatmap0):
    global_variables.screen.fill(magic_constants.PINK)
    main_text = magic_constants.big_font.render("Your session statistics", 1, magic_constants.WHITE)
    place = main_text.get_rect(center=(magic_constants.center_width, magic_constants.mainstr_height))     
    global_variables.screen.blit(main_text, place)
    place = magic_constants.exit_text.get_rect(center=(magic_constants.center_width, magic_constants.HEIGHT - magic_constants.exit_text_indent))     
    global_variables.screen.blit(magic_constants.exit_text, place)
    draws_statistics_on_the_top_of_the_window(rec, 2, begin_time, mistakes, count)
    img = pygame.image.load('src/keyboard.png')
    rct = img.get_rect()
    rct.centerx = global_variables.screen.get_rect().centerx
    rct.bottom = global_variables.screen.get_rect().bottom - magic_constants.keyboard_lower_indent
    global_variables.screen.blit(img, rct)
    main_mistakes_array = []
    for item in heatmap.items():
        x = 0
        if item[0] in heatmap0.keys():
            x = heatmap0[item[0]]
        if item[1] - x != 0:
            if item[0] == ' ':
                main_mistakes_array.append((magic_constants.SPACE.title(), item[1] - x))
            else:
                main_mistakes_array.append((item[0], item[1] - x))
    main_mistakes_array = sorted(main_mistakes_array, key=lambda x: x[1], reverse=True)
    main_mistakes_array = main_mistakes_array[:magic_constants.number_of_main_mistakes]
    mist_text = magic_constants.average_font.render("Top mistakes:", 1, magic_constants.BLUE)
    place = mist_text.get_rect(center=(magic_constants.mistakes_text_left, rct.top))
    global_variables.screen.blit(mist_text, place)
    k = 0
    for i in main_mistakes_array:
        k += 1
        mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistakes", 1, magic_constants.BLUE)
        if i[1] == 1:
            mist_text = magic_constants.average_font.render(str(k) + ") " + i[0] + ": " + str(i[1]) + " mistake", 1, magic_constants.BLUE)
        rect = mist_text.get_rect()
        rect.left = magic_constants.mistakes_left
        rect.bottom = rct.top + magic_constants.mistakes_interval*k
        global_variables.screen.blit(mist_text, rect)
        key_board_drawer(i[0], rct)