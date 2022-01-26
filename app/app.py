from crypt import methods
from flask import Flask, render_template, request
from flask.json import jsonify
import numpy
import math
import random
import numpy.random
import itertools
import re
import copy
import collections
from math import gcd

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lab2')
def lab2():
    return render_template('lab2.html')


@app.route('/lab3')
def lab3():
    return render_template('lab3.html')


@app.route('/decodeLab3', methods=['GET'])
def decodeLab3():
    enc_text = request.args.get('enc_text') # здесь зашифрованный текст в виде чисел из js
    arr_mat = request.args.get('arr_mat')  # здесь матрица-код из js
    arr_mat = arr_mat.split(',')
    if len(arr_mat) == 9:
        arr_tchk_zpt = ' '.join(
            arr_mat[:3]) + '; ' + ' '.join(arr_mat[3:6]) + '; ' + ' '.join(arr_mat[6:]) # привожу к виду, чтобы библиотека питона numpy "съела" мою матрицу и представила в виде себе-понятной матрицы
        matrix_numpy = numpy.matrix(arr_tchk_zpt) # здесь происходит преобразование в матрицу вида numpy
        opredelitel = numpy.linalg.det(matrix_numpy) # нахожу определитель
        if opredelitel == 0: # если определитель равен нулю, то матрица вырожденная, выводим ошибку
            return jsonify('error')
        else:
            obratnaya = numpy.linalg.inv(matrix_numpy) # чтобы произвести расшифровку нужно обратную матрицу умножить на массив зашифрованный чисел. Обратную матрицу также получаем с помощью библиотеки numpy.
            enc_text = enc_text.split(',')
            print(obratnaya)
            # print(len(enc_text))
            obratnaya_to_list = obratnaya.tolist() # привожу элементы обратной матрицы к удобному мне для работы виду - каждый ее элемент в отдельную переменную
            a1 = obratnaya_to_list[0][0]
            a2 = obratnaya_to_list[0][1]
            a3 = obratnaya_to_list[0][2]
            b1 = obratnaya_to_list[1][0]
            b2 = obratnaya_to_list[1][1]
            b3 = obratnaya_to_list[1][2]
            c1 = obratnaya_to_list[2][0]
            c2 = obratnaya_to_list[2][1]
            c3 = obratnaya_to_list[2][2]
            #  for(i=0; i<=indexes_orig_word.length - 3; i=i+3){
            decrypted_indexes = []
            for i in range(0, len(enc_text) - 2, 3):
                # print(a1 * int(enc_text[i]))
                # print('----------------------')
                summa1 = int(
                    round(a1 * int(enc_text[i]) + a2 * int(enc_text[i+1]) + a3 * int(enc_text[i+2]))) # произвожу умножение элементов обратной матрицы на зашифрованные элементы. округляю их, так как в обратной матрице элементы не целые
                summa2 = int(
                    round(b1 * int(enc_text[i]) + b2 * int(enc_text[i+1]) + b3 * int(enc_text[i+2])))
                summa3 = int(
                    round(c1 * int(enc_text[i]) + c2 * int(enc_text[i+1]) + c3 * int(enc_text[i+2])))
                # print(int(round(a1, '*', int(enc_text[i]))))
                # summa2 = int(round(b1 * int(enc_text[i]))) + int(round(b2 * int(enc_text[i+1]))) + int(round(b3 * int(enc_text[i+2])))
                # summa3 = int(round(c1 * int(enc_text[i]))) + int(round(c2 * int(enc_text[i+1]))) + int(round(c3 * int(enc_text[i+2])))
                decrypted_indexes.append(summa1) # здесь умножение каждой из 3-х строк записываю в один массив
                decrypted_indexes.append(summa2)
                decrypted_indexes.append(summa3)
                # print(i)
            print(decrypted_indexes)
            return jsonify(decrypted_indexes)
    else:
        arr_tchk_zpt = ' '.join(arr_mat[:4]) + '; ' + ' '.join( # привожу к виду, чтобы библиотека питона numpy "съела" мою матрицу и представила в виде себе-понятной матрицы
            arr_mat[4:8]) + '; ' + ' '.join(arr_mat[8:12]) + '; ' + ' '.join(arr_mat[12:])
        matrix_numpy = numpy.matrix(arr_tchk_zpt) # здесь происходит преобразование в матрицу вида numpy
        opredelitel = numpy.linalg.det(matrix_numpy) # нахожу определитель
        if opredelitel == 0:
            return jsonify('error') # если определитель равен нулю, то матрица вырожденная, выводим ошибку
        else:
            obratnaya = numpy.linalg.inv(matrix_numpy) # чтобы произвести расшифровку нужно обратную матрицу умножить на массив зашифрованный чисел. Обратную матрицу также получаем с помощью библиотеки numpy.
            enc_text = enc_text.split(',')
            print(obratnaya)
            # print(len(enc_text))
            obratnaya_to_list = obratnaya.tolist() # привожу элементы обратной матрицы к удобному мне для работы виду - каждый ее элемент в отдельную переменную
            a1 = obratnaya_to_list[0][0]
            a2 = obratnaya_to_list[0][1]
            a3 = obratnaya_to_list[0][2]
            a4 = obratnaya_to_list[0][3]
            b1 = obratnaya_to_list[1][0]
            b2 = obratnaya_to_list[1][1]
            b3 = obratnaya_to_list[1][2]
            b4 = obratnaya_to_list[1][3]
            c1 = obratnaya_to_list[2][0]
            c2 = obratnaya_to_list[2][1]
            c3 = obratnaya_to_list[2][2]
            c4 = obratnaya_to_list[2][3]
            d1 = obratnaya_to_list[3][0]
            d2 = obratnaya_to_list[3][1]
            d3 = obratnaya_to_list[3][2]
            d4 = obratnaya_to_list[3][3]
            decrypted_indexes = []
            for i in range(0, len(enc_text) - 2, 4):
                summa1 = int(round(a1 * int(enc_text[i]) + a2 * int( # произвожу умножение элементов обратной матрицы на зашифрованные элементы. округляю их, так как в обратной матрице элементы не целые
                    enc_text[i+1]) + a3 * int(enc_text[i+2]) + a4 * int(enc_text[i+3])))
                summa2 = int(round(b1 * int(enc_text[i]) + b2 * int(
                    enc_text[i+1]) + b3 * int(enc_text[i+2]) + b4 * int(enc_text[i+3])))
                summa3 = int(round(c1 * int(enc_text[i]) + c2 * int(
                    enc_text[i+1]) + c3 * int(enc_text[i+2]) + c4 * int(enc_text[i+3])))
                summa4 = int(round(d1 * int(enc_text[i]) + d2 * int(
                    enc_text[i+1]) + d3 * int(enc_text[i+2]) + d4 * int(enc_text[i+3])))
                decrypted_indexes.append(summa1) # здесь умножение каждой из 4-х строк записываю в один массив
                decrypted_indexes.append(summa2)
                decrypted_indexes.append(summa3)
                decrypted_indexes.append(summa4)
            print(decrypted_indexes)
            return jsonify(decrypted_indexes)


