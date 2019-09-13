from rest_framework import serializers
from .models import Ticket

class Ticketserializer(serializers.ModelSerializer):
    model = Ticket
    fields = '__all__'
