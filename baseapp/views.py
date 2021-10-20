from django.shortcuts import render
from django.views import generic
from .models import Email
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request,'baseapp/home.html',{})

class saveEmail(generic.CreateView):
    model=Email
    fields='__all__'
    template_name='baseapp/home.html'
    success_url=reverse_lazy('home')
