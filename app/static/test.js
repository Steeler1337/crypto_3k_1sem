
ot = 'Я приехал сюда';
var et = new Array();
var et = [];
ot = ot.toLowerCase();
ot_arr = ot.split(' ');
for (i=0; i<ot_arr.length;i++){
    word = ot_arr[i];
    big_word = '';
    for (j=0; j<word.length; j++){
        big_word += word[j].toUpperCase();
        //alert(big_word);
    }
    et.push(big_word);
}
et.join('0');
alert(et.join(' '));
