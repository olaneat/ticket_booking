from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Ticket
from .forms import TicketForm
from django.core import serializers
# Create your views here.
def index(request):
    flight_form = TicketForm(request.POST)
    if request.method =='POST':
        if flight_form.is_valid():
            flight_form.save()
        return redirect(fight_result)
    else:
        flight_form = TicketForm()
    return render(request, 'ticket/index.html', {'flight_form': flight_form})

def ticket_search(request):
    #max_flights = 3
    tickets = Ticket.objects.all()
    q_set = serializers.serialize('json', tickets)
    return HttpResponse(q_set, content_type='application/json')
    data = {'results': list(tickets.values('departure_city', 'depature_date', 'destination', ))}
    return JsonResponse(data)

def flight_result(request):
    result = TicketForm.objects.filter(departure = departure_city, 
            arrival = destination).list(flight_name)
    
    return render(request, 'ticket/index.html', {'result': result} )
        

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
