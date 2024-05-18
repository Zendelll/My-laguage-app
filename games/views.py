from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word, Theme
from random import choice, shuffle

# Create your views here.
def index(request) -> HttpResponse:
    themes_list = Theme.objects.order_by("name")    
    context = {"themes": themes_list}
    return render(request, "games/index.html", context)

#game with random words
def game_random(request) -> HttpResponse:
    words = list(Word.objects.all())
    main_word = choice(words)
    main_word.word_name = main_word.word_name.capitalize()
    words.remove(main_word)

    translations = [main_word]
    while (len(translations) < 4):
        new_word = choice(words)
        translations.append(new_word)
        words.remove(new_word)
    
    shuffle(translations)
    #output = f"{main_word.word_name}\n\n{' '.join([f'({w.main_translation})' for w in translations])}"
    context = {"main_word": main_word, "translations": translations}
    return render(request, "games/click_game.html", context)

#game based on thematic
def game_theme(request, theme_id) -> HttpResponse:
    question = get_object_or_404(Theme, pk=theme_id)
    return render(request, "polls/detail.html", {"question": question})