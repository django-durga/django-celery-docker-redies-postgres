from django.db import models



class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, )
    address = models.TextField(max_length=100, blank=True, default='')
    email=models.EmailField(max_length=300, blank=False, )
    class Meta:
        ordering = ['created']
