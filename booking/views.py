from django.shortcuts import render


def booking_form(request):
    return render(request, 'booking/form.html')
