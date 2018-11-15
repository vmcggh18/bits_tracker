from django.db import models
from issues_list.models import Item


class Order(models.Model):
    """ Get User purchasing related information """
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    # return summary order
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    """ Get purchased items related information """
    order = models.ForeignKey(Order, null=False)
    item = models.ForeignKey(Item, null=False)
    upvote = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.upvote, self.item.name, self.item.price)
    
