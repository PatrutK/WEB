from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for el in myzip.filelist:
        name = el.filename
        if name[-1] == '/':
            print(' ' * name.count('/') + name.split('/')[-2])
        else:
            print(' ' * name.count('/') + name.split('/')[-1])
