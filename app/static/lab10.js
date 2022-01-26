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

p_lab10 = document.getElementById('p_lab10')
q_lab10 = document.getElementById('q_lab10')
p_lab10.style.display = 'none';
q_lab10.style.display = 'none';

encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''

////////////////////////// RSA

gost_10 = document.getElementById('gost_10');
gost_10.onclick = function () {
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
        p = p_lab10.value;
        q = q_lab10.value;
        url = `${window.location.origin}` + '/lab10gost' + `?msg=${ot}`;
        sendRequest(url, 'GET', function () {
            document.getElementById('r_mod').innerHTML = this.response[0];
            document.getElementById('s_mod').innerHTML = this.response[1];
            document.getElementById('u').innerHTML = this.response[2];
        })
    }
}

////////////////////////// RSA конец
