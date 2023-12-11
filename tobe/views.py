from django.shortcuts import render

from .models import Tobe  
from django.views import generic


class TobeList(generic.ListView):
    model = Tobe
    
class TobeDetail(generic.DetailView):
    model = Tobe 
       
class TobeDelete(generic.DeleteView):
    model = Tobe 
    fields = '__all__'
    success_url = '/tobe/tobe/'   
    
class TobeCreate(generic.CreateView):
    model = Tobe 
    fields = '__all__'
    success_url = '/tobe/tobe/'   
    
class TobeEdit(generic.UpdateView):
    model = Tobe 
    fields = '__all__'
    success_url = '/tobe/tobe/'  
    templatename = 'tobe/edit.html'