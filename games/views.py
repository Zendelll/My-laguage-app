from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    translations = [main_word]
    while (len(translations) < CHOICE_NUMBER):
        new_word = choice(words)
        translations.append(new_word)
        words.remove(new_word)
    shuffle(translations)
    #output = f"{main_word.word_name}\n\n{' '.join([f'({w.main_translation})' for w in translations])}"
    context = {"main_word": main_word, "translations": translations}
    return render(request, "games/click_game.html", context)

#game based on theme
def game_theme(request, theme_id) -> HttpResponse:
    question = get_object_or_404(Theme, pk=theme_id)
    return render(request, "polls/detail.html", {"question": question})

def new_word(request) -> HttpResponse:
    infinitives = list(Word.objects.filter(verb_type="0").order_by('word_name'))
    context = {"infinitives": infinitives}
    return render(request, "games/create_word.html", context)