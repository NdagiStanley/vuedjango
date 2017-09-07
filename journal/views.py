from django.shortcuts import render


# Create your views here.
def index(request):
    # The content of context is rendered in the templates
    # using {{ }} delimiters
    context = {
        'days': [1, 2, 3],
    }
    return render(request, 'days.html', context)
