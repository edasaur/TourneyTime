from django.contrib import admin
from .models import *

for model in (Player, Match, Tournament):
    admin.site.register(model)
