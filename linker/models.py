from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .tools import Link

import requests


class LinkModel(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=125)
    link = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    click_count = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    @staticmethod
    def anonymous_create(link, *args, **kwargs):
        lin = LinkModel.objects.filter(link=link)
        if lin.exists():
            return lin.first().shortcut
        lin = Link(link)
        link_title = lin.get_title()
        link_shortcut = lin.create_shortcut()
        LinkModel.objects.create(link=link, title=link_title, shortcut=link_shortcut)
        return link_shortcut

    @staticmethod
    def get_orginal_link(shortcut):
        lin = LinkModel.objects.get(shortcut=shortcut)
        lin.click_count += 1
        lin.save()
        return lin.link
