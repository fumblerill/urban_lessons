from time import sleep

class UrTube:
    """Основной класс программы"""
    def __init__(self):
        self.users = [] # Список пользователей
        self.videos = [] # Список видео
        self.current_user = None # Текущий пользователь

    def register(self, nickname, password, age):
        """Метод регистрации пользователя в программе
        Если пользователей в базе нет, то регистрируем нового пользователя,
        если база не пуста, то проверяем существует ли пользователь с таким ником и если нет, то регистрируем"""
        if len(self.users) == 0:
            self.users.append(User(nickname, password, age))
            # print(f'Пользователь {nickname} зарегистрирован')
            self.log_in(nickname, password)
        else:
            for user in self.users:
                if nickname != user.nickname:
                    self.users.append(User(nickname, password, age))
                    # print(f'Пользователь {nickname} зарегистрирован')
                    self.log_in(nickname, password)
                    break
                else:
                    print(f'Пользователь {nickname} уже существует')
                    break

    def log_in(self, nickname, password):
            """Метод авторизации пользователя, сверяем логин и пароль, если совпадают, то производим вход"""
            for user in self.users:
                if nickname == user.nickname and hash(password) == user.password:
                    self.current_user = nickname
                    # print(f'Добро пожаловать {nickname}!')
                    break

            # Если пользователь не найден, выводим об это сообщение
            if self.current_user is None:
                print('Пользователь не найден!')

    def log_out(self):
        """Метод выхода из аккаунта"""
        print(f'Спасибо за посещение нашего сайта, {self.current_user}. Будем рады видеть Вас снова!')
        self.current_user = None

    def add(self, *args):
        """Метод добавления видео в базу"""
        for video in args:
            self.videos.append(video)

    def get_videos(self, word):
        """Метод поиска видео по слову или предложению"""
        result = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        """Метод просмотра видео"""
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if title is video.title:
                    if video.adult_mode is True:
                        for user in self.users:
                            if self.current_user is user.nickname:
                                if user.age >= 18:
                                    for video.time_now in range(video.time_now, video.duration+1):
                                        print(str(video.time_now), end=' ')
                                        video.time_now += 1
                                        # sleep(1)
                                    print('Конец видео')
                                else:
                                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for video.time_now in range(video.time_now, video.duration+1):
                            print(str(video.time_now), end=' ')
                            video.time_now += 1
                            sleep(1)
                            print('Конец видео')
            if title is not video.title:
                print('Видео не найдено!')


class User:
    """Класс пользователя программы"""
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return f'Пользователь: {self.nickname}, пароль: {self.password}, возраст: {self.age}'

class Video:
    """Класс видео"""
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return (f'Название видео: {self.title}'
                f'\nДлительность: {self.duration}'
                f'\nНачало видео с: {self.time_now}'
                f'\nВозрастное ограничение: {self.adult_mode}')

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