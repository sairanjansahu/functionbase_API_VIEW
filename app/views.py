from django.shortcuts import render
from rest_framework.response import Response,is_Aunthicated
from rest_framework.decorators import api_view,permission_classes
from app.serializers import *
from app.models import *

# Create your views here.

@api_view()
@permission_classes([is_Aunthicated])
def Employeejdata(request):
    EMD=Employee.objects.all()
    ESD=EmployeeMS(EMD,many=True)
    return Response(ESD.data)