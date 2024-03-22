from rest_framework import serializers
from .models import CompanyDetails


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = "__all__"