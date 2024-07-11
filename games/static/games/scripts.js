class Utils {
    static set_success_color(element) {
        if (element.constructor === Array) {
            for (var i = 0; i < element.length; i++) {
                element[i].classList.add('bg-success');
            }
        } else {
            element.classList.add('bg-success');
        }
    }

    static set_error_color(element) {
        if (element.constructor === Array) {
            for (var i = 0; i < element.length; i++) {
                element[i].classList.add('bg-danger');
            }
        } else {
            element.classList.add('bg-danger');
        }
    }
    
    static shake(element) {
        element.classList.remove('shake');
        void element.offsetWidth;
        element.classList.add('shake');
    }
    
    static change_url(element, url) {
        if (element.constructor === Array) {
            for (var i = 0; i < element.length; i++) {
                element[i].href = url
            }
        } else {
            element.href = url
        }
    }

    static disable_or_enable_elements(element, disable=true) {
        for (var i = 0; i < element.length; i++) {
            element[i].disabled = disable
        }
    }
}

class ChoiceGame {
    static choice_game_check(url) {
        var selectedChoice = document.querySelector('input[name="choice"]:checked')
        var quizButton = document.getElementById("quizButton");

        if (!selectedChoice) {
            var quizForm = document.getElementById("quizForm");
            Utils.shake(quizForm)
        } 
        else if ( selectedChoice && selectedChoice.value == "True") {
            Utils.set_success_color([document.getElementById("quizHeader"), quizButton]);
            Utils.disable_or_enable_elements(document.querySelectorAll('[name="choice"]'));
            quizButton.innerHTML = "Далее";
            setTimeout(Utils.change_url, 100, quizButton, url+"?theme_success=0");

        } 
        else {
            if (quizButton.innerHTML != "Далее") {
                var quizForm = document.getElementById("quizForm");
                Utils.shake(quizForm)
            }
            
            if (!url.includes("random")) {
                Utils.set_error_color([document.getElementById("quizHeader"), quizButton]);
                Utils.disable_or_enable_elements(document.querySelectorAll('[name="choice"]'));
                quizButton.innerHTML = "Далее";
                setTimeout(Utils.change_url, 100, quizButton, url);
            }
        }
        
    
        
    }
}





