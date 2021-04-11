from django.db import models
from django.contrib.auth import get_user_model

class LinkModel(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=125)
    link = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
