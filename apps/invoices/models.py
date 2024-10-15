from django.db import models

from clients.models import Client

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, related_name='invoices')
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Unpaid')
    description = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.client.business_name}"

    @property
    def net_amount(self):
        # Calculate the subtotal amount based on associated invoice items
        return sum(invoice_item.total_price for invoice_item in self.invoice_items.all())

class InvoiceItem(models.Model):
    UNIT_CHOICES = [
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('units', 'Units'),  # Default unit for anything that doesn't fit into time-based measurements
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='units')

    def __str__(self):
        return f"{self.description} (x{self.quantity} {self.get_unit_display()})"

    @property
    def total_price(self):
        # Calculate the total price for the item based on quantity and price per unit
        return self.quantity * self.price_per_unit