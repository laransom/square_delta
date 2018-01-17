from tastypie.resources import ModelResource
from square_api.models import Result

class ResultResource(ModelResource):
    class Meta:
        queryset = Result.objects.all()
        resource_name = 'result'