from rest_framework import serializers
from ecomweb.structures.contact import *
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contacts
        fields = ['sno', 'name','email','subject', 'msg']
