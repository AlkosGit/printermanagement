from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Printer, Acco
from django.db.models.functions import Lower

# Create your views here.
def index(request):
    return render(request, 'printer/index.html')

def printers(request):
    context = {
        #  convert to lower case for sorting
        'printers' : Printer.objects.all().order_by(Lower('name'))
    }
    return render(request, 'printer/printers.html', context)

def printer(request):
    printer_id = request.GET['id']
    printer = Printer.objects.get(pk=printer_id)
    context = {
        'printer' : printer
    }
    return render(request, 'printer/printer.html', context)

def accos(request):
    context = {
        #  convert to lower case for sorting
        'accos' : Acco.objects.all().order_by(Lower('name'))
    }
    return render(request, 'printer/accos.html', context)

def acco(request):
    acco_id = request.GET['id']
    acco = Acco.objects.get(pk=acco_id)
    context = {
        'acco' : acco,
        'printers' : acco.location.all().order_by(Lower('name'))
    }
    return render(request, 'printer/acco.html', context)