#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import path, include
from .views import HomeView, RedirectToLinkView

urlpatterns = [
    path('', HomeView.as_view()),
    path('<str:shortcut>/', RedirectToLinkView.as_view())
]
