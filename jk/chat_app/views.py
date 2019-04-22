from django.http import HttpResponse

def index(request):
    return HttpResponse("Yeah,It is my first app and It is working")

