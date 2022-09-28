import pygame
import game
import editor


def main():
    # Loading assets
    assets = {"Cell_alive": pygame.image.load("Assets/cell_alive.png"),
              "Cell_dead": pygame.image.load("Assets/cell_dead.png"),
              "Block": pygame.image.load("Assets/Block.png")}

    # Pseudo global variables
    choice = editor.create(90, 60)
    base_choice = choice
    generation = 1
    mode = "Manual"
    name = 'No chosed'

    # Base display settings
    display = pygame.display.set_mode([1200, 600])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Conway's Game of Life")
    pygame.time.set_timer(1, 100)

    # Fonts
    higher_font = pygame.font.Font(None, 85)
    lower_font = pygame.font.Font(None, 30)

    # Button colors
    reset_button_color = [0, 100, 255]
    load_button_color = [0, 200, 0]
    edit_button_color = [200, 100, 0]

    running = True
    while running:
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                running = False
            # Key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and mode == 'Manual':
                    choice = game.next_generation(choice)
                    generation += 1
                if event.unicode == '\r':
                    mode = 'Manual' if mode == 'Auto' else 'Auto'
            # Mouse buttons events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 930 < event.pos[0] < 1165 and 520 < event.pos[1] < 573:
                    edit_button_color = [200, 100, 0]
                    editor.editor_interface(assets)
                if event.button == 1 and 930 < event.pos[0] < 1165 and 457 < event.pos[1] < 510:
                    load_button_color = [0, 200, 0]
                    returned = editor.load(display)
                    if returned != 0:
                        choice = returned[0]
                        base_choice = returned[0]
                        name = returned[1]
                        mode = 'Manual'
                        generation = 1
                if event.button == 1 and 930 < event.pos[0] < 1165 and 394 < event.pos[1] < 457:
                    choice = base_choice
                    generation = 1
                    mode = 'Manual'
            # Mouse motion events
            if event.type == pygame.MOUSEMOTION:
                if 930 < event.pos[0] < 1165 and 394 < event.pos[1] < 447:
                    reset_button_color = [0, 150, 255]
                else:
                    reset_button_color = [0, 100, 255]
                if 930 < event.pos[0] < 1165 and 457 < event.pos[1] < 510:
                    load_button_color = [0, 250, 0]
                else:
                    load_button_color = [0, 200, 0]
                if 930 < event.pos[0] < 1165 and 520 < event.pos[1] < 573:
                    edit_button_color = [200, 150, 0]
                else:
                    edit_button_color = [200, 100, 0]
            # Generation changer
            if event.type == 1 and mode == "Auto":
                choice = game.next_generation(choice)
                generation += 1

        # Filling the arena with cells
        display.fill([150, 150, 150])
        for i in range(len(choice)):
            for j in range(len(choice[i])):
                if choice[i][j] == "#":
                    display.blit(assets["Block"], [10 * j, 10 * i])
                elif choice[i][j] == "+":
                    display.blit(assets["Cell_alive"], [10 * j, 10 * i])
                else:
                    display.blit(assets["Cell_dead"], [10 * j, 10 * i])

        # Drawing info
        display.blit(lower_font.render(f"Generation: {generation}", True, [0, 0, 0]), [905, 100])
        display.blit(lower_font.render(f"Mode[A]: {mode}", True, [0, 0, 0]), [905, 120])

        display.blit(lower_font.render(f'{name}', True, [0, 0, 0]), [915, 30])
        display.blit(lower_font.render("Board's name:", True, [0, 0, 0]), [915, 10])

        # Drawing buttons
        pygame.draw.rect(display, reset_button_color, [930, 394, 235, 53])
        display.blit(higher_font.render("RESET", True, [0, 0, 0]), [950, 394])

        pygame.draw.rect(display, load_button_color, [930, 457, 235, 53])
        display.blit(higher_font.render("LOAD", True, [0, 0, 0]), [965, 457])

        pygame.draw.rect(display, edit_button_color, [930, 520, 235, 53])
        display.blit(higher_font.render("EDITOR", True, [0, 0, 0]), [930, 520])

        # Ending commands
        clock.tick_busy_loop(60)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
