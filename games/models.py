from django.db import models
from django.conf import settings

class Word(models.Model):
    word_name = models.CharField(
        max_length=26, 
        unique=True
    )
    main_translation = models.CharField(max_length=50)
    accepted_translation = models.JSONField(
        null=True, 
        blank=True
    )
    word_type = models.CharField(
        max_length=11, 
        choices=(
            ("noun", "Noun"),
            ("adjective", "Adjective"),
            ("verb", "Verb"),
            ("adverb", "Adverb"),
            ("preposition", "Preposition"),
            ("pronoun", "Pronoun")
        )
    )
    verb_base = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    ) #verb infinitive
    verb_type= models.IntegerField(
        blank=True, 
        null=True,
        choices=(
            ("0", "Infinitivo"),
            ("1", "Primera singular"),
            ("2", "Segunda singular"),
            ("3", "Tercera singular"),
            ("4", "Primera plural"),
            ("5", "Segunda plural"),
            ("6", "Tercera plural")
        )
    )
    verb_tense = models.CharField(
        max_length=8, 
        blank=True, 
        null=True,
        choices=(
            ("present", "present"),
            ("past", "past"),
            ("future", "future"),
            ("potent", "Potentional")
        )
    )
    gender = models.CharField(
        max_length=3, 
        blank=True, 
        null=True,
        choices=(
            ("m", "Masculino"),
            ("f", "Femenino"),
            ("mf", "Both")
        )
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    need_moderation = models.BooleanField(default=False)
    moderated = models.BooleanField(default=False)
    
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

