from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Company, Analysis


# Create your views here.



def index(request):
    company_list = Company.objects.all()
    template = loader.get_template('spark/index.html')
    context = {
        'company_list' : company_list,
    }
    return HttpResponse(template.render(context, request))

def listanalysis(request, company_name):
    return HttpResponse('Listing COMPANY analysis')

def detail(request, company_name, analysis_id):
    return HttpResponse('Listing companies')