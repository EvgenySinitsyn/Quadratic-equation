from django.shortcuts import render
from .forms import IndexForm


def index(request):
    form = IndexForm()
    return render(request, 'js_app/index.html', {'form': form})
