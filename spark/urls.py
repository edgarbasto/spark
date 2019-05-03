from django.urls import path

from . import views

app_name= 'spark'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:company_name>/', views.CompanyDetailView.as_view(), name='list'),
    path('<str:company_name>/<int:pk>/', views.ResultsView.as_view(), name='detail'),
    path('<str:company_name>/create', views.AnalysisCreate.as_view(), name='createanalysis'),
    
]

#    path('<str:company_name>/<int:pk>/import', views.import_inputs, name='import'),

'''
OLD URLS
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:company_name>/', views.listanalysis, name='List Analysis'),
    path('<str:company_name>/<int:analysis_id>/', views.detail, name='detail'),
    
]
'''
