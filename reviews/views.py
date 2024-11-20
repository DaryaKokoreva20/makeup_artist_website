from django.shortcuts import render


def all_reviews(request):
    template = 'reviews/all.html'
    return render(request, template)


def add_review(request):
    template = 'reviews/add.html'
    return render(request, template)
