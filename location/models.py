from django.db import models


class Location(models.Model):
    """ Model for restaurant location """

    city = models.CharField(max_length=25, primary_key=True)
    country = models.CharField(max_length=25)
    address = models.CharField(max_length=50)

    class Meta:
        """ Order alphabetically """
        ordering = ['city']

    def __str__(self):
        return self.city


class Table(models.Model):
    """ Model for table booked """

    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField()
    capacity = models.IntegerField(default=2)

    class Meta:
        """ Order tables by number """
        ordering = ['number']

    def __str__(self):
        return self.number

