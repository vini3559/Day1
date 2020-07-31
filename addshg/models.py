from django.db import models
from django.utils import timezone

# Create your models here.
class shg(models.Model):
    objects = models.Manager()
    Name = models.CharField(max_length=20)
    Activity = models.CharField(max_length=20)
    Amount = models.IntegerField()
    Woman_beneficiaries = models.IntegerField()
    Location = models.TextField()
    TimePeriod = models.DecimalField(max_digits=4, decimal_places=2)
    Rate = models.DecimalField(max_digits=4, decimal_places=2)
    Registration_id_imo = models.CharField(max_length=10)
    BalanceAmount=models.IntegerField(default=0)
    phno=models.IntegerField(max_length=10,default=0)


class installments(models.Model):
    objects = models.Manager()
    Name = models.CharField(max_length=20)
    Installments = models.IntegerField()
    Date = models.DateField(default=timezone.now)
    Registration_id_imo = models.CharField(max_length=10)

