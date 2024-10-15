from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .models import Client

def clients(request: HttpRequest) -> HttpResponse:
    # search is a query param
    search_query_param = request.GET.get('search', '')

    clients = Client.objects.filter(business_name__icontains=search_query_param)

    return render(
        request, 
        'clients_list.html', 
        context = { 'search': search_query_param, 'clients': clients }
    )

class ClientsCreateEditView(TemplateView):
    template_name = 'clients_create_edit.html'

    def get(self, request: HttpRequest, client_id: int = None) -> HttpResponse:
        if client_id:
            client = Client.objects.get(id=client_id)
            return render(
                request, 
                self.template_name, 
                context = { 'client_id': client_id, 'client': client },
                status=200
            )
        else:
            return render(request,  self.template_name, status=200)

    def post(self, request: HttpRequest, client_id: int = None) -> HttpResponse:
        
        if client_id:
            '''Update client'''
            client = Client.objects.get(id=client_id)
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    setattr(client, key, value)
            client.save()
        else:
            '''Create client'''
            payload = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}
            Client.objects.create(**payload)
        # Handle form submission
        return redirect('clients:list')

class ClientsDeleteView(View):
    def get(self, request: HttpRequest, client_id: int) -> HttpResponse:
        client = Client.objects.get(id=client_id)
        client.is_active = not client.is_active
        client.save()

        return redirect('clients:list')
    