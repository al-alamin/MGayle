from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def destination(request, place_name):
    template = None
    if place_name == 'boundary-waters':
        template = 'destination/boundary_waters.html'
    elif place_name == 'rocky-mountains':
        template = 'destination/rocky_mountains.html'
    elif place_name == 'appalachian-trail':
        template = 'destination/appalachian_trail.html'
    elif place_name == 'superior-hiking-trail':
        template = 'destination/superior_hiking_trail.html'

    return render(request, template)
