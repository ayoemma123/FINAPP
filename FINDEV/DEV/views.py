from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import FinancialRecordForm


def home(request):

    transactions = models.Transaction.objects.all()

    context = {
        'transactions': transactions
    }

    return render(request, 'index.html', context=context)

def fill_form(request):


    form = FinancialRecordForm()

    if request.method == 'POST':
        form = FinancialRecordForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        
        else:

            return HttpResponse("There was an error in submitting the form. Please try again.")
        
    context = {
            'form': form
        }
    

    return render(request, 'form.html', context=context)