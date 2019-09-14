from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['departure_city', 'destination', 'departure_date', 'passenger' ]