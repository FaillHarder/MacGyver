import pygame


class SoundManager:
    sound = {}

    @classmethod
    def load(cls):
        cls.sound["win"] = pygame.mixer.Sound(
            "ressources/audio/Victory.mp3")
        cls.sound["lose"] = pygame.mixer.Sound(
            "ressources/audio/game_over.mp3")

    @classmethod
    def get(cls, name):
        return cls.sound[name]
