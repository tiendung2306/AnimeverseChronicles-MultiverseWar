import pygame

class Nexus():
    def __init__(self, filename):
        self.screen = pygame.display.get_surface()
        self.nexus_surface_original = pygame.image.load(filename)
        self.nexus_surface = self.nexus_surface_original.copy()

        pre_nexus_height = self.nexus_surface.get_rect().height
        pre_nexus_width = self.nexus_surface.get_rect().width
        new_nexus_width = self.screen.get_rect().width // 10
        self.nexus_surface = pygame.transform.smoothscale(self.nexus_surface, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))

        self.total_hp = 1000.0
        self.curr_hp = 1000.0

    def screen_resize(self, filename):
        self.nexus_surface = self.nexus_surface_original.copy()

        pre_nexus_height = self.nexus_surface.get_rect().height
        pre_nexus_width = self.nexus_surface.get_rect().width
        new_nexus_width = self.screen.get_rect().width // 10
        self.nexus_surface = pygame.transform.smoothscale(self.nexus_surface, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))