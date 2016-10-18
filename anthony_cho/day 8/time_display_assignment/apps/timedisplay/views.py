from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    date = now.strftime('%b %m %Y')
    time = now.strftime('%-I:%M %p')
    context = {
        'date': date,
        'time': time
    }
    print("time is", now)
    return render(request, 'timedisplay/index.html', context)
