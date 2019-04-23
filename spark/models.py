from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Analysis(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pub_date = models.DateField('date created')
    #YEAR definition
    _YEAR = ( (2016, '2016'),
              (2017, '2017'),
              (2018, '2018'),
              (2019, '2019'),
              (2020, '2020'),
              (2021, '2021'),
             )
    
    year = models.PositiveSmallIntegerField(
        choices = _YEAR
    )
    def __str__(self):
        ans = str(self.company) + ' - ' + str(self.year)
        return ans
    
    def get_absolute_url(self):
        return reverse('spark:list', kwargs={'company_name': self.company.name})


class Inputs(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    #PRICE
    price = models.FloatField(
        default=0
    )
    #CONSUMPTION
    consumption = models.FloatField(
        default=0
    )

    #MONTH definition
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

    _MONTH = ( (January, 'January'),
               (February, 'February'),
               (March,'March'),
               (April,'April'),
               (May,'May'),
               (June,'June'),
               (July,'July'),
               (August,'August'),
               (September,'September'),
               (October,'October'),
               (November,'November'),
               (December,'December'),
            )

    month = models.PositiveSmallIntegerField(
        choices = _MONTH
    )

    #PERIOD definition
    Ponta = 'Ponta'
    Cheia = 'Cheia'
    Vazio = 'Vazio'
    SuperVazio = 'SuperVazio'
    _PERIOD = (
        (Ponta, 'Ponta'),
        (Cheia, 'Cheia'),
        (Vazio, 'Vazio'),
        (SuperVazio, 'SuperVazio'),
        )

    period = models.CharField(
        max_length=20,
        choices=_PERIOD    
    )
    def __str__(self):
        ans = str(self.analysis) + ' - ' + str(self.month) + ' - ' + str(self.period)
        return ans
    
    