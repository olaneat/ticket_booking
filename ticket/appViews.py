from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
from .models import Ticket
from .serializers import TicketSerializer

class TicketList(generics.ListAPIView):
   queryset = Ticket.objects.all()
   serializer_class = TicketSerializer


class TicketDetail(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
