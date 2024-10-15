from django.urls import path
from . import views
from .views import ClientsCreateEditView, ClientsDeleteView

# URL namespace -> clients:<url_name>
app_name = 'clients'

urlpatterns = [
    path('', views.clients, name='list'),

    path('add/', ClientsCreateEditView.as_view(), name='create'),

    path('<int:client_id>/edit/', ClientsCreateEditView.as_view(), name='edit'),

    path('<int:client_id>/delete/', ClientsDeleteView.as_view(), name='delete'),
]
