from django.shortcuts import render


def official_site(request):
    return render(request, 'officialsite/computer/home.html', dict())
