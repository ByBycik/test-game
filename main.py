import pygame
from pygame.locals import QUIT

import sys
from typing import Union, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from pygame import Surface


class Mainloop:
    def __init__(
            self, 
            __screen_size: tuple[int, int] = (1000, 600), 
            target_fps: Union[int, float] = 144, 
            background_color: Union[str, tuple[int, int, int]] = "#303030"
    ) -> None:
        self.__display = pygame.display.set_mode(__screen_size)
        self.__clock = pygame.time.Clock()
        
        self.__is_working = True

        self.target_fps = target_fps
        self.background_color = background_color
    
    def break_mainloop(self) -> None:
        self.__is_working = False
        pygame.quit()
        sys.exit()
    
    def __update_display(self) -> None:
        self.__display.fill(self.background_color)
        pygame.display.update()
        self.__clock.tick(float(self.target_fps))

    def __update_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.break_mainloop()
    
    def mainloop(self) -> None:
        while self.__is_working:

            self.__update_events()
            self.__update_display()
            print(self.__clock.get_fps())


if __name__ == "__main__":
    mainloop = Mainloop()
    mainloop.mainloop()
