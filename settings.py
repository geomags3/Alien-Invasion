
class Settings():
    """Класс хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 10  # скорость снижения флота

        # Темп ускорения игры
        self.speedup_scale = 2
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1  # скорость бокового передвижения флота

        self.fleet_direction = 1  # fleet_direction = 1 - движение флота вправо; -1 - влево

        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)