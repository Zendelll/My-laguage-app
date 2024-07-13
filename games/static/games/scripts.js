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

    static switch_with_text(text_id_1, text_id_2, switch_id) {
        var elements = [document.querySelector(`#${text_id_1}`), document.querySelector(`#${text_id_2}`)]
        if (document.querySelector(`#${switch_id}`).checked) {
            elements[0].classList.add("text-muted");
            elements[1].classList.remove("text-muted");
        } else {
            elements[0].classList.remove("text-muted");
            elements[1].classList.add("text-muted");
        }
    }
}





