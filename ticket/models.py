from django.db import models

# Create your models here.
class Ticket(models.Model):
    flight_name = models.CharField(max_length= 200, blank = True, null = True)
    departure_city = models.CharField(max_length= 300, blank = True, null = True)
    destination = models.CharField(max_length= 300, blank = True, null = True)
    departure_date = models.DateField(blank = True, null = True)
    departure_time = models.TimeField(blank = True, null = True)
    arrival_date = models.DateField(blank = True, null = True)
    arrival_time =  models.TimeField(null = True, blank = True)
    cabin_class = models.CharField(max_length= 200, help_text= 'First Class, Economy, Premium, All, Business', blank = True, null = True)
    passenger = models.IntegerField( blank=True, null=True)
    number_children = models.IntegerField(null=True, blank=True )
    number_infant = models.IntegerField(null = True, blank=True)
    created = models.DateField(auto_now=True, blank = True, null = True)
    available_seat = models.IntegerField(blank = True, null = True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank = True, null = True)
    
    class Meta: 
        ordering = ('-created',)
            
    def __str__(self):
        return self.flight_name



