function sendRequest(url, method, onloadHandler, params) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.responseType = 'json';
    xhr.onload = onloadHandler;
    xhr.send(params);
}

let alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя ';
let alphabet_amount = alphabet.length;

key_object = document.getElementById('key');
desc1 = document.getElementById('description1');
key_field = document.getElementById('key');
desc1.style.display = 'none';
ogran = document.getElementById('ogran')

encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''


////////////////////////// ВЕРТИКАЛЬНАЯ ПЕРЕСТАНОВКА

vertic = document.getElementById('vertic');
vertic.onclick = function () {
    desc1.style.display = 'block';
    key_field.style.display = 'block';
    encrypted_text = ''
    decrypted_text = ''
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function () {
        document.getElementById('decrypted').innerHTML = ''
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
        clean_text = '' // к нижнему регистру весь исходный текст
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            clean_text += small_letter;
        }
        ot = clean_text
        key_string = key_object.value;
        url = `${window.location.origin}` + '/encodeLab4' + `?orig_text=${ot}&key=${key_string}`;
        sendRequest(url, 'GET', function () {
            encrypted_text = this.response;
            document.getElementById('encrypted').innerHTML = encrypted_text;
        })
    }

    decrypt_button.onclick = function () {
        decrypted_text = ''
        et = encrypted_text;
        url = `${window.location.origin}` + '/decodeLab4' + `?enc_text=${et}&key=${key_string}`;
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
            decrypted_text = '';
        })
    }
}


kardano = document.getElementById('kardano');
kardano.onclick = function () {
    desc1.style.display = 'none';
    key_field.style.display = 'none';
    encrypted_text = ''
    decrypted_text = ''
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function () {
        document.getElementById('decrypted').innerHTML = ''
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
        clean_text = '' // к нижнему регистру весь исходный текст
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            clean_text += small_letter;
        }
        ot = clean_text
        key_string = key_object.value;
        url = `${window.location.origin}` + '/encodeLab41' + `?orig_text=${ot}&check=${1}`;
        sendRequest(url, 'GET', function () {
            encrypted_text = this.response;
            encrypted_text = encrypted_text.replaceAll(' ', '')
            document.getElementById('encrypted').innerHTML = encrypted_text;
        })

    }

    decrypt_button.onclick = function () {
        decrypted_text = ''
        original_text = document.getElementById('originalText');
        ot = original_text.value;
        ot = ot.replaceAll('.', '');
        ot = ot.replaceAll(',', '');
        ot = ot.replaceAll('!', '');
        ot = ot.replaceAll('-', ' ');
        ot = ot.replaceAll('?', '');
        ot = ot.replaceAll(';', '');
        ot = ot.replaceAll(':', '');
        ot = ot.replaceAll('\n', ' ');
        ot = ot.replaceAll(' ', '');
        length_of_original_text = ot.length;
        url = `${window.location.origin}` + '/encodeLab41' + `?orig_text=${ot}&check=${2}`;
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
            decrypted_text = '';
        })
    }
}
