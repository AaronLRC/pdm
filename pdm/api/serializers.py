# serializers.py
from rest_framework import serializers

# from api.models import Hero
from .models import medic_hypertable

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')

class medichypertableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = medic_hypertable
        fields = ('time', 'kit_id','pres_card','frec_resp','temp_corp','caidas')