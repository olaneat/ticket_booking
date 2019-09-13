from django.db import models

# Create your models here.
class Ticket(models.Model):
    departure_city = models.CharField(max_length= 300)
    destination_city = models.CharField(max_length= 300)
    departure_date = models.DateTimeField()
    arrival_date = models.DateField()
    cabin_class = models.CharField(max_length= 200, help_text= 'First Class, Economy, Premium, All, Business')
    number_adults = models.IntegerField()
    number_children = models.IntegerField()
    number_infant = models.IntegerField()
    created = models.DateField(auto_now=True)
    available_seat = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta: 
        ordering = ('-created',)
            
    def __str__(self):
        return self.departure_city



