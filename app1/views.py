from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from app1.forms import *

# Create your views here.
class datarender(View):
    def get(self,request):
        d={'name':'kala'}
        return render(request,'datarender.html',d)


def insert(request):
    sfo=StudentForm()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            sfd.save()
            return HttpResponse('data inserted')
    return render(request,'insert.html',d)



class cbvinsert(View):
    def get(self,request):
        
        sfo=StudentForm()
        d={'sfo':'sfo'}
        return render(request,'cbvinsert.html',d)
    def post(self,request):
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
          sfd.save()
          return HttpResponse('cbv inserted')