import datetime
from dateutil.relativedelta import relativedelta
from django.test import TestCase

# Create your tests here.
today = datetime.datetime.today()
use_date = today+relativedelta(months=+1)
print(use_date.strftime('%Y-%m'))
