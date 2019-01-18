from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany,\
                     Truck, Plane, Train,  FreightCompany, Driver
from .serializers import TruckSerializer, PlaneSerializer, TrainSerializer, \
     PlaneListSerializer,TrainListSerializer, TruckListSerializer, UserSerializer,DriverSerializer,\
     AirFreightCompanySerializer,RailwayFreightCompanySerializer,RoadFreightCompanySerializer, FreightCompanySerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import mixins
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


class DetailViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoadFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RoadFreightCompanySerializer
    queryset = RoadFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RailFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RailwayFreightCompanySerializer
    queryset = RailwayFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DriverViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TruckViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()


class PlaneViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class TrainViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = TrainSerializer
    queryset = Train.objects.all()
