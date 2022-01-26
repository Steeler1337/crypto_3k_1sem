function sendRequest(url, method, onloadHandler, params) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.responseType = 'json';
    xhr.onload = onloadHandler;
    xhr.send(params);
}

let alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя';
let alphabet_amount = alphabet.length;

key_object = document.getElementById('key');
desc1 = document.getElementById('description1');
desc1.style.display = 'none';
key_field = document.getElementById('key');
key_field.hidden = true;
decrypt_button = document.getElementById('decrypt');


encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''

////////////////////////// КУЗНЕЧИК

kuznechik = document.getElementById('kuznechik');
kuznechik.onclick = function () {
    desc1.style.display = 'none';
    key_field.style.display = 'none';
    decrypt_button.hidden = false;
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
        url = `${window.location.origin}` + '/lab7kuznechikEnc' + `?msg=${ot}`;
        sendRequest(url, 'GET', function () {
            encrypted_text = this.response[0];
            decrypted_text = this. response[1];
            document.getElementById('encrypted').innerHTML = encrypted_text;
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

////////////////////////// КУЗНЕЧИК конец


////////////////////////// МАГМА

magma = document.getElementById('magma');
magma.onclick = function () {
    desc1.style.display = 'none';
    key_field.style.display = 'none';
    decrypt_button.hidden = false;
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
        url = `${window.location.origin}` + '/lab7magmaEnc' + `?msg=${ot}`;
        sendRequest(url, 'GET', function () {
            encrypted_text = this.response[0];
            decrypted_text = this. response[1];
            document.getElementById('encrypted').innerHTML = encrypted_text;
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