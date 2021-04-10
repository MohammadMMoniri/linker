#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import path, include
from .views import HomeView

urlpatterns = [
 path('', HomeView.as_view())
]
