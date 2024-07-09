# En csvuploader/models.py
from django.db import models

class CSVData(models.Model):
    invoice_no = models.CharField(max_length=10)
    stock_code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    customer_id = models.FloatField()
    region = models.CharField(max_length=100)
    invoice_day = models.IntegerField()
    invoice_month = models.IntegerField()
    invoice_year = models.IntegerField()
    invoice_hour = models.IntegerField()
    total_sales = models.FloatField()
    sales_per_customer = models.FloatField()
    invoices_per_customer = models.FloatField()
    avg_sales_per_customer = models.FloatField()
    neg_invoices_per_customer = models.FloatField()

    def __str__(self):
        return self.invoice_no