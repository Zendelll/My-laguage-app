from django.conf import settings
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse, QueryDict
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User

from games.models import Word


class CreateWord(View):
  

  def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    TEMPLATE = 'games/create_word.html'

    infinitives = list(Word.objects.filter(verb_type="0").order_by('word_name'))
    return render(request, TEMPLATE, {"infinitives": infinitives})
  
  def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    params = request.POST.dict()
    if not "accepted_translation" in params:
      params["accepted_translation"] = []
    else:
      params["accepted_translation"] = params["accepted_translation"].strip().split(", ")
    if "verb_base" in params: params["verb_base"] = Word.objects.get(id=params["verb_base"])
    #TODO; Change hardcoded user to current after implementing auth
    params.pop("csrfmiddlewaretoken")
    word = Word(author=User.objects.get(username="vlada"), moderated=True, **params)
    word.save()
    return HttpResponseRedirect(reverse('games:new_word'))