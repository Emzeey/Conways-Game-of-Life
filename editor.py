import sys
import pygame
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Saved files import
def files():
    saves = []
    if 'saves' not in os.listdir(os.path.abspath('.')):
        os.mkdir(os.path.abspath('saves'))
    else:
        dir_path = os.path.join(os.path.abspath('.'), 'saves')
        for path in os.listdir(dir_path):
            path = path.split('.')
            if path[-1] == 'txt':
                path.pop(-1)
                saves.append('.'.join(path))
    return saves


# Editor's save function
def save(display, board, name, loaded):
    saved = files()

    medium_font = pygame.font.Font(None, 35)
    mini_font = pygame.font.Font(None, 20)

    font_color = 'black'
    save_button_color = [110, 110, 110]
    back_button_color = [110, 110, 110]
    while True:
        for event in pygame.event.get():
            # Quit events
            if event.type == pygame.QUIT:
                sys.exit()
            # Key down events
            if event.type == pygame.KEYDOWN:
                try:
                    if len(name) < 15 and event.key != pygame.K_BACKSPACE and event.key != pygame.K_ESCAPE \
                            and event.unicode != '\r':
                        name += event.unicode
                        font_color = 'black'
                except KeyError:
                    continue
                finally:
                    if event.key == pygame.K_ESCAPE:
                        return 0
                    if event.key == pygame.K_BACKSPACE:
                        name = [x for x in name]
                        if len(name) > 0:
                            name.pop(-1)
                        name = ''.join(name)
                        font_color = 'black'
                    if event.unicode == '\r':
                        if name in saved and not loaded:
                            font_color = 'red'
                        else:
                            file = open(f'saves/{name}.txt', 'w')
                            for i in range(len(board)):
                                file.writelines(''.join(board[i]))
                                file.write('\n')
                            file.close()
                            return 0
            # Mouse button down events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 480 < event.pos[0] < 580 and 330 < event.pos[1] < 345:
                    if name in saved and not loaded:
                        font_color = 'red'
                    else:
                        if 'saves' not in os.listdir():
                            os.mkdir('saves')
                        file = open(f'saves/{name}.txt', 'w')
                        for i in range(len(board)):
                            file.writelines(''.join(board[i]))
                            file.write('\n')
                        file.close()
                        return 0
                if event.button == 1 and 620 < event.pos[0] < 720 and 330 < event.pos[1] < 345:
                    return 0
            # Mouse motion events
            if event.type == pygame.MOUSEMOTION:
                if 480 < event.pos[0] < 580 and 330 < event.pos[1] < 345:
                    save_button_color = [130, 130, 130]
                else:
                    save_button_color = [110, 110, 110]
                if 620 < event.pos[0] < 720 and 330 < event.pos[1] < 345:
                    back_button_color = [130, 130, 130]
                else:
                    back_button_color = [110, 110, 110]

        # Base rectangle
        pygame.draw.rect(display, [255, 0, 0], [400, 255, 400, 115])
        pygame.draw.rect(display, [255, 255, 255], [405, 260, 390, 105])

        # Writing space
        pygame.draw.rect(display, [150, 150, 150], [430, 285, 340, 30])

        # Buttons
        pygame.draw.rect(display, save_button_color, [480, 330, 100, 15])
        pygame.draw.rect(display, back_button_color, [620, 330, 100, 15])

        # Rendering fonts
        display.blit(medium_font.render(f'{name}|', True, font_color), [430, 287.5])
        display.blit(mini_font.render('SAVE', True, 'black'), [510, 330])
        display.blit(mini_font.render('BACK', True, 'black'), [650, 330])

        pygame.display.update()


