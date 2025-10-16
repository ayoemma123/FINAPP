from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):

    transactions = models.Transaction.objects.all()

    context = {
        'transactions': transactions
    }

    return render(request, 'index.html', context=context)