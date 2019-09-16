from django import forms
from .models import Ticket

class TicketForm(forms.Form):
    From = forms.CharField(label= 'Departure', max_length= 150)
    To = forms.CharField(max_length=150, label='Arrival')
    passenger = forms.IntegerField(label='Number of Ticket', initial=1 )
    date = forms.DateField( label='Travel Date', required=True)