# models.py
from django.db import models
# class Hero(models.Model):

#     name = models.CharField(max_length=60)
#     alias = models.CharField(max_length=60)
#     def __str__(self):
#         return self.name


class medic_hypertable(models.Model):

    time=models.DateTimeField(primary_key=True)
    kit_id=models.CharField(max_length=16)
    pres_card=models.FloatField()
    frec_resp=models.FloatField()
    temp_corp=models.FloatField()
    caidas=models.FloatField()
    
    def __str__(self):
        return self.name