from django.http import HttpResponse


def description(request):
    return HttpResponse('<h2>О Проект</h2>')
