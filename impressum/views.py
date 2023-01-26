from django.shortcuts import render


def impressum(request):
    return render(request, "impressum.html")
