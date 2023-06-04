import pygame
import os
from .theme import Theme


class Configuration:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.index = 0
        self.theme = self.themes[self.index]

    def change_theme(self):
        self.index += 1
        self.index %= len(self.themes)
        self.theme = self.themes[self.index]

    def _add_themes(self):
        blue = Theme('lightblue', 'darkblue')
        green = Theme('lightgreen', 'darkgreen')
        brown = Theme('white', 'brown')
        pink = Theme('pink', 'white')
        red = Theme('red', 'white')
        #wooden = Theme('burlywood1', 'burntsienna')

        self.themes = [blue, green, brown, pink, red]