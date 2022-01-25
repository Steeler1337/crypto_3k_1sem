function sendRequest(url, method, onloadHandler, params) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.responseType = 'json';
    xhr.onload = onloadHandler;
    xhr.send(params);

}

//let alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?- \n';
let alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя';
let alphabet_amount = alphabet.length;

key_object = document.getElementById('key');
desc = document.getElementById('description');

encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''

////////////////////////// МАТРИЧНЫЙ ШИФР

matrica = document.getElementById('matrica');
matrica.onclick = function () {
    desc.style.display = 'block';
    encrypted_text = ''
    decrypted_text = ''
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function () {
        encrypted_text = ''
        decrypted_text = ''
        original_text = document.getElementById('originalText');
        ot = original_text.value;
        ot = ot.replaceAll('.', 'тчк');
        ot = ot.replaceAll(',', 'зпт');
        ot = ot.replaceAll('!', 'вскл');
        ot = ot.replaceAll('-', 'дфс');
        ot = ot.replaceAll('?', 'впр');
        ot = ot.replaceAll('«', 'ковычслева');
        ot = ot.replaceAll('»', 'ковычсправа');
        ot = ot.replaceAll(':', 'двоеточ');
        ot = ot.replaceAll(';', 'тчзапят');
        ot = ot.replaceAll(/\s/g, ''); // убираю пробелы из исходной фразы
        length_of_original_text = ot.length;
        small_letter = '';
        indexes_orig_word = new Array();
        indexes_orig_word = [];
        key_string = key_object.value;
        key_arr = key_string.split(' ');
        if (key_arr.length == 9) {
            a1 = key_arr[0];
            a2 = key_arr[1];
            a3 = key_arr[2];
            b1 = key_arr[3];
            b2 = key_arr[4];
            b3 = key_arr[5];
            c1 = key_arr[6];
            c2 = key_arr[7];
            c3 = key_arr[8];
            for (i = 0; i < length_of_original_text; i++) {
                small_letter = ot[i].toLowerCase(); //привожу все буквы к нижнему регистру
                indexes_orig_word.push(alphabet.indexOf(small_letter) + 1); //записываю в строку индексы букв исходного текста в алфавите, чтобы потом умножать их на ключевую матрицу. делаю +1 чтобы букву А с нулевым индексом обработать верно в дальнейшем.
            }
            while (indexes_orig_word.length % 3 != 0) {
                indexes_orig_word.push(1); // заполняю единицами все оставшиеся пустые места в матрице, чтобы шифр работал. Так как матрица 3 х 3, то и шифруемый текст должен быть кратен 3.
            }
            enc_arr = new Array();
            enc_arr = [];
            for (i = 0; i <= indexes_orig_word.length - 3; i = i + 3) { // здесь произвожу умножение матрицы-ключа на индексы шифруемого текста
                summa1 = (a1 * indexes_orig_word[i]) + (a2 * indexes_orig_word[i + 1]) + (a3 * indexes_orig_word[i + 2]);
                summa2 = (b1 * indexes_orig_word[i]) + (b2 * indexes_orig_word[i + 1]) + (b3 * indexes_orig_word[i + 2]);
                summa3 = (c1 * indexes_orig_word[i]) + (c2 * indexes_orig_word[i + 1]) + (c3 * indexes_orig_word[i + 2]);
                enc_arr.push(summa1); // здесь умножение каждой из 3-х строк записываю в один массив
                enc_arr.push(summa2);
                enc_arr.push(summa3);
            }
            et = enc_arr.join(' '); // из массива делаю строку
            encrypted_text = enc_arr;
            document.getElementById('encrypted').innerHTML = et;
            

        } else if (key_arr.length == 16) {
            a1 = key_arr[0];
            a2 = key_arr[1];
            a3 = key_arr[2];
            a4 = key_arr[3];
            b1 = key_arr[4];
            b2 = key_arr[5];
            b3 = key_arr[6];
            b4 = key_arr[7];
            c1 = key_arr[8];
            c2 = key_arr[9];
            c3 = key_arr[10];
            c4 = key_arr[11];
            d1 = key_arr[12];
            d2 = key_arr[13];
            d3 = key_arr[14];
            d4 = key_arr[15];
            for (i = 0; i < length_of_original_text; i++) {
                small_letter = ot[i].toLowerCase(); //привожу все буквы к нижнему регистру
                indexes_orig_word.push(alphabet.indexOf(small_letter) + 1); //записываю в строку индексы букв исходного текста в алфавите, чтобы потом умножать их на ключевую матрицу. делаю +1 чтобы букву А с нулевым индексом обработать верно в дальнейшем.
            }
            while (indexes_orig_word.length % 4 != 0) {
                indexes_orig_word.push(1); // заполняю единицами все оставшиеся пустые места в матрице, чтобы шифр работал. Так как матрица 4 х 4, то и шифруемый текст должен быть кратен 4.
            }
            enc_arr = new Array();
            enc_arr = [];
            for (i = 0; i <= indexes_orig_word.length - 4; i = i + 4) { // здесь произвожу умножение матрицы-ключа на индексы шифруемого текста
                summa1 = (a1 * indexes_orig_word[i]) + (a2 * indexes_orig_word[i + 1]) + (a3 * indexes_orig_word[i + 2]) + (a4 * indexes_orig_word[i + 3]);
                summa2 = (b1 * indexes_orig_word[i]) + (b2 * indexes_orig_word[i + 1]) + (b3 * indexes_orig_word[i + 2]) + (b4 * indexes_orig_word[i + 3]);
                summa3 = (c1 * indexes_orig_word[i]) + (c2 * indexes_orig_word[i + 1]) + (c3 * indexes_orig_word[i + 2]) + (c4 * indexes_orig_word[i + 3]);
                summa4 = (d1 * indexes_orig_word[i]) + (d2 * indexes_orig_word[i + 1]) + (d3 * indexes_orig_word[i + 2]) + (d4 * indexes_orig_word[i + 3]);
                enc_arr.push(summa1); // здесь умножение каждой из 4-х строк записываю в один массив
                enc_arr.push(summa2);
                enc_arr.push(summa3);
                enc_arr.push(summa4);
            }
            et = enc_arr.join(' '); // из массива делаю строку
            encrypted_text = enc_arr;
            document.getElementById('encrypted').innerHTML = et;
            

        }
    }

    decrypt_button.onclick = function () {
        decrypted_text = ''
        et = encrypted_text;
        //length_of_encrypted_text = et.length;
        if (key_arr.length == 9) {
            a1 = key_arr[0];
            a2 = key_arr[1];
            a3 = key_arr[2];
            b1 = key_arr[3];
            b2 = key_arr[4];
            b3 = key_arr[5];
            c1 = key_arr[6];
            c2 = key_arr[7];
            c3 = key_arr[8];

            arr_matrix = new Array();
            arr_matrix = [
                [a1, a2, a3],
                [b1, b2, b3],
                [c1, c2, c3]
            ];

            decr_word = new Array
            decr_word = []

            url = `${window.location.origin}` + '/decodeLab3' + `?enc_text=${et}&arr_mat=${arr_matrix}`;
            sendRequest(url, 'GET', function () {
                recv_obj = this.response;
                if (recv_obj == 'error'){
                    alert('МАТРИЦА ВЫРОЖДЕННАЯ!') // если получаю сигнал из питона error, то делаю алерт, что матрица вырожденная
                }
                for (i = 0; i < recv_obj.length; i++) {
                    decr_word.push(alphabet[recv_obj[i] - 1]) // заменяю индексы из полученной строки на буквы из алфавита
                }
                decrypted_text = decr_word.join('') // привожу к виду строки
                // alert(decrypted_text);
                decrypted_text = decrypted_text.replaceAll('тчк', '.');
                decrypted_text = decrypted_text.replaceAll('зпт', ',');
                decrypted_text = decrypted_text.replaceAll('вскл', '!');
                decrypted_text = decrypted_text.replaceAll('дфс', '-');
                decrypted_text = decrypted_text.replaceAll('впр', '?');
                decrypted_text = decrypted_text.replaceAll('ковычслева', '«');
                decrypted_text = decrypted_text.replaceAll('ковычсправа', '»');
                decrypted_text = decrypted_text.replaceAll('двоеточ', ':');
                decrypted_text = decrypted_text.replaceAll('тчзапят', ';');
                document.getElementById('decrypted').innerHTML = decrypted_text;
                decrypted_text = '';
            })
        } else if (key_arr.length == 16) {
            a1 = key_arr[0];
            a2 = key_arr[1];
            a3 = key_arr[2];
            a4 = key_arr[3];
            b1 = key_arr[4];
            b2 = key_arr[5];
            b3 = key_arr[6];
            b4 = key_arr[7];
            c1 = key_arr[8];
            c2 = key_arr[9];
            c3 = key_arr[10];
            c4 = key_arr[11];
            d1 = key_arr[12];
            d2 = key_arr[13];
            d3 = key_arr[14];
            d4 = key_arr[15];

            arr_matrix = new Array();
            arr_matrix = [
                [a1, a2, a3, a4],
                [b1, b2, b3, b4],
                [c1, c2, c3, c4],
                [d1, d2, d3, d4]
            ];

            decr_word = new Array
            decr_word = []

            url = `${window.location.origin}` + '/decodeLab3' + `?enc_text=${et}&arr_mat=${arr_matrix}`;
            sendRequest(url, 'GET', function () {
                recv_obj = this.response;
                if (recv_obj == 'error'){
                    alert('МАТРИЦА ВЫРОЖДЕННАЯ!') // если получаю сигнал из питона error, то делаю алерт, что матрица вырожденная
                }
                for (i = 0; i < recv_obj.length; i++) { // заменяю индексы из полученной строки на буквы из алфавита
                    decr_word.push(alphabet[recv_obj[i] - 1])
                }
                decrypted_text = decr_word.join('') // привожу к виду строки
                // alert(decrypted_text);
                decrypted_text = decrypted_text.replaceAll('тчк', '.');
                decrypted_text = decrypted_text.replaceAll('зпт', ',');
                decrypted_text = decrypted_text.replaceAll('вскл', '!');
                decrypted_text = decrypted_text.replaceAll('дфс', '-');
                decrypted_text = decrypted_text.replaceAll('впр', '?');
                decrypted_text = decrypted_text.replaceAll('ковычслева', '«');
                decrypted_text = decrypted_text.replaceAll('ковычсправа', '»');
                decrypted_text = decrypted_text.replaceAll('двоеточ', ':');
                decrypted_text = decrypted_text.replaceAll('тчзапят', ';');
                document.getElementById('decrypted').innerHTML = decrypted_text;
                decrypted_text = '';
            })
        }
    }
}

