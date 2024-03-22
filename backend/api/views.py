from django.shortcuts import render
from .models import CompanyDetails
from .serializers import CompanySerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class CompanyView(ListCreateAPIView):
    queryset = CompanyDetails.objects.all()
    serializer_class = CompanySerializer
    print(queryset,'lllllllllllllllllllllllllllllllllll')