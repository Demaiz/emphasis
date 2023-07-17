"use strict";

let words_without_emphasis = [];
let words_emphasis = [];


function get_all_data(url) {
  fetch(url, {
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    }
  })
  .then(response => response.json())
  .then(data => {
// make arr with words
    (data.context).forEach(words => {
    words_without_emphasis.push(words.words_without_emphasis)
    words_emphasis.push(words.words_emphasis)
    });

    let button = document.querySelector('#start_button');
    let header = document.querySelector('#header');


start()

function start() {
    header.innerHTML = "Обери букву на яку падає наголос";
// replace the button
    let continue_button = document.querySelector('#continue_button');
    continue_button.style.display = "inline-block"
    play(words_without_emphasis, words_emphasis);
    };


     function play(words_without_emphasis, words_emphasis) {
     let iter = 0;
     let statistic = {right_answer: 0,
                      wrong_answer: 0,
                      words_with_mistake: [],
                      words_without_mistake: [],
                      };

     // get arr of random numbers
    const range = words_emphasis.length - 1;
    const count = 15;

    let m = {};
    let a = [];

    for (let i = 0; i < count; ++i) {
      let r = Math.floor(Math.random() * (range - i));
      a.push(((r in m) ? m[r] : r) + 1);
      let l = range - i - 1;
      m[r] = (l in m) ? m[l] : l;
      }
          
     get_word(words_without_emphasis, words_emphasis, a, iter, statistic)
    }


    function get_word(words_without_emphasis, words_emphasis, a, iter, statistic) {
        let c = document.querySelector('#counter');
        c.innerHTML = iter + 1 + "/15";
        let word_without_emphasis = words_without_emphasis[a[iter]];
        let word = document.querySelector('#word');
        word.innerHTML = word_without_emphasis;
        change_word(words_without_emphasis, words_emphasis, a, iter, statistic)
}


    function change_word(words_without_emphasis, words_emphasis, a, iter, statistic) {
    let l1 = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
    let l2 = ["а́", "б́", "в́", "ѓ", "ґ́", "д́", "е́", "є́", "ж́", "з́", "и́", "і́", "ї́", "й́", "ќ", "л́", "м́", "н́", "о́", "п́", "р́", "с́", "т́", "у́", "ф́", "х́", "ц́", "ч́", "ш́", "щ́", "ь́", "ю́", "я́"]
    let word = document.querySelector('#word');
    let str = "";
    for (let g = 1; g <= word.textContent.length; g++) {
    str += "<span id = \"" + g + "\">" + word.textContent[g-1] + "</span>";
    }
    word.innerHTML = str;

    let span = document.querySelectorAll('span');
    for (let h of span) {
    h.addEventListener('click', function click_emphasis(event) {
        let letter_index = l1.indexOf(h.textContent.toLowerCase());
        let letter_index2 = l2.indexOf(h.textContent.toLowerCase());

        if (h.textContent.includes('́')){
             if (h.id == 1){
                h.innerHTML = l1[letter_index2].toUpperCase();
                }
             else{
                h.innerHTML = l1[letter_index2];
                }
        }
        else{
            if (h.id == 1){
                h.innerHTML = l2[letter_index].toUpperCase();
                }
            else{
                h.innerHTML = l2[letter_index];
                }
            }

    })}

    let button = document.querySelector('#continue_button');
    button.addEventListener('click', function go_to_the_check_answer() {
    check_answer(words_without_emphasis, words_emphasis, a, iter, statistic)
    this.removeEventListener('click', go_to_the_check_answer);


    });
}


    function check_answer(words_without_emphasis, words_emphasis, a, iter, statistic) {
        let word = document.querySelector('#word');
        let answer = document.querySelector('#answer');

        if (word.textContent == words_emphasis[a[iter]]) {

        answer.innerHTML = "✅ Правильно! " + words_emphasis[a[iter]];
        statistic["right_answer"]++;
        // make list with words where user give correct answer
        statistic["words_without_mistake"].push(words_emphasis[a[iter]]);
        }
        else{
          // make list with words where user give wrong answer
          statistic["words_with_mistake"].push(words_emphasis[a[iter]]);
          statistic["wrong_answer"]++;
          answer.innerHTML = "❌ Неправильно! " + words_emphasis[a[iter]];
        }
    word.textContent = "";
    iter++;

    let button = document.querySelector('#continue_button');
    button.addEventListener('click', function next_word() {
    if (iter <= 14){
    header.innerHTML = "";
    answer.innerHTML = "";
    get_word(words_without_emphasis, words_emphasis, a, iter, statistic);
    this.removeEventListener('click', next_word);
    }
    else{
    this.removeEventListener('click', next_word);
    let c = document.querySelector('#counter');
    c.innerHTML = ""
    answer.innerHTML = ""
    let end_message = "Правильні відповіді: " + statistic["right_answer"] + "</br>" +
    "Неправильні відповіді: " + statistic["wrong_answer"] + "</br>" +"Кінець. Тисни кнопку щоб зіграти ще раз"
    header.innerHTML = end_message

    // if user is authenticated send statistic data to views.py
    if (data.is_authenticated){
        sendData(statistic);
    }
    else{
    header.innerHTML = end_message + "</br>" + " Зареєструйтесь, щоб ваша статистика зберігалась";
    }
    button.addEventListener('click', function play_again() {
    header.innerHTML = ""

    play(words_without_emphasis, words_emphasis);
    this.removeEventListener('click', play_again);
    });
    }
    });
    }


function sendData(statistic) {

  $.ajax({
    type: "POST",
    url: "",
    data: {url:JSON.stringify(statistic), 'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,},
    dataType: "json",
    success: function(response) {
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
}
  });
}

