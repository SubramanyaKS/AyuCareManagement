from rest_framework import serializers 
from AyucareApp.models import Ayucare, User

class AyucareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayucare
        fields =('id','productname','details','cure','availability','price','manufacturedate','expiredate')

#class UserSerializer(serializers.ModelSerializer):
#    class Meta: 
 #       model = User
 #       fields =('id','username','email')