# Editor's load function
def load(display):
    saved = files()
    name = ''

    # Fonts
    medium_font = pygame.font.Font(None, 35)
    mini_font = pygame.font.Font(None, 20)

    # Font colors
    font_color = 'black'
    save_button_color = [110, 110, 110]
    back_button_color = [110, 110, 110]

    board = []

    while True:
        for event in pygame.event.get():
            # Quit events
            if event.type == pygame.QUIT:
                sys.exit()
            # Key down events
            if event.type == pygame.KEYDOWN:
                try:
                    if len(name) < 15 and event.key != pygame.K_BACKSPACE and event.unicode != '\r' \
                            and event.key != pygame.K_ESCAPE:
                        name += event.unicode
                        font_color = 'black'
                except KeyError:
                    continue
                finally:
                    if event.key == pygame.K_ESCAPE:
                        return 0
                    if event.key == pygame.K_BACKSPACE:
                        name = [x for x in name]
                        if len(name) > 0:
                            name.pop(-1)
                        name = ''.join(name)
                        font_color = 'black'
                    if event.unicode == '\r':
                        if name in saved:
                            file = open(rf'saves\{name}.txt', 'r')
                            for i in range(60):
                                board.append([x for x in file.readline()[:-1]])
                            file.close()
                            return board, name, True
                        else:
                            font_color = [200, 0, 0]
            # Mouse button down events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 480 < event.pos[0] < 580 and 330 < event.pos[1] < 345:
                    if name in saved:
                        if 'saves' not in os.listdir():
                            os.mkdir('saves')
                        file = open(rf'saves\{name}.txt', 'r')
                        for i in range(60):
                            board.append([x for x in file.readline()[:-1]])
                        file.close()
                        return board, name, True
                    else:
                        font_color = [200, 0, 0]
                if event.button == 1 and 620 < event.pos[0] < 720 and 330 < event.pos[1] < 345:
                    return 0
            # Mouse motion events
            if event.type == pygame.MOUSEMOTION:
                if 480 < event.pos[0] < 580 and 330 < event.pos[1] < 345:
                    save_button_color = [130, 130, 130]
                else:
                    save_button_color = [110, 110, 110]
                if 620 < event.pos[0] < 720 and 330 < event.pos[1] < 345:
                    back_button_color = [130, 130, 130]
                else:
                    back_button_color = [110, 110, 110]

        # Base frame
        pygame.draw.rect(display, [255, 0, 0], [400, 255, 400, 115])
        pygame.draw.rect(display, [255, 255, 255], [405, 260, 390, 105])

        # Writing space
        pygame.draw.rect(display, [150, 150, 150], [430, 285, 340, 30])

        # Buttons
        pygame.draw.rect(display, save_button_color, [480, 330, 100, 15])
        pygame.draw.rect(display, back_button_color, [620, 330, 100, 15])

        # Rendering fonts
        display.blit(medium_font.render(f'{name}|', True, font_color), [430, 287.5])
        display.blit(mini_font.render('LOAD', True, 'black'), [510, 330])
        display.blit(mini_font.render('BACK', True, 'black'), [650, 330])

        # Ending commands
        pygame.display.update()


# Creating empty board
def create(width, height):
    board = [['#' for x in range(width)] for x in range(height)]
    for i in range(height):
        for j in range(width):
            if 0 < i < height - 1 and 0 < j < width - 1:
                board[i][j] = "-"
    return board


# Display editor mode
def editor_interface(assets):
    # Display settings
    display = pygame.display.set_mode([1200, 600])

    # Pseudo global variables for editor interface
    board = create(90, 60)
    name = ''
    loaded = False

    # Fonts
    font = pygame.font.Font(None, 85)

    # Button colors
    load_button_color = [0, 200, 0]
    save_button_color = [250, 200, 0]
    back_button_color = [250, 0, 0]

    while True:
        for event in pygame.event.get():
            # Quit events
            if event.type == pygame.QUIT:
                sys.exit()
            # Key down events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
            # Mouse button down events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 10 < event.pos[0] < 890 and 10 < event.pos[1] < 590:
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if 10 * j < event.pos[0] < 10 * j + 10 and 10 * i < event.pos[1] < 10 * i + 10:
                                if board[i][j] == "+":
                                    board[i][j] = "-"
                                elif board[i][j] == "-":
                                    board[i][j] = "+"
                if event.button == 1 and 930 < event.pos[0] < 1165 and 394 < event.pos[1] < 447:
                    load_button_color = [0, 200, 0]
                    returned = load(display)
                    if returned != 0:
                        board = returned[0]
                        name = returned[1]
                        loaded = returned[2]
                if event.button == 1 and 930 < event.pos[0] < 1165 and 457 < event.pos[1] < 510:
                    save_button_color = [250, 200, 0]
                    save(display, board, name, loaded)
                if event.button == 1 and 930 < event.pos[0] < 1165 and 520 < event.pos[1] < 573:
                    return 0
            # Mouse motion events
            if event.type == pygame.MOUSEMOTION:
                if 930 < event.pos[0] < 1165 and 394 < event.pos[1] < 447:
                    load_button_color = [0, 250, 0]
                else:
                    load_button_color = [0, 200, 0]
                if 930 < event.pos[0] < 1165 and 457 < event.pos[1] < 510:
                    save_button_color = [250, 250, 0]
                else:
                    save_button_color = [250, 200, 0]
                if 930 < event.pos[0] < 1165 and 520 < event.pos[1] < 573:
                    back_button_color = [250, 0, 0]
                else:
                    back_button_color = [200, 0, 0]

        # Filling the area
        display.fill([150, 150, 150])
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "#":
                    display.blit(assets["Block"], [10 * j, 10 * i])
                elif board[i][j] == "+":
                    display.blit(assets["Cell_alive"], [10 * j, 10 * i])
                else:
                    display.blit(assets["Cell_dead"], [10 * j, 10 * i])

        # Drawing buttons
        pygame.draw.rect(display, load_button_color, [930, 394, 235, 53])
        display.blit(font.render("LOAD", True, [0, 0, 0]), [965, 394])

        pygame.draw.rect(display, save_button_color, [930, 457, 235, 53])
        display.blit(font.render("SAVE", True, [0, 0, 0]), [965, 457])

        pygame.draw.rect(display, back_button_color, [930, 520, 235, 53])
        display.blit(font.render("BACK", True, [0, 0, 0]), [965, 520])

        # Ending commands
        pygame.display.update()
