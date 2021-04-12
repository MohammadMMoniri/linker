from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views import View

import re

from .forms import AnonymousLinkForm
from .models import LinkModel


class HomeView(View):
    def get(self, request):
        form = AnonymousLinkForm() 
        return render(request, 'html/home.html', {'form': form})

    def post(self, request):
        form = AnonymousLinkForm(request.POST)
        if form.is_valid():
            message = {
                "type": "success",
                "data": "ur link created successfully"
            }
            return render(request, 'html/home.html', {"form": form, "message":message})
        else:
            message = {
                "type": "danger",
                "data": "bad link"
            }
            return render(request, 'html/home.html', {"form": form, "message":message})


class RedirectToLinkView(View):
    def get(self, request, shortcut):
        return redirect(LinkModel.get_orginal_link(shortcut=shortcut))
