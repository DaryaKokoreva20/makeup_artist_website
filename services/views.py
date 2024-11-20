from django.shortcuts import render


def wedding_services(request):
    template = 'services/wedding.html'
    return render(request, template)


def evening_services(request):
    template = 'services/evening.html'
    return render(request, template)


def nude_services(request):
    template = 'services/nude.html'
    return render(request, template)


def thematic_services(request):
    template = 'services/thematic.html'
    return render(request, template)
