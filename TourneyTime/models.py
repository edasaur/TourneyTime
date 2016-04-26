from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DCI = models.BigIntegerField(unique=True)

class Tournament(models.Model):
    name = models.CharField(max_length=500)
    player_ids = models.CharField(max_length=5000)
    host_id = models.ForeignKey(Player)

class Match(models.Model):
    player1_id = models.ForeignKey(Player, related_name='p1_id')
    player2_id = models.ForeignKey(Player, related_name='p2_id')
    verified = models.BooleanField(default=False)
    tournament_id = models.ForeignKey(Tournament)
    p1_wins = models.PositiveIntegerField()
    p2_wins = models.PositiveIntegerField()
    p1_losses = models.PositiveIntegerField()
    p2_losses = models.PositiveIntegerField()
    p1_ties = models.PositiveIntegerField()
    p2_ties = models.PositiveIntegerField()

