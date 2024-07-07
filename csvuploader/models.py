# En csvuploader/models.py
from django.db import models

class CSVData(models.Model):
    invoice_no = models.CharField(max_length=20)
    stock_code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    invoice_date = models.DateTimeField()
    unit_price = models.FloatField()
    customer_id = models.IntegerField()
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.invoice_no