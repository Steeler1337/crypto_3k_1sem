a_object = document.getElementById('a_lab11');
n_object = document.getElementById('n_lab11');
submit_an = document.getElementById('submit_an');
submit_Ka = document.getElementById('submit_Ka');
submit_Ka.style.display = 'none'

Ka_label = document.getElementById('Ka_label');
Ka_label.style.display = 'none';
Ka_lab11 = document.getElementById('Ka_lab11');
Ka_lab11.style.display = 'none';
Kb_label = document.getElementById('Kb_label');
Kb_label.style.display = 'none';
Kb_lab11 = document.getElementById('Kb_lab11');
Kb_lab11.style.display = 'none';

Ya = document.getElementById('Ya');
Ya.style.display = 'none';
Yb = document.getElementById('Yb');
Yb.style.display = 'none';
Ya_label = document.getElementById('Ya_label');
Ya_label.style.display = 'none';
Yb_label = document.getElementById('Yb_label');
Yb_label.style.display = 'none';

Ya_checker_label = document.getElementById('Ya_checker_label');
Ya_checker_label.style.display = 'none';
Yb_checker_label = document.getElementById('Yb_checker_label');
Yb_checker_label.style.display = 'none';
Ya_checker = document.getElementById('Ya_checker');
Ya_checker.style.display = 'none';
Yb_checker = document.getElementById('Yb_checker');
Yb_checker.style.display = 'none';

submit_result = document.getElementById('submit_result');
submit_result.style.display = 'none';

final_label = document.getElementById('final_label');
final_label.style.display = 'none';
final = document.getElementById('final');
final.style.display = 'none';

submit_an.onclick = function() {
    a = a_object.value;
    n = n_object.value;
    a_object.setAttribute('readonly', true);
    n_object.setAttribute('readonly', true);
    submit_an.style.display = 'none'
    Ka_label.style.display = 'block';
    Ka_lab11.style.display = 'block';
    Kb_label.style.display = 'block';
    Kb_lab11.style.display = 'block';
    submit_Ka.style.display = 'block';
    submit_Ka.onclick = function() {
        Ka = Ka_lab11.value;
        Kb = Kb_lab11.value;
        Ka_lab11.setAttribute('readonly', true);
        Kb_lab11.setAttribute('readonly', true);
        submit_Ka.style.display = 'none';
        Ya.style.display = 'block';
        Yb.style.display = 'block';
        Ya_label.style.display = 'block';
        Yb_label.style.display = 'block';
        Ya.value = Math.pow(a, Ka) % n;
        Yb.value = Math.pow(a, Kb) % n;
        Ya_checker_label.style.display = 'block';
        Yb_checker_label.style.display = 'block';
        Ya_checker.style.display = 'block';
        Yb_checker.style.display = 'block';
        submit_result.style.display = 'block';
        submit_result.onclick = function() {
            submit_result.style.display = 'none';
            K = Math.pow(a, (Ya.value * Yb.value)) % n;
            final_label.style.display = 'block';
            final.style.display = 'block';
            final.value = K;
        }
    }
}
