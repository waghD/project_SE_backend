from django.http import HttpResponse
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany,\
                     Truck, Plane, Train, Destination, FreightCompany
from .serializers import TruckSerializer, PlaneSerializer, TrainSerializer, \
    DestinationSerializer, PlaneListSerializer,TrainListSerializer, TruckListSerializer,\
    AirFreightCompanySerializer,RailwayFreightCompanySerializer,RoadFreightCompanySerializer, FreightCompanySerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import mixins


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


class DetailViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin, GenericViewSet):
    pass


class FreighterList(ReadOnlyModelViewSet):
    serializer_class = FreightCompanySerializer
    queryset = FreightCompany.objects.all()


class PlaneListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = PlaneListSerializer
    queryset = Plane.objects.all()


class TrainListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TrainListSerializer
    queryset = Train.objects.all()


class TruckListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TruckListSerializer
    queryset = Truck.objects.all()


class AirFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = AirFreightCompanySerializer
    queryset = AirFreightCompany.objects.all()


class RoadFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RoadFreightCompanySerializer
    queryset = RoadFreightCompany.objects.all()


class RailFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RailwayFreightCompanySerializer
    queryset = RailwayFreightCompany.objects.all()


class TruckViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()


class PlaneViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class TrainViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = TrainSerializer
    queryset = Train.objects.all()


class DestinationViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()


