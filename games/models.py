from django.db import models
from django.conf import settings

# Create your models here.
class Word(models.Model):
    word_name = models.CharField(max_length=26, unique=True) #spanish word
    main_translation = models.CharField(max_length=50) #translation that will be shown
    accepted_translation = models.JSONField() #list of str - translations that also correct
    word_type = models.CharField(max_length=10)
    verb_base = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True) #verb infinitive, null if it is inf or not a verb
    verb_type= models.IntegerField(blank=True, null=True) #NULL, 0-beber, 1-bebo, 2-bebes, 3-bebe, 4-bebemos, 5-bebe'is, 6-beben
    verb_tense = models.CharField(max_length=8, blank=True, null=True) #NULL, inf, present, past, future
    gender = models.CharField(max_length=3, blank=True, null=True) #NULL, m, f, mf
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    need_moderation = models.BooleanField(default=False) #is there need to make it public
    moderated = models.BooleanField(default=False) #was it moderated and accepted
    
    def __str__(self) -> str:
        return f"{self.word_name.capitalize()} ({self.main_translation.capitalize()})"

class Theme(models.Model):
    name = models.CharField(max_length=26, unique=True)
    words = models.ManyToManyField(Word)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_verb = models.BooleanField(default=False) #is this theme for verb forms (true) or translation (false)
    need_moderation = models.BooleanField(default=False) #is there need to make it public
    moderated = models.BooleanField(default=False) #was it moderated and accepted

    def __str__(self) -> str:
        return f"[{'Спряжения' if self.is_verb else 'Перевод'}] {self.name.capitalize()}"

