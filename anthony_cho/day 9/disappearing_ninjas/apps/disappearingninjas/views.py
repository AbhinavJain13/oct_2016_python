from django.shortcuts import render

ninjas = {
    'blue': 'leonardo.jpg',
    'red': 'raphael.jpg',
    'purple': 'donatello.jpg',
    'orange': 'michelangelo.jpg'
}

# Create your views here.
def index(request):
    return render(request, 'disappearingninjas/index.html')

def ninja(request):
    context = {
        'ninjas': ninjas
    }
    return render(request, 'disappearingninjas/ninja.html', context)

def ninjas_color(request, color):
    which = {}
    if color:
        which[color] = ninjas[color]
    else:
        which[color] = 'notapril.jpg'
    context = {
        'ninjas': which
    }
    return render(request, 'disappearingninjas/ninja.html', context)
