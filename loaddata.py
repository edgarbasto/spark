from spark.models import Company, Analysis, Inputs
from django.utils import timezone
 c = Company.objects.get(pk=1)
 c.analysis_set.create(pub_date=timezone.now(), year=2016)
 c.analysis_set.create(pub_date=timezone.now(), year=2017)
 c.analysis_set.create(pub_date=timezone.now(), year=2018)
