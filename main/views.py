from django.shortcuts import render

# Create your views here.
def mainpage(request):
    context = {
        'info': 1
    }
    return render(request, 'main/mainpage.html', context)