from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany,\
                     Truck, Plane, Train,  FreightCompany, Driver, Features
from .serializers import TruckSerializer, PlaneSerializer, TrainSerializer, FeatureSerializer, \
     PlaneListSerializer,TrainListSerializer, TruckListSerializer, UserSerializer,DriverSerializer,\
     AirFreightCompanySerializer,RailwayFreightCompanySerializer,RoadFreightCompanySerializer, FreightCompanySerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import mixins
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions,filters
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


class DetailViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FreighterList(ReadOnlyModelViewSet):
    serializer_class = FreightCompanySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'location', 'permissions',)
    search_fields = ('name','type', 'location','permissions',)
    queryset = FreightCompany.objects.all()


class PlaneListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = PlaneListSerializer

    def get_queryset(self):
        queryset = Plane.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class TrainListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TrainListSerializer

    def get_queryset(self):
        queryset = Train.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class TruckListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TruckListSerializer

    def get_queryset(self):
        queryset = Truck.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class FeautureListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = FeatureSerializer
    queryset = Features.objects.all()


class AirFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = AirFreightCompanySerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    search_fields = ('name', 'type', 'location', 'permissions',)
    filter_fields = ('name', 'type', 'location', 'permissions',)
    queryset = AirFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoadFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RoadFreightCompanySerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'location', 'permissions',)
    search_fields = ('name', 'type', 'location', 'permissions',)
    queryset = RoadFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RailFreighterViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = RailwayFreightCompanySerializer
    queryset = RailwayFreightCompany.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'location', 'permissions',)
    search_fields = ('name', 'type', 'location', 'permissions',)
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
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'types', 'location', 'goods', 'features', 'company__id')
    search_fields = ('name', 'types', 'location', 'goods', 'features')
    queryset = Truck.objects.all()


class PlaneViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = PlaneSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'types', 'location', 'goods', 'features', 'company__id')
    search_fields = ('name', 'types', 'location','goods', 'features')
    queryset = Plane.objects.all()


class TrainViewSet(DetailViewSet, NestedViewSetMixin):
    serializer_class = TrainSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'types', 'location','goods', 'features', 'company__id')
    search_fields = ('name', 'types', 'location','goods', 'features')
    queryset = Train.objects.all()


class FeatureViewSet(ModelViewSet, NestedViewSetMixin):
    serializer_class = FeatureSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    queryset = Features.objects.all()
