import pygame
from pygame.locals import *
from screen import *
from color import *
from states import *

class tutorials():
    def __init__(self):
        self.font_size = 36
        self.font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', self.font_size)
        self.color = Black

        self.button_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)
        self.buttons_color = Navy

        self.text = "Thang nao co tien\nThi nap tien vao donate cho tao\nIt thi 5 qua trung\nNhieu thi 1 qua ten lua"

        self.bank_qr_original = pygame.image.load('GameplayAssets\\BankQR.png')

        self.load()

    def load(self):
        self.text_display = self.font.render(self.text, True, self.color)
        self.text_display_rect = self.text_display.get_rect()
        self.text_display_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 2.0)

        self.back_button = self.button_font.render('Back', True, self.buttons_color)
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 5.0 * 4.0)

        self.bank_qr = self.bank_qr_original.copy()
        self.bank_qr = pygame.transform.smoothscale(self.bank_qr, (screen.screen.get_rect().width / 5, self.bank_qr.get_rect().height / (self.bank_qr.get_rect().width / (screen.screen.get_rect().width / 5))))
        self.bank_qr_rect = self.bank_qr.get_rect()
        self.bank_qr_rect.center = (screen.screen.get_rect().width / 5.0 * 4.0, screen.screen.get_rect().height / 2)

    def check_click(self, mouse):
        if self.back_button_rect.left <= mouse[0] <= self.back_button_rect.right and self.back_button_rect.top <= mouse[1] <= self.back_button_rect.bottom:
            State.curr_state = State.states[0]

    def update(self):
        self.print_multiline(screen.screen.get_rect().width / 2.5, screen.screen.get_rect().height / 2.5, self.font, self.text, self.color, self.font_size)
        screen.screen.blit(self.back_button, self.back_button_rect)
        screen.screen.blit(self.bank_qr, self.bank_qr_rect)

    def print_multiline(self, posX, posY, font, text : str, fontColour, fontsize):
        # posX = (screen.screen.get_rect().width * 1/8)
        # posY = (screen.screen.get_rect().height * 1/8)
        position = posX, posY
        tmp_text = text.splitlines()
        label = []
        for line in tmp_text: 
            label.append(font.render(line, True, fontColour))
        for line in range(len(label)):
            screen.screen.blit(label[line],(position[0],position[1]+(line*fontsize)+(15*line)))

    def screen_resize(self):
        self.load()