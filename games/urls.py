from django.urls import path
from .class_views.create_word import CreateWord
from .class_views.create_theme import CreateTheme

from . import views

app_name = "games"
urlpatterns = [
    path("", views.index, name="index"),
    path("theme/<int:theme_id>/", views.game_theme, name="game"),
    path("theme/random/", views.game_random, name="random_game"),
    path("word/new/", CreateWord.as_view(), name="new_word"),
    path("theme/new/", CreateTheme.as_view(), name="new_theme"),
]