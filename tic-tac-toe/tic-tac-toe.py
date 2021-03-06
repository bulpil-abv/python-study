import pygame
from enum import Enum

CELL_SIZE = 50
FPS = 60


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Player class with type of sign and
    name
    """

    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameRoundManager:
    """
    Game manager, who stars all processes
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        print("click_handled", i, j)


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameFieldView:
    """
    Widget of the field which finds the place of click
    """

    def __init__(self, field):
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True  # TODO

    def get_coords(self, x, y):
        return 0, 0  # TODO


class GameWindow:

    def __init__(self):
        pygame.init()

        self._width = 800
        self._height = 600
        self._title = "Tic Tac Toe"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # self._field_widget = GameFieldView()
        player1 = Player("Petya", Cell.CROSS)
        player2 = Player("Vasya", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                    self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print("Game over!")


if __name__ == "__main__":
    main()
