#!/home/igor/PycharmProjects/module_5
# -*- coding: utf-8 -*-
import hashlib
import time



class User:
    """ Класс пользователя, содержащий атрибуты: логин, пароль """
    def __init__(self, username, password, age):
        self.username = username
        self.password = self.hash_password(password)
        self.age = age
    def hash_password(self, password):
        """Хеширование пароля с использованием алгоритма SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()


    def get_ifo(self):
        return self.username, self.password

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return other.username == self.username

class Video:
    """
    Класс видео, содержащий атрибуты: title(заголовок, строка), duration
    (продолжительность, секунды), time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class UrTube:
    """
    Класс UrTube, содержащий атрибуты: users(список объектов User),
    videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, username, password, age):
        for user in self.users:
            if username in user.username:
                print(f"Пользователь {username} уже существует")
                return

        new_user = User (username,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {username} зарегистрирован и вошел в систему')

    def log_out(self):
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.username and password == user.password:
                self.current_user = user

    def add(self, *args):
        for movie in args:
            self.videos.append(movie)

    def get_videos(self, text):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
