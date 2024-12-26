from django.contrib import admin
from .models import Sentence

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    pass

