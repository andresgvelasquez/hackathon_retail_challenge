# En csvuploader/models.py
from django.db import models

class CSVData(models.Model):
    invoice_no = models.CharField(max_length=10)
    stock_code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    invoice_day = models.IntegerField()
    invoice_month = models.IntegerField()
    invoice_year = models.IntegerField()
    invoice_hour = models.IntegerField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    sales_per_customer = models.DecimalField(max_digits=10, decimal_places=2)
    invoices_per_customer = models.DecimalField(max_digits=10, decimal_places=2)
    avg_sales_per_customer = models.FloatField()
    neg_invoices_per_customer = models.IntegerField()

    def __str__(self):
        return self.invoice_no