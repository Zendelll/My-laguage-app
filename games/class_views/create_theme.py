from django.conf import settings
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse, QueryDict
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from games.models import Word, Theme


class CreateTheme(View):
  

  def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    TEMPLATE = 'games/create_theme.html'

    words = list(Word.objects.filter(~Q(word_type="verb") | ( Q(word_type="verb") & Q(verb_type=0) )).order_by('word_type', 'word_name')) #we dont want verb forms to be here
    return render(request, TEMPLATE, {"words": words})
  
  #TODO: Change exceptions to error message
  def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    params = request.POST.dict()
    if not "theme-words[]" in params: raise Exception("No words")
    params["words"] = [Word.objects.get(pk=word_id) for word_id in request.POST.getlist("theme-words[]")]

    if not "theme-switch" in params:
      params["is_verb"] = False
    else:
      for word in params["words"]:
        if word.word_type != "verb": raise Exception("Not all word are verbs")
      params.pop("theme-switch")
      params["is_verb"] = True

    #TODO; Change hardcoded user to current after implementing auth
    params.pop("csrfmiddlewaretoken")
    params.pop("theme-words[]")
    theme = Theme(author=User.objects.get(username="vlada"), moderated=True, is_verb=params["is_verb"], name=params["name"])
    theme.save()
    theme.words.set(params["words"])
    
    return HttpResponseRedirect(reverse('games:new_theme'))