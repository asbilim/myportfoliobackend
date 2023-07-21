from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ["interest",'name','email','message']