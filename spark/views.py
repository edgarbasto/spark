#from django.shortcuts import render, get_object_or_404, get_list_or_404
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Company, Analysis, Inputs
import pandas as pd
import openpyxl


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'spark/index.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.all()

class CompanyDetailView(generic.ListView):
    template_name= 'spark/companydetail.html'
    def get_queryset(self, *args, **kwargs):
        c = Company.objects.get(name=self.kwargs['company_name'])
        return  Analysis.objects.filter(company= c.id)

class AnalysisCreate(CreateView):
    model = Analysis
    model.company = self.kwargs['company_name']
    fields = ['year', 'pub_date']
    #success_url = "/spark/"
    

class ResultsView(generic.ListView):
    template_name= 'spark/detail.html' 
    context_object_name = 'object'
    def get_queryset(self, *args, **kwargs):
         c = Company.objects.get(name=self.kwargs['company_name'])
         a = Analysis.objects.get(pk=self.kwargs['pk'])
         if a.company.id == c.id:
             return Inputs.objects.filter(analysis=a.id)
    '''
    model = Inputs
    template_name= 'spark/detail.html' 
    
    '''





'''
def index(request):
    company_list = Company.objects.all()
    template = loader.get_template('spark/index.html')
    context = {
        'company_list' : company_list,
    }
    return HttpResponse(template.render(context, request)) 
    

def listanalysis(request, company_name):
    c = Company.objects.get(name=company_name)
    analysis_list = get_list_or_404(Analysis, company=c.id) 
    return render(request, 'spark/listanalysis.html', {'analysis_list':analysis_list})
    #return HttpResponse(' {c.name}')

#def detail(request, company_name, analysis_id):
#    return render(request, 'spark/detail.html')
    #return HttpResponse('Listing details')



def detail(request, company_name, analysis_id):
    if "GET" == request.method:
        context = {
            'company_name':company_name,
            'analysis_id':analysis_id
        }
        return render(request, 'spark/detail.html', context)
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["base"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        context =  {
            'company_name':company_name,
            'analysis_id':analysis_id,
            "excel_data":excel_data
            }
        
        return render(request, 'spark/detail.html', context)

'''