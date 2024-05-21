from pygame import *
init()
ARIAL_50 = font.SysFont('arial', 50)


class Menu:
    def __init__(self):
        self._option_surfaces_ = []
        self._callback_ = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces_.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callback_.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction,
                                                len(self._option_surfaces_) - 1))

    def select(self):
        self._callback_[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces_):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)





