"""
#without html template
from django.http import HttpResponse

 
def index(request):
    return HttpResponse("YEAH, It is my first app and It is working")

"""
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'index.html'
class HomePageView1(TemplateView):
    template_name = 'h.html'
        