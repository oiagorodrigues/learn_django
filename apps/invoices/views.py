from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .models import Invoice

def invoices(request: HttpRequest) -> HttpResponse:
    # search is a query param
    search_query_param = request.GET.get('search', '')

    invoices = Invoice.objects.filter(name__icontains=search_query_param)

    return render(
        request, 
        'invoices_list.html', 
        context = { 'search': search_query_param, 'invoices': invoices }
    )

class InvoicesCreateEditView(TemplateView):
    template_name = 'invoices_create_edit.html'

    def get(self, request: HttpRequest, invoice_id: int = None) -> HttpResponse:
        if invoice_id:
            invoice = Invoice.objects.get(id=invoice_id)
            return render(
                request, 
                self.template_name, 
                context = { 'invoice_id': invoice_id, 'invoice': invoice },
                status=200
            )
        else:
            return render(request,  self.template_name, status=200)

    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        Invoice.objects.create(**kwargs)
        # Handle form submission
        return redirect('invoices:list')
    
class InvoicesDeleteView(View):
    def get(self, request: HttpRequest, invoice_id: int) -> HttpResponse:
        invoice = Invoice.objects.get(id=invoice_id)
        invoice.delete()
        return render(request, 'invoices_list.html', status=204)
    