@app.route('/playfairEncode', methods=['GET'])
def playfairEncode():
    text = request.args.get('text')
    key = request.args.get('key')
    alphabet_lower = ['а', 'б', 'в', 'г', 'д',
                      'е', 'ж', 'з', 'и', 'к',
                      'л', 'м', 'н', 'о', 'п',
                      'р', 'с', 'т', 'у', 'ф',
                      'х', 'ц', 'ч', 'ш', 'щ',
                      'ь', 'ы', 'э', 'ю', 'я']

    ### здесь идет проверка на то, какие буквы из алфавита есть в ключе, а какие  - нет. Алфавит сначала заполняется кодовым словом, а потом весь оставшийся исходный алфавит без повтора букв из кодового слова.
    new_alphabet = []  
    for i in range(len(key)):
        new_alphabet.append(key[i]) 
    for i in range(len(alphabet_lower)):
        bool_buff = False 
        for j in range(len(key)):
            if alphabet_lower[i] == key[j]: # Если символ ключа = символ алфавита
                bool_buff = True
                break
        if bool_buff == False: # Если символ ключа != символ алфавита
            new_alphabet.append(alphabet_lower[i])  
    ###

    ### Формируем матричный алфавит на основе того, что получили выше
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            # Добавляем букву в матрицу
            mtx_abt_i.append(new_alphabet[counter])
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print('\n'.join(map(str, mtx_abt_j))) # отображение полученной таблицы в консоли
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    ###

    ### Шифруем
    enc_text = ""  
    for t in range(0, len(text), 2): # перемещаемся по биграммам исходного текста и ищем совпадения биграм: на строке, в столбце, в диагоналях
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5): # двигаемся по строкам алфавита
            if flag == False:
                break
            for i_1 in range(6): # двигаемся по столбцам алфавита
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t+1]:
                                # Если буквы по диагонали, то меням буквы на буквы из противоположных "углов"
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_2] + \
                                        mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке, то меняем их на стоящие справа
                                elif j_1 == j_2 and i_1 != i_2:
                                    # %6 для предотвращения выхода за строку
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][(i_1+1) % 6] + \
                                        mtx_abt_j[j_2][(i_2+1) % 6]
                                # Если буквы в одном столбце, то меняем на те, что стоят прямо снизу
                                elif j_1 != j_2 and i_1 == i_2:
                                    # %5 для предотвращения выхода за столбец
                                    enc_text = enc_text + \
                                        mtx_abt_j[(j_1+1) % 5][i_1] + \
                                        mtx_abt_j[(j_2+1) % 5][i_2]
                                # Если буквы совпадают, то эта буква записывается дважды
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_1] + \
                                        mtx_abt_j[j_1][i_1]
                                flag = False
                                break
    print("\n Зашифрованный текст = {} \n".format(enc_text))
    return jsonify(enc_text)
    ###

