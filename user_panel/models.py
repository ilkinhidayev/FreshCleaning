from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userpanel_orders")
    service_name = models.CharField(max_length=200)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
