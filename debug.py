import pygame 


class Debug():
    def __init__(self, screen):
        self.status = False#
        self.font = pygame.font.SysFont("Arial", 36)
        self.screen = screen

    def displayFps(self, fps):
        if self.status:
            print("Debugging")
            text = self.font.render(fps, True, (255,255,255))
            self.screen.blit(text, (200 - text.get_width() // 2, 150 - text.get_height() // 2))

    def update(self, fps):
        self.displayFps(fps)
