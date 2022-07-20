# Register your models here.
import datetime

from django.contrib import admin
from django.db import connections
from django.http import HttpResponse
import csv
from appqmx.models import KhxT, HtxT, YhxT, CbxT, jhxT
from django.contrib import messages
from django.utils.translation import ngettext

