origin = [0, 0]
title_text = [8, 8]
new_button = [480, 320, 320, 80]
new_text = [504, 344]
load_button = [480, 480, 320, 80]
load_text = [504, 504]

class Load_Window():
    rect = [320, 240, 640, 240]
    window_title = [344, 264]
    close = [920, 240, 40, 40]

    file_list_rect = [[400, 320, 240, 40], [400, 360, 240, 40], [400, 400, 240, 40], [640, 320, 240, 40], [640, 360, 240, 40], [640, 400, 240, 40]]
    file_list_text = [[424, 324], [424, 364], [424, 404], [664, 324], [664, 364], [664, 404]]
    load_button = [840, 440, 120, 40]
    load_text = [864, 444]
    button_prev = [320, 440, 40, 40]
    button_next = [800, 440, 40, 40]
    page_number = [400, 444]

class Upper_Bar():
    rect = [0, 0, 1280, 40]
    new = [0, 0, 40, 40]
    load = [40, 0, 40, 40]
    save = [80, 0, 40, 40]
    pointer = [120, 0, 40, 40]
    brush = [160, 0, 40, 40]
    erase = [200, 0, 40, 40]
    move = [240, 0, 40, 40]
    play = [280, 0, 40, 40]
    close = [1240, 0, 40, 40]

class File_Name_Bar():
    rect = [0, 40, 1280, 40]
    text = [24, 44]

class Left_Bar():
    rect = [0, 80, 480, 600]
    tab_block = [0, 80, 80, 80]
    icon_block = [20, 100]
    tab_thing = [80, 80, 80, 80]
    icon_thing = [100, 100]
    tab_goal = [160, 80, 80, 80]
    icon_goal = [180, 100]
    tab_background = [240, 80, 80, 80]
    icon_background = [260, 100]
    button_start = [0, 160]

class Game_Screen():
    rect = [480, 80, 800, 600]

class Lower_Bar():
    rect = [0, 680, 1280, 40]
    text_mode = [24, 684]

class Save_Window():
    rect = [320, 240, 640, 240]
    window_title = [344, 264]
    close = [920, 240, 40, 40]

    text_name = [344, 324]
    text_box = [480, 320, 320, 40]
    file_name = [504, 324]
    button_save = [800, 320, 120, 40]
    text_save = [824, 324]

class Upper_Play():
    play = [580, 0, 40, 40]
    pause = [620, 0, 40, 40]
    stop = [660, 0, 40, 40]

class Lower_Play():
    rect = [0, 660, 1280, 60]

class Game_Screen_Play():
    rect = [240, 60, 800, 600]

class Tutorial_Play():
    move_key = [20, 60]
    move_text = [164, 104]
    space_key = [20, 180]
    space_text = [164, 184]
    result_text = [20, 264]