/////////////////////////////////////ШИФР ПЛЕЙФЕРА
playfair = document.getElementById('playfair');
playfair.onclick = function () {
    desc.style.display = 'none';
    encrypted_text = ''
    decrypted_text = ''
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function () {
        encrypted_text = ''
        decrypted_text = ''
        original_text = document.getElementById('originalText');
        ot = original_text.value;
        ot = ot.replaceAll('.', 'тчк');
        ot = ot.replaceAll(',', 'зпт');
        ot = ot.replaceAll('!', 'вскл');
        ot = ot.replaceAll('-', 'дфс');
        ot = ot.replaceAll('?', 'впр');
        ot = ot.replaceAll('«', 'ковычслева');
        ot = ot.replaceAll('»', 'ковычсправа');
        ot = ot.replaceAll(':', 'двоеточ');
        ot = ot.replaceAll(';', 'тчзапят');
        ot = ot.replaceAll(/\s/g, ''); // убираю пробелы из исходной фразы
        length_of_original_text = ot.length;
        small_letter = ''

        clean_text = '' // к нижнему регистру весь исходный текст
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            clean_text += small_letter;
        }
        ot = clean_text

        key_string = key_object.value;
        url = `${window.location.origin}` + '/playfairEncode' + `?text=${ot}&key=${key_string}`;
            sendRequest(url, 'GET', function () {
                encrypted_text = this.response;
                document.getElementById('encrypted').innerHTML = encrypted_text;
            })
    }

    decrypt_button.onclick = function () {
        decrypted_text = ''
        et = encrypted_text;
        key_string = key_object.value;
        url = `${window.location.origin}` + '/playfairDecode' + `?text=${et}&key=${key_string}`;
            sendRequest(url, 'GET', function () {
                decrypted_text = this.response;
                decrypted_text = decrypted_text.replaceAll('тчк', '.');
                decrypted_text = decrypted_text.replaceAll('зпт', ',');
                decrypted_text = decrypted_text.replaceAll('вскл', '!');
                decrypted_text = decrypted_text.replaceAll('дфс', '-');
                decrypted_text = decrypted_text.replaceAll('впр', '?');
                decrypted_text = decrypted_text.replaceAll('ковычслева', '«');
                decrypted_text = decrypted_text.replaceAll('ковычсправа', '»');
                decrypted_text = decrypted_text.replaceAll('двоеточ', ':');
                decrypted_text = decrypted_text.replaceAll('тчзапят', ';');
                document.getElementById('decrypted').innerHTML = decrypted_text;
            })
    }
}