"""
#without html template
from django.http import HttpResponse

 
def index(request):
    return HttpResponse("YEAH, It is my first app and It is working")

"""
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'index.html'