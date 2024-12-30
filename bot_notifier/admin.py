from django.contrib import admin
from .models import Sentence, BotUser


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    pass

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    pass
