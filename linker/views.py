from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import AnonymousLinkForm

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
