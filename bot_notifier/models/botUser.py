from django.db.models import Model
from django.db.models.fields import CharField, BooleanField


class BotUser(Model):
    chat_id = CharField(max_length=10, unique=True)
    first_name = CharField(max_length=255, null=True, blank=True)
    username = CharField(max_length=255, null=True, blank=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.username or str(self.chat_id)