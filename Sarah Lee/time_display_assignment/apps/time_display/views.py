from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
     context = {
     "idontknow" : datetime.now()
     }
     return render(request, 'time_display/page.html', context)
