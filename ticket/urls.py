from . import views
from django.urls import path

app_name = 'ticket'
urlpatterns = [
    path('', views.index, name='index'),
    path('search_ticket', views.ticket_search, name='search'),
    path('tickets_detail/<int:pk>', views.ticket_detail, name = 'detail')
]
