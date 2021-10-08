import os
import json

import pygame as pg

with open("config.json") as file:
    config = json.load(file)
BACKGROUND_COLOR = pg.Color(config["background_color"])
VISITED_COLOR = [min(chan+20, 255) for chan in BACKGROUND_COLOR]

class Game:

    def __init__(self, max_width, max_height):
        self.cells = {}
        for value in config["initial_config"]:
            coord = tuple(value)
            self.cells[coord] = Cell(coord)

        self.max_width = max_width
        self.max_height = max_height
        print(max_width, self.max_height )
        print(self.cells)

    def reset(self):
        self.cells = {}

    def __setitem__(self, coord, value):
        self.cells[coord] = value

    def __delitem__(self, coord):
        del self.cells[coord]

    def next_generation(self):
        """ method that build the next generation of the game"""
        new_generation = {}
        for i in range(-10, self.max_width+10):
            for j in range(-10, self.max_height+10):
                # first we need all the cell neighbors
                neighboring_cells = self.__neighbors((i,j))
                # we then need to select the active ones
                alive_cells = {}
                for adjacent_cell in neighboring_cells:
                    if adjacent_cell in self.cells:
                        alive_cells[adjacent_cell] = Cell(adjacent_cell)
                # we check if our cell is dead or alive
                if (i,j) in self.cells:
                    # if it's alive then we'll keep it alive if there 2 or 3
                    # neighbor's alive
                    if len(alive_cells) == 3 or len(alive_cells) == 2:
                        new_generation[(i,j)] = Cell((i,j))
                else:
                    # if it's not then we'll make it alive if there is exectly 3
                    # neighbor's alive
                    if len(alive_cells) == 3:
                        new_generation[(i,j)] = Cell((i,j))
        self.cells = new_generation



    def __neighbors(self, cell):
        """ method that retun the list of neighbors of a cell"""
        return {
                (cell[0]-1, cell[1]-1), (cell[0]-1, cell[1]), (cell[0]-1, cell[1]+1),
                (cell[0], cell[1]-1), (cell[0], cell[1]+1),
                (cell[0]+1, cell[1]-1), (cell[0]+1, cell[1]), (cell[0]+1, cell[1]+1),
        }


class Cell:
    size = (config["cell_size_width"], config["cell_size_height"])

    def __init__(self, coords):
        self.color = pg.Color(config["cell_color"])
        self.rect = pg.Rect((coords[0]*Cell.size[0],coords[1]*Cell.size[1]),
                            Cell.size)
        self.rect.inflate_ip(-2, -2)
        self.age = 0

    def draw(self, surface, background):
        color = [min(chan+self.age, 255) for chan in self.color]
        surface.fill(color, self.rect)
        background.fill(VISITED_COLOR, self.rect)


class App:
    """
    Manages control flow for entire program.
    """

    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.background = pg.Surface(self.screen_rect.size).convert()
        self.background.fill(BACKGROUND_COLOR)
        self.fps = 30
        self.clock = pg.time.Clock()
        self.done = False
        self.cell_w = self.screen_rect.w//Cell.size[0]
        self.cell_h = self.screen_rect.h//Cell.size[1]
        self.game = Game(self.cell_w, self.cell_h)
        self.wrapping = True
        self.generating = False

    def reset(self):
        self.game.reset()
        self.background.fill(BACKGROUND_COLOR)

    def event_loop(self):
        """
        Start and stop generation by pressing spacebar.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.generating = not self.generating
                elif event.key == pg.K_BACKSPACE:
                    self.reset()

    def add_delete(self, mouse):
        mouse_pos = pg.mouse.get_pos()
        coords = mouse_pos[0]//Cell.size[0], mouse_pos[1]//Cell.size[1]
        if mouse[0]:
            self.game[coords] = Cell(coords)
        elif mouse[2]:
            try:
                del (self.game[coords])
            except KeyError:
                pass

    def update(self):
        """
        If generating is True, calculate the next generation of living cells.
        """
        mouse = pg.mouse.get_pressed()
        if any(mouse):
            self.add_delete(mouse)
        elif self.generating:
            self.game.next_generation()

    def render(self):
        """
        Clear the screen and render all living cells.
        """
        self.screen.blit(self.background, (0,0))
        for coord, cell in self.game.cells.items():
            cell.draw(self.screen, self.background)
        pg.display.update()

    def main_loop(self):
        """
        Spin.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(self.fps)

def main():
    """
    Set up our environment; create an App instance; and start our main loop.
    """
    os.environ["SDL_VIDEO_CENTERED"] = "True"
    screen_size = (config["screen_size_width"], config["screen_size_height"])
    pg.init()
    pg.display.set_caption("Game of life")
    pg.display.set_mode(screen_size)
    App().main_loop()
    pg.quit()


if __name__ == "__main__":
    main()
