from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}: {self.amount}"
    

class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    Transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='types')

    def __str__(self):
        return self.name