// let alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?- \n';
let alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
let alphabet_amount = alphabet.length;


key_object = document.getElementById('key');
// key_string = key_object.value
// key = Number(key_string)


encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''

///////////////////// АТБАШ


atbash = document.getElementById('atbash');
atbash.onclick = function() {        
    key_object.style.display = 'none';
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function() {
        encrypted_text = ''
        decrypted_text = ''
        document.getElementById('decrypted').innerHTML = decrypted_text //очищаю строку "расшифрованный"
        original_text = document.getElementById('originalText');
        ot = original_text.value;
        length_of_original_text = ot.length;
        for(i = 0; i<length_of_original_text; i++){
            encrypted_letter_index = alphabet_amount - alphabet.indexOf(ot[i]); // нахожу индекс буквы, на которую будет произведена замена
            encrypted_letter = alphabet[encrypted_letter_index - 1]; // получаю букву по индексу
            encrypted_text += encrypted_letter; // из букв получаю зашифрованный текст
        }
        document.getElementById('encrypted').innerHTML = encrypted_text;
        encrypted_text = '';
    }

    decrypt_button.onclick = function() { // с расшифровкой абсолютно такие же действия
        decrypted_text = ''
        encrypted_text = document.getElementById('encrypted');
        et = encrypted_text.value;
        length_of_encrypted_text = et.length;
        for(i = 0; i<length_of_encrypted_text; i++){
            decrypted_letter_index = alphabet_amount - alphabet.indexOf(et[i]);
            decrypted_letter = alphabet[decrypted_letter_index - 1];
            decrypted_text += decrypted_letter;
        }
        document.getElementById('decrypted').innerHTML = decrypted_text;
        decrypted_text = '';
    }
}

//////////////// ЦЕЗАРЬ
    
caesar = document.getElementById('caesar');
caesar.onclick = function() {        
    key_object.style.display = 'block';
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function() {
        encrypted_text = ''
        decrypted_text = ''
        key_string = key_object.value
        key = Number(key_string)
        original_text = document.getElementById('originalText');
        ot = original_text.value;
        length_of_original_text = ot.length;
        for(i = 0; i<length_of_original_text; i++){
            encrypted_letter_index = (alphabet.indexOf(ot[i]) + key) % alphabet_amount; // нахожу индекс буквы со сдвигом по модулю текущего алфавита
            encrypted_letter = alphabet[encrypted_letter_index]; // получаю зишифрованную букву по индексу
            encrypted_text += encrypted_letter;
        }
        document.getElementById('encrypted').innerHTML = encrypted_text;
        encrypted_text = '';
    }

    decrypt_button.onclick = function() {
        key_string = key_object.value
        key = Number(key_string)
        encrypted_text = document.getElementById('encrypted');
        et = encrypted_text.value;
        length_of_encrypted_text = et.length;
        for(i = 0; i<length_of_encrypted_text; i++){
            decrypted_letter_index = (alphabet.indexOf(et[i]) - key + alphabet_amount * 10000) % alphabet_amount; // вместо числа 10000 может быть любое число, но такое, чтобы alphabet_amount * {число} > введенного ключа
            decrypted_letter = alphabet[decrypted_letter_index];
            decrypted_text += decrypted_letter;
        }
        document.getElementById('decrypted').innerHTML = decrypted_text;
        decrypted_text = '';
    }
    
}


///////////// КВАДРАТ ПОЛИБИЯ

square = document.getElementById('square');
square.onclick = function() {     
    key_object.style.display = 'none';
    minimum_square = 0
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    while (minimum_square**2 < alphabet_amount) {
        minimum_square+=1; // находим сторону квадрата исходя из размера алфавита
    }
    var square_new = [];
    var i;
    var j;
    for (i=0; i < minimum_square; i++) {
        square_new[i] = new Array();
        for (j=0; j < minimum_square; j++) {
            alphabet[minimum_square*i+j] ? square_new[i][j] = alphabet[minimum_square*i+j] : square_new[i][j] = ''; // заполнил квадрат. если до полного квадрата не хватает символов в алфавите, - там пропуски.
        } 

    }
    
    encrypt_button.onclick = function() {
        encrypted_text = '';
        original_text = document.getElementById('originalText');
        document.getElementById('encrypted').innerHTML = '' // очищаю формы с результатами
        ot = original_text.value
        //alert(ot)
        length_of_original_text = ot.length
        length_of_square_new = square_new.length
        for (i=0; i<length_of_original_text; i++) {
            for (a=0; a<length_of_square_new; a++) {
                if (square_new[a].indexOf(ot[i])!= -1) { // если в новой матрице есть число, сопоставимое с исходным алфавитом, то шифруй
                    encrypted_text += `${a}${square_new[a].indexOf(ot[i])} `;
                }
            }
        }
        document.getElementById('encrypted').innerHTML = encrypted_text;
    }

    decrypt_button.onclick = function() {
        document.getElementById('decrypted').innerHTML = ''

        encrypted_arr = encrypted_text.split(' ');
        for (i=0; i < encrypted_arr.length; i++) {
            if (encrypted_arr[i][0] && encrypted_arr[i][1]) {
                decrypted_text += square_new[Number(encrypted_arr[i][0])][Number(encrypted_arr[i][1])];
            }
        }
        document.getElementById('decrypted').innerHTML = decrypted_text;
        decrypted_text = '';
    }
}



