from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    reverse_text = request.GET['usertext'][::-1]
    return render(request, 'reverse.html', {'reverse_text': reverse_text})
