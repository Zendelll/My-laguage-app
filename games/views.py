from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Word, Theme
from random import choice, shuffle
from django.db.models import Q

def index(request) -> HttpResponse:
    themes_list = Theme.objects.order_by("name")    
    context = {"themes": themes_list}
    return render(request, "games/index.html", context)

#game with random words
def game_random(request) -> HttpResponse:
    CHOICE_NUMBER = 4

    words = list(Word.objects.filter(~Q(word_type="verb") | ( Q(word_type="verb") & Q(verb_type=0) ))) #we dont want verb forms to be here
    main_word = choice(words)
    main_word.word_name = main_word.word_name.capitalize()
    words.remove(main_word)
    translations = [main_word.main_translation]
    while (len(translations) < CHOICE_NUMBER):
        new_word = choice(words)
        translations.append(new_word.main_translation)
        words.remove(new_word)
    shuffle(translations)
    #output = f"{main_word.word_name}\n\n{' '.join([f'({w.main_translation})' for w in translations])}"
    context = {"main_word": main_word, "translations": translations}
    return render(request, "games/click_game.html", context)

#game based on theme
def game_theme(request: HttpRequest, theme_id) -> HttpResponse:
    CHOICE_NUMBER = 4
    if not isinstance(theme_id, int): return index(request) #SQL injections? Try it with integer! 
    
    #initiate session variables
    if not "theme_used_words" in request.session:
        request.session["theme_used_words"] = []
        request.session["theme_success"] = 0
    if "theme_success" in request.GET:  request.session["theme_success"] += 1 #count right answers

    theme = get_object_or_404(Theme, pk=theme_id)
    if len(request.session["theme_used_words"]) >= 0 and len(request.session["theme_used_words"]) < theme.words.count():
        if len(request.session["theme_used_words"]) == 0:
            words = list(theme.words.all())
        else:
            condition_string = ""
            for word_id in request.session["theme_used_words"]:
                condition_string += f"AND NOT word_id = {word_id} "
            words = list(theme.words.raw(f"SELECT word_id as id FROM games_theme_words WHERE theme_id = {theme_id} {condition_string}"))
        
        word = choice(words)
        request.session["theme_used_words"].append(word.id)
        request.session.save()
        translations = [word.main_translation]
        word_list = list(theme.words.all())
        word_list.remove(word)
        while len(translations) < CHOICE_NUMBER and len(word_list) > 0:
            new_word = choice(word_list)
            translations.append(new_word.main_translation)
            word_list.remove(new_word)
        shuffle(translations)
        return render(request, "games/click_game.html", {"main_word": word, "translations": translations, "theme_id": theme_id})
    
    
    context = {
            "successes": request.session["theme_success"], 
            "words": len(request.session["theme_used_words"]), 
            "percent": int(request.session["theme_success"] / len(request.session["theme_used_words"]) * 100),
            "theme_id": theme_id
        }
    request.session["theme_used_words"] = []
    request.session["theme_success"] = 0
    request.session.save()
    return render(request, "games/click_game_win.html", context)
        

def new_word(request) -> HttpResponse:
    infinitives = list(Word.objects.filter(verb_type="0").order_by('word_name'))
    context = {"infinitives": infinitives}
    return render(request, "games/create_word.html", context)