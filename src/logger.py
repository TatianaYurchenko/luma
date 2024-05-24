import logging
import os
from logging.handlers import RotatingFileHandler
from function import get_current_path

# создаем папку для логов
def create__logs():
    file_name = "logs.log"
    log_dir = get_current_path("logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    file_path = os.path.join(log_dir, file_name)
    print(file_path)
    return file_path

def get_logger(name:str):
    # Создание лог-файла и определение максимального размера файла:
    # Функция create_logs() создает и возвращает путь к файлу для логирования.
    # Переменная max_byte устанавливает максимальный размер лог-файла на 1 мегабайт.

    log_file = create__logs()
    max_byte = 1 * 1024 * 1024
    # Метод logging.getLogger(name) возвращает логгер с именем name.
    # Если такого логгера еще не существует, он будет создан.
    logger = logging.getLogger(name)
    # Устанавливается уровень логирования DEBUG, что означает, что все сообщения уровней DEBUG и выше
    # (INFO, WARNING, ERROR, CRITICAL) будут записываться.
    logger.setLevel(logging.DEBUG)
    # Создание форматера. Форматер определяет формат лог-сообщений.
    # В данном случае сообщения будут содержать уровень логирования, временную метку, само сообщение и имя логгера.
    formatter = logging.Formatter(
        fmt="%(levelname)s | %(asctime)s | %(message)s | file: %(name)s | %(lineno)d",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    #  Создание обработчика с ротацией файлов:
    #  Обработчик RotatingFileHandler записывает лог-сообщения в файл. Когда размер файла достигает maxBytes (1 МБ),
    #  создается новый файл, а старые файлы сохраняются в резервных копиях (до 10 копий).
    handler = logging.handlers.RotatingFileHandler(
        filename=log_file,
        encoding='utf-8',
        maxBytes=max_byte,
        backupCount=10
    )
    #  Применение форматера к обработчику:
    handler.setFormatter(formatter)
    # Добавление консольного обработчика к логгеру
    logger.addHandler(handler)
    return logger
#  Пример использования метода:
logger = get_logger('my_logger')
logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
