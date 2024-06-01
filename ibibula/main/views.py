from django.shortcuts import render



def categories(request):
    context = {
        'content': 'хуй',
    }
    return render(request, 'main/index.html', context)