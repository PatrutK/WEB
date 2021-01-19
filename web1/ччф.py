def human_read_format(size):
    formats = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    n = 0
    while size >= 1024:
        size /= 1024
        n += 1
    return str(round(size)) + formats[n]
