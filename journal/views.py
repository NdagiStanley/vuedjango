from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'days': [1, 2, 3],
    }
    return render(request, 'days.html', context)
