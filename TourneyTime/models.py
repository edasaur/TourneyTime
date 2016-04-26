from django.db import models
from django.utils import timezone

class Player(models.User):
    DCI = models.BigIntegerField(unique=True)

class Tournament(models.Model):
    name = models.CharField(max_length=500)
    player_ids = models.CharField()
    host_id = models.ForeignKey(Player)

class Match(models.Model):
    player1_id = models.ForeignKey(Player)
    player2_id = models.ForeignKey(Player)
    verified = models.BooleanField(initial=False)
    tournament_id = models.ForeignKey(Tournament)
    p1_wins = p2_losses = models.PositiveIntegerField()
    p1_losses = p2_wins = models.PositiveIntegerField()
    p1_ties = p2_ties = models.PositiveIntegerField()

