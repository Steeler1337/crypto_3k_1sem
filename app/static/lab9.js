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
decrypt_button = document.getElementById('decrypt');

p_lab9 = document.getElementById('p_lab9')
q_lab9 = document.getElementById('q_lab9')


encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''

////////////////////////// RSA

rsa1 = document.getElementById('rsa1');
rsa1.onclick = function () {
    desc1.style.display = 'none';
    decrypt_button.hidden = false;
    encrypted_text = ''
    decrypted_text = ''
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
        clean_text = '' // к нижнему регистру весь исходный текст
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            clean_text += small_letter;
        }
        ot = clean_text;
        p = p_lab9.value;
        q = q_lab9.value;
        url = `${window.location.origin}` + '/lab9rsaSign' + `?msg=${ot}&p=${p}&q=${q}`;
        sendRequest(url, 'GET', function () {
            document.getElementById('hash_code_msg').innerHTML = this.response[0];
            document.getElementById('sign_msg').innerHTML = this.response[1];
            document.getElementById('check_sign').innerHTML = this.response[2];
        })
    }
}

////////////////////////// RSA конец
