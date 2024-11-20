from django.shortcuts import render


def contacts(request):
    template = 'contacts/contacts.html'
    return render(request, template)
