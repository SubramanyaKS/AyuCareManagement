from rest_framework import serializers 
from AyucareApp.models import Ayucare

class AyucareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayucare
        fields =('id','productname','details','cure','availability','price','manufacturedate','expiredate')
