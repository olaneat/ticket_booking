from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Ticket
# Create your views here.
def index(request):
    ticket = Ticket.objects.all()
    return render(request, 'ticket/index.html', {'ticket': ticket})

def ticket_search(request):
    max_flights = 3
    tickets = Ticket.objects.all()[:max_flights]
    data = {'results': list(tickets.values('departure_city', 'depature_time', 'destination_city', 'return_date'))}
    return JsonResponse(data)

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    data = {"result":{
        'available seats': ticket.available_seat,
        'class': ticket.cabin_class,
        'departure': ticket.departure_date,
        'arrival_date': ticket.arrival_date,
        'cost': ticket.price
    }}
    return JsonResponse(data)