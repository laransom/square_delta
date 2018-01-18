from django.http import HttpResponseNotFound
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import pdb
from models import Result


class ResultView(APIView):
    def get(self, request, format=None):
        number = int(request.GET.get('number', 0))
        if not number or number not in range(1, 101):
            return HttpResponseNotFound('<p>404: Number must be between 1 and 100</p>') 
            
        try:
            result_obj = Result.objects.get(number=number)
        except Result.DoesNotExist:
            result_obj = Result.get_result(number)
        
        result_obj.occurences += 1
        result_obj.save()
        
        return Response({"datetime": unicode(datetime.datetime.now()), "value": result_obj.solution, "number": number, "occurences": result_obj.occurences})
