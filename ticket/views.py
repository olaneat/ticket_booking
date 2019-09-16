from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Ticket
from .forms import TicketForm
from django.core import serializers
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

'''def ticket_search(request):
    #max_flights = 3
    tickets = Ticket.objects.all()
    q_set = serializers.serialize('json', tickets)
    return HttpResponse(q_set, content_type='application/json')
    data = {'results': list(tickets.values('departure_city', 'depature_date', 'destination', ))}
    return JsonResponse(data)
'''
def index(request):
    current_site = get_current_site(request)
    flight_form = TicketForm(request.POST)
    if request.method =='POST':
        if flight_form.is_valid():
            flight_list = dict()
            flight = Ticket.objects.all()
            flight_list['flight_list'] = Ticket.objects.filter(departure_city__contains =flight_form.cleaned_data['From']).filter(destination__contains=flight_form.cleaned_data['To'])
            flight_list['flight_form'] = TicketForm()
            flight_list['domain'] = current_site
            list(flight_list)
            return render(request, 'ticket/flight_result.html',  flight_list, )

    else:
        flight_form = TicketForm()
    return render(request, 'ticket/index.html', {'flight_form': flight_form})


def flight_result(request):
    result = Ticket.objects.filter(departure = departure_city, 
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
