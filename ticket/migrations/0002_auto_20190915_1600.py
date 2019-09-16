# Generated by Django 2.2.5 on 2019-09-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='available_seat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cabin_class',
            field=models.CharField(blank=True, help_text='First Class, Economy, Premium, All, Business', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='departure_city',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='destination',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flight_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
