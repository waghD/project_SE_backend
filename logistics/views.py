from django.http import HttpResponse
from .models import FreightCompany,Truck,Region
from .serializers import FreightCompanySerializer,TruckSerializer, RegionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'freighters': reverse('freighter-list', request=request, format=format)
    })


class FreighterViewSet(ModelViewSet,NestedViewSetMixin):
    serializer_class = FreightCompanySerializer
    queryset = FreightCompany.objects.all()


class TruckViewSet(ModelViewSet,NestedViewSetMixin):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()


class DestinationViewSet(ModelViewSet,NestedViewSetMixin):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


