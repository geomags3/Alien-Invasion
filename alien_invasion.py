import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

import game_functions as gf


#еще одно изменение для Git (создание новой ветки)

def run_game():

    # Инициализирует игру и создает объект на экране
    pygame.init()  # Инициализирует настройки, необходимые Pygame для работы
    ai_settings = Settings()  # Создаем объект класса настроек

    # Создает проверхность размером 1200 на 800 пискселей
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()
    aliens = Group()

    # Создание пришельца
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры
    while True:
        # Обрабатывает нажатия клавиш и событий мыши
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Обновляет позицию корабля
            ship.update()
            # Обновляет позиции пуль и удаляет старые пули
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Обновляет позиции пришельцев
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Обновляет изображения на экране и отображает новый экран
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()
