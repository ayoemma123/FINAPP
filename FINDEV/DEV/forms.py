from django.forms import ModelForm
from .models import Transaction

class FinancialRecordForm(ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'