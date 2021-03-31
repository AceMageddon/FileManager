import os
import shutil

print('Ввод команды:')
text = input()
text = text.split(' ')
root = 'C:/'
count = 0
while text[0] != 'stop':
    if count > 0:
        print('Ввод команды:')
        text = input()
        text = text.split(' ')

    def mkdir():
        path = text[1]
        os.mkdir(path)

    def rmdir():
        path = text[1]
        os.rmdir(path)

    def chdir():
        path = text[1]
        os.chdir(path)

    def getcwd():
        root = os.getcwd()
        print(root)

    def create():
        f = open(text[1], 'w')
        f.write('')
        f.close()

    def write():
        f = open(text[1], 'w')
        f.write(input())
        f.close()

    def read():
        f = open(text[1], 'r')
        print(*f)
        f.close()

    def remove():
        os.remove(text[1])

    def copy():
        shutil.copy(text[1], text[2])

    def move():
        shutil.move(text[1], text[2])

    def rename():
        os.rename(text[1], text[2])


    if (text[0] != 'getcwd') and (text[0] != 'stop'):
        if(text[1][0] != 'C') and (text[1][0] != ':') and (text[1][0] != '/'):
         text[1] = root + '/' + text[1]

    if text[0] == 'getcwd':
        print('Текущая директория:')
        getcwd()
        print('')

    if text[0] == 'move':
        print('Файл ' + text[1] + ' перемещён в папку ' + text[2])
        move()
        print('')

    if text[0] == 'rename':
        print('Файл ' + text[1] + ' переименован в ' + text[2])
        rename()
        print('')

    if text[0] == 'copy':
        print('Файл ' + text[1] + ' копирован в папку ' + text[2])
        copy()
        print('')

    if text[0] == 'remove':
        print('Файл ' + text[1] + ' удалён')
        remove()
        print('')

    if text[0] == 'create':
        print('Создан файл ' + text[1])
        create()
        print('')

    if text[0] == 'read':
        print('Прочтён файл ' + text[1])
        read()
        print('')

    if text[0] == 'write':
        write()
        print('Написан текст в файл ' + text[1])
        print('')

    if text[0] == 'mkdir':
        mkdir()
        print('Директория ' + text[1] + ' создана.')
        print('')

    if text[0] == 'rmdir':
        rmdir()
        print('Директория ' + text[1] + ' удалена.')
        print('')

    if text[0] == 'chdir':
        chdir()
        root = text[1]
        print(os.getcwd())
        print('')

    else:
        print('')
    count += 1