@app.route('/playfairDecode', methods=['GET'])
def playfairDecode():
    text = request.args.get('text')
    key = request.args.get('key')
    alphabet_lower = ['а', 'б', 'в', 'г', 'д',
                      'е', 'ж', 'з', 'и', 'к',
                      'л', 'м', 'н', 'о', 'п',
                      'р', 'с', 'т', 'у', 'ф',
                      'х', 'ц', 'ч', 'ш', 'щ',
                      'ь', 'ы', 'э', 'ю', 'я']

    ### здесь идет проверка на то, какие буквы из алфавита есть в ключе, а какие  - нет. Алфавит сначала заполняется кодовым словом, а потом весь оставшийся исходный алфавит без повтора букв из кодового слова.
    new_alphabet = []  
    for i in range(len(key)):
        new_alphabet.append(key[i])  
    for i in range(len(alphabet_lower)):
        bool_buff = False  
        for j in range(len(key)):
            if alphabet_lower[i] == key[j]:
                bool_buff = True
                break
        if bool_buff == False:  
            new_alphabet.append(alphabet_lower[i])  
    ###

    ### Формируем матричный алфавит на основе того, что получили выше
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            # Добавляем букву в матрицу
            mtx_abt_i.append(new_alphabet[counter])
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    ###

    # Расшифровываем
    enc_text = ""
    for t in range(0, len(text), 2):
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5): # двигаемся по строкам алфавита
            if flag == False:
                break
            for i_1 in range(6): # двигаемся по столбцам алфавита
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t+1]:
                                # Если буквы по диагонали, то меням буквы на буквы из противоположных "углов"
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_2] + \
                                        mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке, то меняем их на стоящие слева
                                elif j_1 == j_2 and i_1 != i_2:
                                    # %6 для предотвращения выхода за строку
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][(i_1-1) % 6] + \
                                        mtx_abt_j[j_2][(i_2-1) % 6]
                                # Если буквы в одном столбце, то меняем их на стоящие сверху
                                elif j_1 != j_2 and i_1 == i_2:
                                    # %5 для предотвращения выхода за столбец
                                    enc_text = enc_text + \
                                        mtx_abt_j[(j_1-1) % 5][i_1] + \
                                        mtx_abt_j[(j_2-1) % 5][i_2]
                                # Если буквы совпадают
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_1] + \
                                        mtx_abt_j[j_1][i_1]
                                flag = False
                                break
    print("\n Расшифрованный текст = {}\n ".format(enc_text))
    return jsonify(enc_text)



@app.route('/lab4')
def lab4():
    return render_template('lab4.html')


@app.route('/encodeLab4', methods=['GET'])
def encodeLab4():
    ot = request.args.get('orig_text')  # получил исходный текст
    key = request.args.get('key')  # здесь ключ

    ot_len = float(len(ot))  # длина исходного текста
    ot_lst = list(ot)  # из букв исходного текста делаю список
    key_lst = sorted(list(key))# расставляю буквы в ключе в порядке возрастания

    print(key_lst)

    col = len(key) # количество столбцов в таблице шифра равно кол-ву символов в ключе

    row = int(math.ceil(ot_len / col)) # узнаем кол-во строк путем деления длины всего сообщения на кол-во столбцов с округ. вверх
    fill_null = int((row * col) - ot_len) # так как округляли в бОльшую сторону, вероятно останутся пробелы в таблице, находим их кол-во
    ot_lst.extend('_' * fill_null) # добавляем столько прочерков, сколько осталось пустых ячеек таблицы


    matrix = [ot_lst[i: i + col] for i in range(0, len(ot_lst), col)] # сделали двойной массив (матрицу) шифрования
    cipher = ""
    k_indx = 0
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx]) # узнаём, индекс буквы в исходном неупорядоченном ключе из буквы упорядоченного списка.
        cipher += ''.join([row[curr_idx] for row in matrix]) # пишем в правильном порядке части исходного текста порционно(в соответствии с порядком столбца)
        k_indx += 1 # счетчик
    return jsonify(cipher)


@app.route('/decodeLab4', methods=['GET'])
def decodeLab4():
    cipher = request.args.get('enc_text') # зашифрованный текст
    key = request.args.get('key') # ключ

    msg = "" # расшифрованный текст

    msg_len = float(len(cipher)) # узеаем длину зашифрованного сообщения
    msg_lst = list(cipher) # делаем список из зашифрованного сообщения

    col = len(key) # кол-во столбцов равно длине ключа

    row = int(math.ceil(msg_len / col)) # узнаем кол-во строк путем деления длины всего сообщения на кол-во столбцов с округ. вверх

    key_lst = sorted(list(key)) # расставляю буквы в ключе в порядке возрастания

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col] # заполняем пустыми значениями построчно для дальнейшей работы
    
    print(dec_cipher)

    k_indx = 0
    msg_indx = 0
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx]) # узнаём, индекс буквы в исходном неупорядоченном ключе из буквы упорядоченного списка.
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] # в соответствии с нужным по очереди порядком заполняем каждый столбец построчно
            msg_indx += 1
        k_indx += 1

    null_count = msg.count('_') # считаем кол-во пропусков

    if null_count > 0:
        return msg[: -null_count] # если пропуски есть., то возвращаем все кроме них

    msg = ''.join(sum(dec_cipher, [])) # возвращаем строку из итогового списка

    return jsonify(msg.replace('_', ''))


################## ГЕНЕРАТОР КАРДАНО

