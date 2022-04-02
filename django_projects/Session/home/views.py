from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': 'started',
        'variable2': 'ended'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")

def services(request):
    return HttpResponse("Services Page")

def contact(request):
    return HttpResponse("Contacts Page")