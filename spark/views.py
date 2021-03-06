#from django.shortcuts import render, get_object_or_404, get_list_or_404
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Company, Analysis, Inputs
from .forms import UploadFileForm
#import openpyxl


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
    fields = ['year']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = Company.objects.get(name=self.kwargs['company_name'])
        obj.pub_date = timezone.now()
        obj.save()
        return HttpResponseRedirect(reverse('spark:list', args=[self.kwargs['company_name']]))
    

class ResultsImport(CreateView):
    model = Inputs
    fields = [] 
    def form_valid(self, form):
        obj = form.save(commit=False)
        #excel_file = request.FILES["excel_file"]
        obj.save()


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
def import_inputs(request, company_name, pk):
    message=''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            try:
                import pandas as pd
                df = pd.read_excel(excel_file, index_col=None, header=None, dtype={'period':str, 'consumption':int, 'price':float})
                year = df[1][1]
                df.columns = ['Descritivo', 'Consumo', 'Preco', 'Total']
                df.dropna(axis=0, thresh=1, inplace=True)
                mes=0
                for row in df.itertuples(index=True, name='Teste'):
                    meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
                    periodo = ['Ponta', 'Cheio', 'Vazio', 'Super Vazio']
                    try:
                        #meses.index(getattr(row, 'Descritivo'))
                        mes = meses.index(getattr(row, 'Descritivo')) + 1
                        print('Mês: {}'.format(mes))
                    except ValueError:
                        if mes >= 1 and mes <= 12:
                            try:
                                #periodo.index(getattr(row, 'Descritivo'))
                                if (periodo.index(getattr(row, 'Descritivo')) is not None):
                                    obj=Inputs(
                                        analysis=pk, 
                                        price=getattr(row, 'Preco').value, 
                                        consumption=getattr(row, 'Consumo').value, 
                                        month=mes, period=periodo.index(getattr(row, 'Descritivo')
                                    )
                                    #obj.save()
                                    print('Para o {} mes, periodo: {}, consumo: {}, preço: {}'.format(mes, getattr(row, 'Descritivo'), getattr(row, 'Consumo'), getattr(row, 'Preco')))
                                    type(getattr(row, 'Consumo'))
                                    type(getattr(row, 'Preco'))
                            except ValueError:
                                print('')
                        #False        
                    #print('Para o {} mes, periodo: {}, consumo: {}, preço: {}'.format(mes, getattr(row, 'Descritivo'), getattr(row, 'Consumo'), getattr(row, 'Preco')))
        else:
            message='Invalid Entries'
    else:
        form= UploadFileForm()
    return render(request,'spark/import.html', {'form':form,'message':message})
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