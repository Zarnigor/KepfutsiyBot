from django.db.models import Model
from django.db.models.fields import CharField, BooleanField, TextField, DateTimeField
from django.utils import timezone
from django.utils.timezone import now

class BotUser(Model):
    chat_id = CharField(max_length=10, unique=True)
    first_name = CharField(max_length=255, null=True, blank=True)
    username = CharField(max_length=255, null=True, blank=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.username or str(self.chat_id)


class Sentence(Model):
    message = TextField()
    author = CharField(max_length=255, default="Kepfutsiy", null=True, blank=True)
    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(auto_now=True)


