from django.urls import path

from . import views

app_name = "games"
urlpatterns = [
    path("", views.index, name="index"),
    path("theme/<int:theme_id>/", views.game_theme, name="game"),
    path("theme/random/", views.game_random, name="random_game"),
]