import os


def get_files_sizes():
    for file in os.listdir():
        if os.path.isfile(file):
            print(file, human_read_format(os.path.getsize(file)))


def human_read_format(size):
    formats = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    n = 0
    while size >= 1024:
        size /= 1024
        n += 1
    return str(round(size)) + formats[n]


get_files_sizes()
