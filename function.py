import os.path


def get_current_path(file_name: str):
    # current_path будет содержать абсолютный путь до директории, в которой находится текущий файл.
    current_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_path, file_name)

# print(os.path.abspath(__file__))
# print(__file__)
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
