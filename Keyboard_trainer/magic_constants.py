import pygame

key_brd0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
key_brd1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
key_brd2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
key_brd3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
keys_arr = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', 'Space', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
WIDTH = 1000
HEIGHT = 800
Red = (255, 0, 0)
Blue = (30,144,255)
White = (255, 255, 255)
Green = (155, 205, 150)
Pink = (252, 15, 192)
interv = 11
sp_koord = 175
height_of_key = 25
indent_from_above = 15
circle_rad = 5
number_of_main_mistakes = 5
mistakes_left = 50
mistakes_interval = 55
keyboard_columns_interval = 25
above_left_and_right_indent = 90
symbols_per_sec_place = 110
left_indent = 45
exit_text_indent = 60
time_center = 90
one_minute = 60
milisec_in_sec = 1000
prev_window = 0
game1_window_change = 1
game1_window_process = 2
game2_window_process = -1
game2_end = -2
pygame.init()
big_font = pygame.font.SysFont('arial', 60)
average_font = pygame.font.SysFont('arial', 25)
small_font = pygame.font.SysFont('arial', 40)
exit_text = small_font.render("Press ESC to exit", 1, White)