class Cardan(object):
    def __init__(self, size, spaces):
        self.size = int(size)
        self.spaces = str(spaces)
        self.spaces = self.spaces.replace("[", '')
        self.spaces = self.spaces.replace("]", '')
        self.spaces = self.spaces.replace("(", '')
        self.spaces = self.spaces.replace(")", '')
        self.spaces = self.spaces.replace(",", '')
        self.spaces = self.spaces.replace(" ", '')
        matricespaces = []
        i = 0
        cont = 0
        while i < self.size*self.size/4:
            t = int(self.spaces[cont]), int(self.spaces[cont + 1])
            cont = cont + 2
            i = i+1
            matricespaces.append(t)
        self.spaces = matricespaces

    def encode(self, message):
        offset = 0
        encoded_mes = ""
       #создаем массив из ячеек для хранения букв
        matrice = []
        for i in range(self.size*2-1):
            matrice.append([])
            for j in range(self.size):
                matrice[i].append(None)
        whitesneeded = self.size*self.size - \
            len(message) % (self.size*self.size)
        if (len(message) % (self.size*self.size) != 0):
            for h in range(whitesneeded):
                message = message + ' '
        while offset < len(message):
            self.spaces.sort()
            for i in range(int(self.size*self.size//4)):
                xy = self.spaces[i]
                x = xy[0]
                y = xy[1]
                matrice[x][y] = message[offset]
                offset = offset + 1
            if (offset % (self.size*self.size)) == 0:
                for i in range(self.size):
                    for j in range(self.size):
                        encoded_mes = encoded_mes + matrice[i][j]
            for i in range(self.size*self.size//4):
                x = (self.size-1)-self.spaces[i][1]
                y = self.spaces[i][0]
                self.spaces[i] = x, y
        return encoded_mes


    def decode(self, message, size):
        decoded_msg = ""
        offset = 0
        matrice = []
        for i in range(self.size*2-1):
            matrice.append([])
            for j in range(self.size):
                matrice[i].append(None)
        whitesneeded = self.size*self.size - \
            len(message) % (self.size*self.size)
        if (len(message) % (self.size*self.size) != 0):
            for h in range(whitesneeded):
                message = message + ' '
        offsetmsg = len(message) - 1
        while offset < len(message):
            if (offset % (self.size*self.size)) == 0:
                for i in reversed(list(range(self.size))):
                    for j in reversed(list(range(self.size))):
                        matrice[i][j] = message[offsetmsg]
                        offsetmsg = offsetmsg - 1
            for i in reversed(list(range(self.size*self.size//4))):
                x = self.spaces[i][1]
                y = (self.size-1)-self.spaces[i][0]
                self.spaces[i] = x, y
            self.spaces.sort(reverse=True)
            for i in range(self.size*self.size//4):
                xy = self.spaces[i]
                x = xy[0]
                y = xy[1]
                decoded_msg = matrice[x][y] + decoded_msg
                offset = offset + 1

        return decoded_msg


###################  ГЕНЕРАТОР КАРДАНО КОНЕЦ

@app.route('/encodeLab41', methods=['GET'])
def decodeLab41():
    ot = request.args.get('orig_text')  # получил исходный текст
    n = len(ot) # длина исходного текста
    check = request.args.get('check')
    if check == '1':
        print(ot)
        gaps = [(7, 7), (6, 0), (5, 0), (4, 0), (7, 1), (1, 1), (1, 2), (4, 1),
                (7, 2), (2, 1), (2, 5), (2, 3), (7, 3), (3, 1), (3, 2), (3, 4)] # обозначаем вырезы в решетке
        r = Cardan(8, gaps) # делаю "r" объектом класса Cardan, у которого размер 8 и указанные в gaps вырезы
        enc_text = r.encode(ot)
        return jsonify(enc_text)
    else:
        gaps = [(7, 7), (6, 0), (5, 0), (4, 0), (7, 1), (1, 1), (1, 2), (4, 1),
                (7, 2), (2, 1), (2, 5), (2, 3), (7, 3), (3, 1), (3, 2), (3, 4)] # обозначаем вырезы в решетке
        r = Cardan(8, gaps)
        enc_text = r.encode(ot)
        return jsonify(r.decode(enc_text, n))


@app.route('/lab5')
def lab5():
    return render_template('lab5.html')

##################  БЛОКНОТ ШЕННОНА
    
@app.route('/lab5bloknotEnc', methods=['GET'])
def lab5bloknotEnc():
    msg = request.args.get('msg')
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_lower = {}
    i = 0
    while i < (len(alphabet)):
        alphabet_lower.update({alphabet[i]: i}) # создается словарь где ключ - буква, значение - индекс
        i += 1
    msg = request.args.get('msg')
    msg_list = list(msg)
    msg_list_len = len(msg_list)
    msg_code_bin_list = list()
    for i in range(len(msg_list)):
        msg_code_bin_list.append(alphabet_lower.get(msg_list[i]))

    key_list = list()
    for i in range(msg_list_len):
        key_list.append(random.randint(0, 32))

    cipher_list = list()
    for i in range(msg_list_len):
        m = int(msg_code_bin_list[i])
        k = int(key_list[i])
        cipher_list.append(int(bin(m ^ k), base=2))
    return jsonify(cipher_list, key_list)

@app.route('/lab5bloknotDecode', methods=['GET'])
def lab5bloknotDecode():
    msg = request.args.get('msg')
    msg = msg.split(',')
    key_list = request.args.get('key_list')
    key_list = key_list.split(',')
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_lower = {}
    i = 0
    while i < (len(alphabet)):
        alphabet_lower.update({alphabet[i]: i})
        i += 1
    decipher_list = list()
    msg_list_len = len(msg)
    for i in range(msg_list_len):
        c = int(msg[i])
        k = int(key_list[i])
        decipher_list.append(int(bin(c ^ k), base=2))
    deciphered_str = ""
    for i in range(len(decipher_list)):
        deciphered_str += get_key(alphabet_lower, decipher_list[i])
    return jsonify(deciphered_str)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

##################  БЛОКНОТ ШЕННОНА конец

##################  ГОСТ 28147-89

class GostCrypt(object):
    def __init__(self, key, sbox):
        self._key = None
        self._subkeys = None
        self.key = key
        self.sbox = sbox

    @staticmethod
    def _bit_length(value):
        return len(bin(value)[2:])

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        self._subkeys = [(key >> (32 * i)) & 0xFFFFFFFF for i in range(8)] #8 кусков


    def _f(self, part, key):
        temp = part ^ key
        output = 0
        for i in range(8):
            output |= ((self.sbox[i][(temp >> (4 * i)) & 0b1111]) << (4 * i))
        return ((output >> 11) | (output << (32 - 11))) & 0xFFFFFFFF


    def _decrypt_round(self, left_part, right_part, round_key):
        return left_part, right_part ^ self._f(left_part, round_key)

    def encrypt(self, plain_msg):
        def _encrypt_round(left_part, right_part, round_key):
            return right_part, left_part ^ self._f(right_part, round_key)

        left_part = plain_msg >> 32
        right_part = plain_msg & 0xFFFFFFFF
        for i in range(24):
            left_part, right_part = _encrypt_round(left_part, right_part, self._subkeys[i % 8])
        for i in range(8):
            left_part, right_part = _encrypt_round(left_part, right_part, self._subkeys[7 - i])
        return (left_part << 32) | right_part

    def decrypt(self, crypted_msg):
        def _decrypt_round(left_part, right_part, round_key):
            return right_part ^ self._f(left_part, round_key), left_part

        left_part = crypted_msg >> 32
        right_part = crypted_msg & 0xFFFFFFFF
        for i in range(8):
            left_part, right_part = _decrypt_round(left_part, right_part, self._subkeys[i])
        for i in range(24):
            left_part, right_part = _decrypt_round(left_part, right_part, self._subkeys[(7 - i) % 8])
        return (left_part << 32) | right_part


@app.route('/lab5gost98Enc', methods=['GET'])
def lab5gost98Enc():
    sbox = [numpy.random.permutation(l) for l in itertools.repeat(list(range(16)), 8)]
    sbox = (
        (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
        (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
        (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
        (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
        (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
        (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
        (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
        (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
    )

    key = 18318279387912387912789378912379821879387978238793278872378329832982398023031

    text_short = request.args.get('msg').encode().hex()
    text_short = int(text_short, 16)

    gost_short = GostCrypt(key, sbox)

    enc_txt = gost_short.encrypt(text_short)

    dec_txt = gost_short.decrypt(enc_txt)
    dec_txt = bytes.fromhex(hex(dec_txt)[2::]).decode('utf-8')

    text_long = request.args.get('msg').encode().hex()
    text_long = int(text_long, 16)

    return jsonify(str(enc_txt), dec_txt)

################################# ГОСТ 28147-89 конец

@app.route('/lab6')
def lab6():
    return render_template('lab6.html')

################################# Шифр A5/1

reg_x_length = 19
reg_y_length = 22
reg_z_length = 23
key_one = ""
reg_x = []
reg_y = []
reg_z = []

@app.route('/lab6a51', methods=['GET'])
def lab6a51():
    text = request.args.get('msg')

    # 0101001000011010110001110001100100101001000000110111111010110111

    key = str(user_input_key())
    set_key(key)
    enc_text = encode_lab6(text)
    dec_text = decode_lab6(enc_text)
    print(enc_text)
    return jsonify(enc_text, dec_text)

def loading_registers(key):
    i = 0
    while(i < reg_x_length):
        reg_x.insert(i, int(key[i]))
        i = i + 1
    j = 0
    p = reg_x_length
    while(j < reg_y_length):
        reg_y.insert(j, int(key[p]))
        p = p + 1
        j = j + 1
    k = reg_y_length + reg_x_length
    r = 0
    while(r < reg_z_length):
        reg_z.insert(r, int(key[k]))
        k = k + 1
        r = r + 1


def set_key(key):
    if(len(key) == 64 and re.match("^([01])+", key)):
        key_one = key
        loading_registers(key)
        return True
    return False


def get_key1():
    return key_one


def to_binary(plain):
    s = ""
    i = 0
    for i in plain:
        binary = str(' '.join(format(ord(x), 'b') for x in i))
        j = len(binary)
        while(j < 12):
            binary = "0" + binary
            s = s + binary
            j = j + 1
    binary_values = []
    k = 0
    while(k < len(s)):
        binary_values.insert(k, int(s[k]))
        k = k + 1
    return binary_values


def get_majority(x, y, z):
    if(x + y + z > 1):
        return 1
    else:
        return 0


def get_keystream(length):
    reg_x_temp = copy.deepcopy(reg_x)
    reg_y_temp = copy.deepcopy(reg_y)
    reg_z_temp = copy.deepcopy(reg_z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(reg_x_temp[8], reg_y_temp[10], reg_z_temp[10])
        if reg_x_temp[8] == majority:
            new = reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
            reg_x_temp_two = copy.deepcopy(reg_x_temp)
            j = 1
            while(j < len(reg_x_temp)):
                reg_x_temp[j] = reg_x_temp_two[j-1]
                j = j + 1
            reg_x_temp[0] = new

        if reg_y_temp[10] == majority:
            new_one = reg_y_temp[20] ^ reg_y_temp[21]
            reg_y_temp_two = copy.deepcopy(reg_y_temp)
            k = 1
            while(k < len(reg_y_temp)):
                reg_y_temp[k] = reg_y_temp_two[k-1]
                k = k + 1
            reg_y_temp[0] = new_one

        if reg_z_temp[10] == majority:
            new_two = reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
            reg_z_temp_two = copy.deepcopy(reg_z_temp)
            m = 1
            while(m < len(reg_z_temp)):
                reg_z_temp[m] = reg_z_temp_two[m-1]
                m = m + 1
            reg_z_temp[0] = new_two

        keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
        i = i + 1
    return keystream


def convert_binary_to_str(binary):
    s = ""
    length = len(binary) - 12
    i = 0
    while(i <= length):
        s = s + chr(int(binary[i:i+12], 2))
        i = i + 12
    return str(s)


def encode_lab6(plain):
    s = ""
    binary = to_binary(plain)
    keystream = get_keystream(len(binary))
    i = 0
    while(i < len(binary)):
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return s


def decode_lab6(cipher):
    s = ""
    binary = []
    keystream = get_keystream(len(cipher))
    i = 0
    while(i < len(cipher)):
        binary.insert(i, int(cipher[i]))
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return convert_binary_to_str(str(s))


def user_input_key(): # проверка ключа на валидность
    tha_key = '0101001000011010110001110001100100101001000000110111111010110111'
    if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
        return tha_key
    else:
        while(len(tha_key) != 64 and not re.match("^([01])+", tha_key)):
            if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
                return tha_key
            tha_key = str(input('Введите 64-bit ключ: '))
    return tha_key

################################# Шифр A5/1 конец

@app.route('/lab7')
def lab7():
    return render_template('lab7.html')

################################# КУЗНЕЧИК
@app.route('/lab7kuznechikEnc', methods=['GET'])
def lab7kuznechikEnc():

    #инициализация алфавита
    alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                    'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                    'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                    'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                    'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                    'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                    'ю':30, 'я':31, ' ':32, ",":33, ".":34
                    }

    #хэшируем сообщение
    msg = request.args.get('msg')
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    def hash_value(mod,alpha_code):
        i = 0
        hashing_value = 1
        while i < len(alpha_code_msg):
            hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % curve.p
            i += 1
        return hashing_value

    #класс точки, нужен для хранения точек и вывода их
    class Point:
        def __init__(self,x_init,y_init):
            self.x = x_init
            self.y = y_init

        def shift(self, x, y):
            self.x += x
            self.y += y

        def __repr__(self):
            return "".join(["( x=", str(self.x), ", y=", str(self.y), ")"])

    x_1=0 #магические переменные, которые хранят координаты точки Q
    y_1=0 #магические переменные, которые хранят координаты точки Q
    EllipticCurve = collections.namedtuple('EllipticCurve', 'name p q_mod a b q g n h') #тюпл(статичный массив, именной, хранит переменные(параметры эк))
    curve = EllipticCurve(
        'secp256k1',
        #параметры поля
        #модуль поля
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
        q_mod = 0xfffffffffefffffffffcfffffffffffcfffffffffffffffffffffffefffffc2f,
        #коэфф а и b
        a=7,
        b=11,
        #Базовая точка эк записано в hex
        g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
        0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
        q=(0xA0434D9E47F3C86235477C7B1AE6AE5D3442D49B1943C2B752A68E2A47E247C7,
        0x893ABA425419BC27A3B6C7E693A24C696F794C2ED877A1593CBEE53B037368D7),
        #Подгруппа группы точек
        n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
        #Подгруппа
        h=1,
    )
    print("Q mod",int(curve.q_mod))
    print("P mod",int(curve.p))
    def is_on_curve(point):
        """Возвращает True если точка лежит на элиптической кривой."""
        if point is None:
            return True

        x, y = point

        return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0

    def point_neg(point):
        """Инвертирует точку по оси y -point."""
        #assert is_on_curve(point)

        if point is None:
            # -0 = 0
            return None

        x, y = point
        result = (x, -y % curve.p)

        #assert is_on_curve(result)

        return result

    def inverse_mod(k, p):
        """Возвращает обратное k по модулю p.
        Эта функция возвращает число x удовлетворяющее условию (x * k) % p == 1.
        k не должно быть равно 0 и p должно быть простым.
        """
        if k == 0:
            raise ZeroDivisionError('деление на 0')

        if k < 0:
            # k ** -1 = p - (-k) ** -1  (mod p)
            return p - inverse_mod(-k, p)

        # Раширенный алгоритм Евклида.
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = p, k

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        gcd, x, y = old_r, old_s, old_t

        assert gcd == 1
        assert (k * x) % p == 1

        return x % p

    def point_add(point1, point2):
        """Возвращает результат операции сложения point1 + point2 оперируя законами операции над группами."""
        #assert is_on_curve(point1)
        #assert is_on_curve(point2)

        if point1 is None:
            # 0 + point2 = point2
            return point2
        if point2 is None:
            # point1 + 0 = point1
            return point1

        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2 and y1 != y2:
            # point1 + (-point1) = 0
            return None

        if x1 == x2:
            # This is the case point1 == point2.
            m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
        else:
            # This is the case point1 != point2.
            m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

        x3 = m * m - x1 - x2
        y3 = y1 + m * (x3 - x1)
        result = (x3 % curve.p,
                -y3 % curve.p)

        #assert is_on_curve(result)

        return result

    def scalar_mult(k, point):
        """Возвращает k * точку используя дублирование и алгоритм сложения точек."""
        #assert is_on_curve(point)

        if k % curve.n == 0 or point is None:
            return None

        if k < 0:
            # k * point = -k * (-point)
            return scalar_mult(-k, point_neg(point))

        result = None
        addend = point

        while k:
            if k & 1:
                # Add.
                result = point_add(result, addend)

            # Double.
            addend = point_add(addend, addend)

            k >>= 1

        #assert is_on_curve(result)

        return result

    #Вывод хэш-значения
    hash_code_msg = hash_value(curve.p, alpha_code_msg)
    print("Хэш сообщения:={}".format(hash_code_msg))
    #вычисляем е, обращаемся через тюпл к перемнной p
    e = hash_code_msg%curve.q_mod
    print("E={}".format(e))
    #генерация k
    k = random.randint(1,curve.q_mod)
    print("K={}".format(k))
    print("")
    #нахождение точки элиптической кривой из базовый точки C=K * P(x,y)
    d = 10
    print("D={}".format(d))
    x,y = scalar_mult(k,curve.g)
    point_c = Point(x,y)
    print("Point_C={}".format(point_c))
    r = point_c.x % curve.q_mod
    print("R={}".format(r))
    s = (r*curve.p + k*e)%curve.q_mod
    print("S={}".format(s))
    #проверка подписи
    v = inverse_mod(e,curve.p)
    print("V={}".format(v))
    z1 = (s*v)%curve.q_mod
    z2 = ((curve.p-r)*v)%curve.q_mod
    x_1,y_1 = scalar_mult(d,curve.g)
    print("Point_Q=( x={}, y={} )".format(x_1,y_1))
    point_c_new = Point(x,y)
    x,y = point_add(scalar_mult(z1,curve.g),
                    scalar_mult(z2,curve.q))
    r_1 = point_c_new.x% curve.q_mod
    print("R_new={}".format(r_1))
    if r == r_1:
        print("Подпись прошла проверку!")
    else:
        print("Ошибка проверки!")
################################# КУЗНЕЧИК конец

################################# МАГМА

@app.route('/c', methods=['GET'])
def lab7magmaEnc():


    # импорт компонентов, необходимых для работы программы
    pi0 = [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
    pi1 = [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15]
    pi2 = [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0]
    pi3 = [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11]
    pi4 = [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12]
    pi5 = [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0]
    pi6 = [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7]
    pi7 = [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]
    pi = [pi0, pi1, pi2, pi3, pi4, pi5, pi6, pi7]
    MASK32 = 2 ** 32 - 1

    to_encrypt = request.args.get('msg')

    def t(x):
        y = 0
        for i in reversed(range(8)):
            j = (x >> 4 * i) & 0xf
            y <<= 4
            y ^= pi[i][j]
        return y
    # функция сдвига на 11
    def rot11(x):
        return ((x << 11) ^ (x >> (32 - 11))) & MASK32
    def g(x, k):
        return rot11(t((x + k) % 2 ** 32))
    def split(x):
        L = x >> 32
        R = x & MASK32
        return (L, R)

    def join(L, R):
        return (L << 32) ^ R
    def magma_key_schedule(k):
        keys = []
        for i in reversed(range(8)):
            keys.append((k >> (32 * i)) & MASK32)
        for i in range(8):
            keys.append(keys[i])
        for i in range(8):
            keys.append(keys[i])
        for i in reversed(range(8)):
            keys.append(keys[i])
        return keys

    # функция шифрования
    def magma_encrypt(x, k):
        keys = magma_key_schedule(k)
        (L, R) = split(x)
        for i in range(31):
            (L, R) = (R, L ^ g(R, keys[i]))
        return join(L ^ g(R, keys[-1]), R)


    # функция расшифрования
    def magma_decrypt(x, k):
        keys = magma_key_schedule(k)
        keys.reverse()
        (L, R) = split(x)
        for i in range(31):
            (L, R) = (R, L ^ g(R, keys[i]))
        return join(L ^ g(R, keys[-1]), R)

    # установка ключа
    key = int('ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff', 16)

    i = 0
    text_short = to_encrypt
    encr_short = []
    while (i < len(text_short)):
        text = text_short[i:i+4].encode().hex()
        text = int(text, 16)
        text = text % 2**64
        pt = text
        ct = magma_encrypt(pt, key)
        encr_short.append(ct)
        i += 4
    decr_short = []
    for i in encr_short:
        dt = magma_decrypt(i, key)
        decr_short.append(bytes.fromhex(hex(dt)[2::]).decode('utf-8'))

    #вывод результатов работы программы
    def main():
        print(f'''
        МАГМА:
        КЛЮЧ:
        {key}

        КОРОТКИЙ ТЕКСТ:
        Зашифрованный текст:
        {encr_short}

        Расшифрованный текст:
        {''.join(decr_short)}
        ''')
    main()

    return jsonify(encr_short, ''.join(decr_short))

################################# МАГМА конец

@app.route('/lab8')
def lab8():
    return render_template('lab8.html')

################################ RSA

@app.route('/lab8rsaEnc', methods=['GET'])
def lab8rsaEnc():
    message = request.args.get('msg')
    p = int(request.args.get('p'))
    q = int(request.args.get('q'))

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def multiplicative_inverse(e,r):
        for i in range(r):
            if((e*i)%r == 1):
                return i

    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generate_keypair(p, q):
        if not (is_prime(p) and is_prime(q)):
            return ('Оба числа должны быть простыми.')
        elif p == q:
            return ('p и q не должны быть одинаковыми')
        #n = pq
        n = p * q

        phi = (p-1) * (q-1)

        e = random.randrange(1, phi)

        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        d = multiplicative_inverse(e, phi)
        return ((e, n), (d, n))

    def encrypt_lab8(pk, plaintext):
        key, n = pk
        cipher = [(ord(char) ** key) % n for char in plaintext]
        return cipher

    def decrypt_lab8(pk, ciphertext):
        key, n = pk
        plain = [chr((char ** key) % n) for char in ciphertext]
        return ''.join(plain)
         
    print("RSA")
   
    public, private = generate_keypair(p, q)
    print("Публичный ключ: ", public ,"Секретный ключ: ", private)
    encrypted_msg = encrypt_lab8(public, message)
    print("Зашифрованное сообщение: ")
    print(''.join([str(x) for x in encrypted_msg]))
    print("Расшифрованное сообщение: ")
    print(decrypt_lab8(private, encrypted_msg))

    return jsonify(''.join([str(x) for x in encrypted_msg]), decrypt_lab8(private, encrypted_msg))

################################### RSA конец

@app.route('/lab9')
def lab9():
    return render_template('lab9.html')

################################## ЭЦП RSA 

@app.route('/lab9rsaSign', methods=['GET'])
def lab9rsaSign():
    #инициализация алфавита
    alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                    'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                    'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                    'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                    'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                    'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                    'ю':30, 'я':31, ' ':32, ",":33, ".":34
                    }

    #проверка на простое число
    def IsPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    #расширенный алгоритм Евклида или (e**-1) mod fe
    def modInverse(e,el):
        e = e % el
        for x in range(1,el):
            if ((e * x) % el == 1):
                return x
        return 1

    #инициализация p,q,e,n
    p = int(request.args.get('p'))
    print('Число p простое: ' + str(IsPrime(p)))
    q = int(request.args.get('q'))
    print('Число q простое: ' + str(IsPrime(q)))
    n = p * q
    print("N =",n)
    el = (p-1) * (q-1)
    print("El =",el)

    e = random.randrange(1, el)
    g = gcd(e, el)
    while g != 1:
        e = random.randrange(1, el)
        g = gcd(e, el)

    print("E =",e)
    if gcd(e,el) == 1:
        print("E подходит")
    else:
        print(gcd(e,el),"False")
    #нахождение секретной экспоненты D
    d = modInverse(e,el)
    print("D =",d)
    print("Открытый ключ e={} n={}".format(e,n))
    print("Секретный ключ d={} n={}".format(d,n))
    #хэширование сообщения
    msg = request.args.get('msg')
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    def hash_value(n,alpha_code):
        i = 0
        hashing_value = 1
        while i < len(alpha_code_msg):
            hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % n
            i += 1
            print ("Значение хэша №{} = {}".format(i, hashing_value))
        return hashing_value

    hash_code_msg = hash_value(n, alpha_code_msg)
    print("Хэш сообщения", hash_code_msg)
    #подпись сообщения s=Sa(m) = m^d mod n
    def signature_msg(hash_code,n,d):
        sign = (hash_code**d)%n
        return sign

    sign_msg = signature_msg(hash_code_msg,n,d)
    print("Значение подписи: {}".format(sign_msg))
    #передаём пару m,s
    def check_signature(sign_msg, n,e):
        check = (sign_msg**e) % n
        return check

    check_sign = check_signature(sign_msg,n,e)
    print("Значение проверки подписи = {}".format(check_sign))

    return jsonify(hash_code_msg, sign_msg, str(check_sign))

################################## ЭЦП RSA конец

@app.route('/lab10')
def lab10():
    return render_template('lab10.html')

################################## ГОСТ Р 34.10-94

@app.route('/lab10gost', methods=['GET'])
def lab10gost():
    alphavit = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
        'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10,
        'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15,
        'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20,
        'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
        'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30,
        'ю': 31, 'я': 32
    }

    result = []

    def ciphergostd(clearText):
        array = []
        flag = False
        for s in range(50, 1000):
            for i in range(2, s):
                if s % i == 0:
                    flag = True
                    break
            if flag == False:
                array.append(s)
            flag = False

        p = 31
        print("p = ", p)
        q = 5
        print("q = ", q)
        a = 2
        print("a =", a)

        array2 = []
        flag2 = False
        for s in range(2, q):
            for i in range(2, s):
                if s % i == 0:
                    flag2 = True
                    break
            if flag2 == False:
                array2.append(s)
            flag2 = False
        x = 3
        print("x = ", x)
        y = a**x % p
        k = 4
        print("k = ", k)

        r = (a**k % p) % q
        result.append(r)
        msg = clearText
        msg_list = list(msg)
        alpha_code_msg = list()
        for i in range(len(msg_list)):
            alpha_code_msg.append(int(alphavit.get(msg_list[i])))
        print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
        hash_code_msg = hash_value(p, alpha_code_msg)
        print("Хэш сообщения = {}".format(hash_code_msg))
        s = (x*r+k*hash_code_msg) % q
        result.append(s)
        print("Цифровая подпись = ", r % (2**256), ",", s % (2**256))
        v = (hash_code_msg**(q-2)) % q
        z1 = s*v % q
        z2 = ((q-r)*v) % q
        u = (((a**z1)*(y**z2)) % p) % q
        result.append(u)

        if u == r:
            print(r,'=',u, 'следовательно:')
            print("Подпись верна\n")
        else:
            print("Подпись неверна")

    def hash_value(n, alpha_code):
        i = 0
        hash = 1
        while i < len(alpha_code):
            hash = (((hash-1) + int(alpha_code[i]))**2) % n
            i += 1
        return hash

    print('ГОСТ Р 34.10-94:')
    message = request.args.get('msg')
    ciphergostd(message)

    return jsonify(result[0], result[1], result[2])
################################## ГОСТ Р 34.10-94 конец

@app.route('/lab11')
def lab11():
    return render_template('lab11.html')

