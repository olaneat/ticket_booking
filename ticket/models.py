from django.db import models

# Create your models here.
class Ticket(models.Model):
    flight_name = models.CharField(max_length= 200)
    departure_city = models.CharField(max_length= 300)
    destination = models.CharField(max_length= 300)
    departure_date = models.DateTimeField()
    arrival_date = models.DateField(blank = True, null = True)
    cabin_class = models.CharField(max_length= 200, help_text= 'First Class, Economy, Premium, All, Business')
    passenger = models.IntegerField( blank=True)
    number_children = models.IntegerField( blank=True )
    number_infant = models.IntegerField(blank=True)
    created = models.DateField(auto_now=True)
    available_seat = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta: 
        ordering = ('-created',)
            
    def __str__(self):
        return self.flight_name



