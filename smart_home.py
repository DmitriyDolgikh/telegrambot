import telebot

from database import Database
from status import status


class SmartHomeBot:
    def __init__(self, token, db_name):
        self.bot = telebot.TeleBot(token)
        self.db = Database(db_name)

    def start(self, message):
        # Регистрация и авторизация пользователя
        user_id = message.from_user.id
        username = message.from_user.username
        user = self.db.get_user(user_id)
        if not user:
            self.db.register_user(user_id, username)

    def show_device_status(self):
        # Показать текущее состояние устройств в умном доме
        home_status = f"Температура: {status.temperature}C\n" \
                      f"Статус sds: {status.door_status}\n" \
                      f"Статус окон: {status.window_status}\n" \
                      f"Статус света: {status.light_status}"

    def control_device(self, message):
        # Управление устройствами в умном доме (например, свет, термостат)
        pass
    def create_automation(self, message):
        # Создание сценариев автоматизации (например, включение света при открытии двери)
        pass
    def schedule_device_control(self, message):
        # Возможность управления устройствами по расписанию
        pass
