from django.urls import path
from . import views
from .views import InvoicesCreateEditView, InvoicesDeleteView

# URL namespace -> invoices:<url_name>
app_name = 'invoices'

urlpatterns = [
    path('', views.invoices, name='list'),

    path('add/', InvoicesCreateEditView.as_view(), name='create'),

    path('<int:invoice_id>/edit/', InvoicesCreateEditView.as_view(), name='edit'),

    path('<int:invoice_id>/delete/', InvoicesDeleteView.as_view(), name='delete'),
]
