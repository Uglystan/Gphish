from datetime import datetime
from django.db import models

# Create your models here.
class SignIn(models.Model):
    email = models.EmailField()
    password_strength = models.IntegerField()  # Score de zxcvbn
    guesses = models.IntegerField()  # Nombre de tentatives estimées
    crack_time_display_offline_fast_hashing_10_milliards_per_second = models.CharField(max_length=100)
    crack_time_display_offline_slow_hashing_10000_per_second = models.CharField(max_length=100)
    crack_time_display_online_10_per_seconde = models.CharField(max_length=100)
    crack_time_display_online_throttling_100_per_hour = models.CharField(max_length=100)
    feedback_suggestions = models.TextField(null=True, blank=True)  # Suggestions d'amélioration
    feedback_warning = models.TextField(null=True, blank=True)  # Avertissement sur le mot de passe
    sequence_rank = models.IntegerField(null=True, blank=True)  # Rang du mot de passe dans le dictionnaire
    sequence_pattern = models.CharField(max_length=100, null=True, blank=True)  # Motif identifié
    sequence_reversed = models.BooleanField(null=True, blank=True)  # Si le mot de passe est inversé
    sequence_l33t = models.BooleanField(null=True, blank=True)  # Si le mot de passe contient des substitutions leet
    nbr_upper = models.IntegerField() # Nombre de majuscule
    nbr_lower = models.IntegerField() # Nombre de minuscule
    nbr_nbr = models.IntegerField() # Nomnbre de nombre
    length = models.IntegerField() # Taille
    nbr_special = models.IntegerField() # Nombre de caractère spécial
    date_time = models.DateTimeField(auto_now_add=True)
    client_ip = models.CharField(max_length=32, null=True)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.email