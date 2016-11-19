from django.shortcuts import render
from django.http import HttpResponse

from .models import Color

# Create your views here.
def index(request):
	colors = Color.objects
	context = {'colors':colors}
	return render(request, 'rantest/index.html', context)
