from django.db.models import Model
from django.db.models.fields import CharField, TextField, DateTimeField
from django.utils import timezone


class Sentence(Model):
    message = TextField()
    author = CharField(max_length=255, default="Kepfutsiy", null=True, blank=True)
    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.message