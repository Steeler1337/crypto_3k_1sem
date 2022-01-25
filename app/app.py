from crypt import methods
from flask import Flask, render_template, request
from flask.json import jsonify
import numpy as np
import math
import random
import time

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
        matrix_numpy = np.matrix(arr_tchk_zpt) # здесь происходит преобразование в матрицу вида numpy
        opredelitel = np.linalg.det(matrix_numpy) # нахожу определитель
        if opredelitel == 0: # если определитель равен нулю, то матрица вырожденная, выводим ошибку
            return jsonify('error')
        else:
            obratnaya = np.linalg.inv(matrix_numpy) # чтобы произвести расшифровку нужно обратную матрицу умножить на массив зашифрованный чисел. Обратную матрицу также получаем с помощью библиотеки numpy.
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
        matrix_numpy = np.matrix(arr_tchk_zpt) # здесь происходит преобразование в матрицу вида numpy
        opredelitel = np.linalg.det(matrix_numpy) # нахожу определитель
        if opredelitel == 0:
            return jsonify('error') # если определитель равен нулю, то матрица вырожденная, выводим ошибку
        else:
            obratnaya = np.linalg.inv(matrix_numpy) # чтобы произвести расшифровку нужно обратную матрицу умножить на массив зашифрованный чисел. Обратную матрицу также получаем с помощью библиотеки numpy.
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


@app.route('/lab5', methods=['GET'])
def lab5():
    return render_template('lab5.html')
    

