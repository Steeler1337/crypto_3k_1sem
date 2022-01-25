//let alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?- \n';
let alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя';
let alphabet_amount = alphabet.length;

key_object = document.getElementById('key');

encrypt_button = document.getElementById('encrypt');
decrypt_button = document.getElementById('decrypt');
encrypted_text = ''
decrypted_text = ''


///////// ТРИТЕМИЙ

tritemia = document.getElementById('tritemia');
tritemia.onclick = function() {        
    key_object.style.display = 'none';
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function() {
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
        checker = -1;
        for(i = 0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();  // к маленькому регистру привожу все буквы.
            checker += 1
            encrypted_letter_index = (alphabet.indexOf(small_letter) + checker + alphabet_amount) % alphabet_amount; // нахожу индекс зашифрованной буквы, предусматривая случай, что в исходном тексте может быть больше 32 символов
            encrypted_letter = alphabet[encrypted_letter_index];
            encrypted_text += encrypted_letter;
        }
        document.getElementById('encrypted').innerHTML = encrypted_text //для расшифровки
        encrypted_text = ''
    }

    decrypt_button.onclick = function() {
        decrypted_text = ''
        encrypted_text = document.getElementById('encrypted');
        et = encrypted_text.value;
        length_of_encrypted_text = et.length;
        checker = 0
        for(i = 0; i<length_of_encrypted_text; i++){
            decrypted_letter_index = (alphabet.indexOf(et[i]) - checker + alphabet_amount * 1000000) % alphabet_amount; // увеличиваем checker. Так как первая буква - исходная, изначально checker равен нулю, для второй буквы он равен 1 (вторая строчка таблицы тритемия), для третьей буквы он равен 2 (третья строчка таблицы тритемия) т.д. Важно, чтобы alphabet_amount * 10000 (или другое число вместо 10000) был больше, чем кол-во символов в шифртексте.
            decrypted_letter = alphabet[decrypted_letter_index];
            decrypted_text += decrypted_letter;
            checker += 1
        }
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
    }

}

///////////////// БЕЛАЗО

belazo = document.getElementById('belazo');
belazo.onclick = function() {        
    key_object.style.display = 'block';
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function() {
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
        key_word = key_object.value;
        key_length = key_word.length;
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            origin_letter_index = alphabet.indexOf(small_letter);
            index_key_letter_alphabet = alphabet.indexOf(key_word[i%key_length]); //узнаем индекс буквы кодового слова
            from_key_index_to_end = alphabet.substring(index_key_letter_alphabet); // от буквы кодового слова в алфавите до конца алфавита
            from_begin_to_key_index = alphabet.substring(0,index_key_letter_alphabet); // от начала алфавита до буквы кодового слова в алфавите
            new_alphabet = from_key_index_to_end + from_begin_to_key_index;
            encrypted_letter = new_alphabet[origin_letter_index];
            encrypted_text += encrypted_letter;
        }
        document.getElementById('encrypted').innerHTML = encrypted_text; //для расшифровки
        encrypted_text = '';
    }

    decrypt_button.onclick = function() {
        decrypted_text = '';
        encrypted_text = document.getElementById('encrypted');
        et = encrypted_text.value;
        length_of_encrypted_text = et.length;
        key_word = key_object.value;
        key_length = key_word.length;
        for(i=0; i<length_of_encrypted_text; i++){
            encrypted_letter_index = alphabet.indexOf(et[i]);
            key_letter_index = alphabet.indexOf(key_word[i%key_length]);
            decrypted_index = 0;
            if (encrypted_letter_index - key_letter_index <= 0){
                decrypted_index = encrypted_letter_index + alphabet_amount - key_letter_index;
            } else {
                decrypted_index = encrypted_letter_index - key_letter_index;
            }
            decrypted_text += alphabet[decrypted_index % alphabet_amount];
        }
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
    }
}


///////////////////// ВИЖЕНЕР
clean_text = ''

vizhener = document.getElementById('vizhener')
vizhener.onclick = function() {
    key_object.style.display = 'block';
    document.getElementById('encrypted').innerHTML = '' //очищаю формы с результатами
    document.getElementById('decrypted').innerHTML = ''
    encrypt_button.onclick = function() {
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
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            clean_text += small_letter;
        }
        key_word = key_object.value + clean_text;
        //alert(key_word);
        key_length = key_word.length;
        for(i=0; i<length_of_original_text; i++){
            small_letter = ot[i].toLowerCase();
            origin_letter_index = alphabet.indexOf(small_letter);
            index_key_letter_alphabet = alphabet.indexOf(key_word[i%key_length]); //узнаем индекс буквы кодового слова
            from_key_index_to_end = alphabet.substring(index_key_letter_alphabet); // от буквы кодового слова в алфавите до конца алфавита
            from_begin_to_key_index = alphabet.substring(0,index_key_letter_alphabet); // от начала алфавита до буквы кодового слова в алфавите
            new_alphabet = from_key_index_to_end + from_begin_to_key_index;
            encrypted_letter = new_alphabet[origin_letter_index];
            encrypted_text += encrypted_letter;
        }
        document.getElementById('encrypted').innerHTML = encrypted_text; //для расшифровки
        encrypted_text = '';
    }

    decrypt_button.onclick = function() {
        decrypted_text = '';
        encrypted_text = document.getElementById('encrypted');
        et = encrypted_text.value;
        length_of_encrypted_text = et.length;
        key_word = key_object.value + clean_text;
        key_length = key_word.length;
        for(i=0; i<length_of_encrypted_text; i++){
            encrypted_letter_index = alphabet.indexOf(et[i]);
            key_letter_index = alphabet.indexOf(key_word[i%key_length]);
            decrypted_index = 0;
            if (encrypted_letter_index - key_letter_index <= 0){
                decrypted_index = encrypted_letter_index + alphabet_amount - key_letter_index;
            } else {
                decrypted_index = encrypted_letter_index - key_letter_index;
            }
            decrypted_text += alphabet[decrypted_index % alphabet_amount];
        }
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
        clean_text = '';
    }
}
