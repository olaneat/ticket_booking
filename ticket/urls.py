from . import views
from django.urls import path
from .appViews import TicketList, TicketDetail


app_name = 'ticket'
urlpatterns = [
    path('', views.index, name='index'),
    path('available_tickets', TicketList.as_view(), name='available_tickets'),
    path('available_tickets/<int:pk>', TicketDetail.as_view(), name='available_tickets')
]

